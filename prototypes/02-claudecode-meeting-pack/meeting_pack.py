#!/usr/bin/env python3
"""
meeting_pack.py — 会議自動化パック (UC-16)
==========================================

文字起こし（プレーンテキスト）を入力に、以下を1コマンドで生成する
Claude Code 向けのプロトタイプ・キット。

  1. 議事録 (Markdown)      : 要旨・論点・決定事項・保留事項
  2. 決定事項リスト          : Decision と根拠
  3. タスク抽出              : タスク / 担当 / 期限 / 優先度 (Markdown表 + JSON)

設計方針（元資料に準拠）
  - G5 : プロンプト・様式は Markdown/JSON の汎用形式で外部化し、ツール交代に耐える。
  - G1 : 秘匿情報の投入区分は運用側の責任。--redact で人名などを匿名化してから送出可能。
  - A1 : 出力の最終責任は人間。生成物には必ずレビュー欄を付す。

動作モード
  - 既定             : Anthropic API (Claude) を呼び、構造化 JSON を得る。
                       環境変数 ANTHROPIC_API_KEY が必要。
  - --offline        : APIを使わず、内蔵のルールベース抽出で動く（デモ/CI用）。
                       ネットワークやキー無しでも成果物の形を確認できる。

使い方
  python meeting_pack.py sample_transcript.txt
  python meeting_pack.py sample_transcript.txt --offline
  python meeting_pack.py sample_transcript.txt --offline --redact -o out/
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# プロンプト（G5: 様式は外部化して汎用形式で管理）
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = """あなたは経営コンサルティングファームの会議書記です。
会議の文字起こしを読み、事実に基づいて簡潔に構造化します。
- 推測で情報を補わない。文字起こしに無い担当者・期限は "未定" とする。
- 決定事項(decision)と、単なる意見・検討中の論点(discussion)を区別する。
- タスクは動詞で始め、担当と期限を可能な限り特定する。
出力は指定のJSONスキーマに厳密に従うこと。"""

USER_TEMPLATE = """次の会議文字起こしを構造化してください。

# 会議タイトル
{title}

# 文字起こし
{transcript}

# 出力スキーマ (JSONのみ、前後に文章を付けない)
{{
  "summary": "3〜5文の要旨",
  "decisions": [{{"decision": "決定事項", "rationale": "根拠/背景"}}],
  "discussion_points": ["結論の出ていない論点"],
  "tasks": [
    {{"task": "動詞で始まるタスク", "owner": "担当者名 or 未定",
      "due": "YYYY-MM-DD or 相対表現 or 未定", "priority": "高|中|低"}}
  ],
  "open_questions": ["次回までに解消すべき問い"]
}}"""

# 構造化出力用ツールスキーマ（Anthropic tool use）
OUTPUT_TOOL = {
    "name": "emit_minutes",
    "description": "会議の構造化結果を提出する",
    "input_schema": {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "decisions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "decision": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["decision"],
                },
            },
            "discussion_points": {"type": "array", "items": {"type": "string"}},
            "tasks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "task": {"type": "string"},
                        "owner": {"type": "string"},
                        "due": {"type": "string"},
                        "priority": {"type": "string", "enum": ["高", "中", "低"]},
                    },
                    "required": ["task", "owner", "due", "priority"],
                },
            },
            "open_questions": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["summary", "decisions", "tasks"],
    },
}

MODEL = os.environ.get("MEETING_PACK_MODEL", "claude-sonnet-4-5")


# --------------------------------------------------------------------------- #
# 匿名化 (G1: 顧客秘密/個人情報の投入区分に配慮)
# --------------------------------------------------------------------------- #
def redact(text: str) -> tuple[str, dict]:
    """『氏名さん/部長』等の敬称付き固有名を [PERSON_n] に置換し、対応表を返す。"""
    mapping: dict[str, str] = {}
    pat = re.compile(r"([一-龥ァ-ヴA-Za-z]{2,5})(さん|部長|課長|マネージャー|PM|リーダー)")
    counter = [0]

    def sub(m: re.Match) -> str:
        name = re.sub(r"^[はがのをにへともで、。」）\s]+", "", m.group(1)) or m.group(1)
        if name not in mapping:
            counter[0] += 1
            mapping[name] = f"[PERSON_{counter[0]}]"
        return mapping[name] + m.group(2)

    return pat.sub(sub, text), mapping


# --------------------------------------------------------------------------- #
# オフライン抽出（デモ/CI用のルールベース。LLM無しでも成果物の形を確認できる）
# --------------------------------------------------------------------------- #
DECISION_CUES = ["決定", "決めた", "承認", "GO", "合意", "確定", "方針とする", "で進める"]
TASK_CUES = ["やる", "対応", "作成", "準備", "まとめ", "確認", "共有", "連絡", "調整",
             "レビュー", "実測", "整備", "策定", "検討する", "まで", "までに"]
OWNER_PAT = re.compile(r"([一-龥ァ-ヴA-Za-z]{2,5})(さん|部長|課長|マネージャー|PM|リーダー)")


def _clean_owner(match: re.Match) -> str:
    """助詞などを剥がして 氏名+敬称 だけを返す（例: 'は佐藤さん'→'佐藤さん'）。"""
    name = re.sub(r"^[はがのをにへともで、。」）\s]+", "", match.group(1))
    return (name or match.group(1)) + match.group(2)
DUE_PAT = re.compile(r"(\d{1,2}/\d{1,2}|来週|今週中|月末|\d+日以内|次回|明日|\d{4}-\d{2}-\d{2})")


def _priority(line: str) -> str:
    if any(w in line for w in ["至急", "最優先", "今週中", "明日", "リスク"]):
        return "高"
    if any(w in line for w in ["いずれ", "余裕", "できれば"]):
        return "低"
    return "中"


def offline_extract(transcript: str, title: str) -> dict:
    lines = [ln.strip() for ln in transcript.splitlines() if ln.strip()]
    # 発言本文のみ（"話者: 発言" 形式に対応）
    utterances = []
    for ln in lines:
        body = ln.split(":", 1)[1].strip() if ":" in ln[:12] else ln
        for seg in re.split(r"[。！？\n]", body):
            seg = seg.strip()
            if seg:
                utterances.append(seg)

    decisions, tasks, discussion, questions = [], [], [], []
    for seg in utterances:
        if any(c in seg for c in DECISION_CUES):
            decisions.append({"decision": seg, "rationale": ""})
        elif seg.endswith("か") or "どうする" in seg or "べきか" in seg:
            questions.append(seg)
        elif any(c in seg for c in TASK_CUES):
            owner_m = OWNER_PAT.search(seg)
            due_m = DUE_PAT.search(seg)
            tasks.append({
                "task": seg,
                "owner": _clean_owner(owner_m) if owner_m else "未定",
                "due": due_m.group(0) if due_m else "未定",
                "priority": _priority(seg),
            })
        elif len(seg) > 12:
            discussion.append(seg)

    summary = "（オフライン抽出）" + "。".join(u for u in utterances[:3]) + "。" if utterances else "（内容なし）"
    return {
        "summary": summary,
        "decisions": decisions,
        "discussion_points": discussion[:6],
        "tasks": tasks,
        "open_questions": questions[:6],
    }


# --------------------------------------------------------------------------- #
# LLM 抽出（既定モード）
# --------------------------------------------------------------------------- #
def llm_extract(transcript: str, title: str) -> dict:
    try:
        import anthropic  # noqa: WPS433
    except ImportError:
        sys.exit("anthropic SDK 未インストールです。`pip install anthropic` するか --offline を使ってください。")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("環境変数 ANTHROPIC_API_KEY が未設定です。--offline でデモ実行できます。")

    client = anthropic.Anthropic()
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        tools=[OUTPUT_TOOL],
        tool_choice={"type": "tool", "name": "emit_minutes"},
        messages=[{"role": "user",
                   "content": USER_TEMPLATE.format(title=title, transcript=transcript)}],
    )
    for block in msg.content:
        if getattr(block, "type", None) == "tool_use":
            return block.input
    sys.exit("LLM から構造化出力が得られませんでした。")


# --------------------------------------------------------------------------- #
# レンダリング
# --------------------------------------------------------------------------- #
def render_markdown(data: dict, title: str, meta: dict) -> str:
    today = meta["date"]
    lines = [
        f"# 議事録 — {title}",
        "",
        f"- **日付**: {today}",
        f"- **生成**: 会議自動化パック (UC-16) / mode=`{meta['mode']}`"
        + ("・匿名化済" if meta["redacted"] else ""),
        f"- **レビュー担当**: ______（A1: 出力の最終責任は人間。承認前に必ず確認）",
        "",
        "## 要旨",
        data.get("summary", "—"),
        "",
        "## 決定事項",
    ]
    decisions = data.get("decisions", [])
    if decisions:
        for i, d in enumerate(decisions, 1):
            r = f" — {d['rationale']}" if d.get("rationale") else ""
            lines.append(f"{i}. **{d['decision']}**{r}")
    else:
        lines.append("_（明確な決定事項は検出されませんでした）_")

    lines += ["", "## タスク", "", "| # | タスク | 担当 | 期限 | 優先 |", "|---|---|---|---|---|"]
    tasks = data.get("tasks", [])
    if tasks:
        for i, t in enumerate(tasks, 1):
            lines.append(
                f"| {i} | {t['task']} | {t.get('owner','未定')} | {t.get('due','未定')} | {t.get('priority','中')} |"
            )
    else:
        lines.append("| — | （タスクなし） | — | — | — |")

    disc = data.get("discussion_points", [])
    if disc:
        lines += ["", "## 論点（結論未確定）"]
        lines += [f"- {d}" for d in disc]

    oq = data.get("open_questions", [])
    if oq:
        lines += ["", "## 次回までに解消する問い"]
        lines += [f"- [ ] {q}" for q in oq]

    lines += ["", "---",
              "_Generated by 会議自動化パック (UC-16) — アプリ・ユースケースラボ Prototype 02_"]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="会議自動化パック (UC-16): 文字起こし→議事録/決定/タスク")
    ap.add_argument("transcript", help="文字起こしテキストファイル (.txt)")
    ap.add_argument("-o", "--out", default=".", help="出力ディレクトリ (既定: カレント)")
    ap.add_argument("-t", "--title", default=None, help="会議タイトル (既定: ファイル名)")
    ap.add_argument("--offline", action="store_true", help="LLMを使わずルールベース抽出（デモ/CI用）")
    ap.add_argument("--redact", action="store_true", help="人名を匿名化してから処理 (G1)")
    args = ap.parse_args(argv)

    src = Path(args.transcript)
    if not src.exists():
        print(f"入力が見つかりません: {src}", file=sys.stderr)
        return 1
    transcript = src.read_text(encoding="utf-8")
    title = args.title or src.stem

    redaction_map: dict = {}
    if args.redact:
        transcript, redaction_map = redact(transcript)

    mode = "offline" if args.offline else f"llm:{MODEL}"
    data = offline_extract(transcript, title) if args.offline else llm_extract(transcript, title)

    meta = {
        "date": _dt.date.today().isoformat(),
        "mode": mode,
        "redacted": bool(redaction_map),
    }

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    md_path = outdir / f"{title}_minutes.md"
    json_path = outdir / f"{title}_tasks.json"

    md_path.write_text(render_markdown(data, title, meta), encoding="utf-8")
    json_path.write_text(
        json.dumps(
            {"meta": meta, **data,
             "redaction_map": {v: k for k, v in redaction_map.items()} if redaction_map else {}},
            ensure_ascii=False, indent=2,
        ),
        encoding="utf-8",
    )

    print(f"✓ 議事録   : {md_path}")
    print(f"✓ タスク   : {json_path}")
    print(f"  mode={mode}  decisions={len(data.get('decisions',[]))}  tasks={len(data.get('tasks',[]))}")
    if args.offline:
        print("  ※ offline はルールベースのデモ抽出です。実運用は ANTHROPIC_API_KEY を設定し LLM モードで。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
