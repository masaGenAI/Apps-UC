# Prototype 01 — AIケイパビリティ成熟度アセスメント（Claude）v2

> **元ユースケース：UC-29 AI成熟度診断サービス（外販・◆本命）＋ UC-23 AIケイパビリティ測定キット**
> 提出物（証跡）を**お使いのLLM（任意）**に読ませ、AI活用型ビジネスコンサルタントのAIケイパビリティを
> **CMMI型5段階 × 10ディメンション**で採点。**能力／証跡信頼度／ビジネス価値を分離した4層**で示す。

## 設計思想（v2の土台）

Rise Consulting Group 向け「AIケイパビリティ成熟度モデル」（DeepResearch）の設計思想を**汎用テンプレート化**したもの。
- 既存標準の役割分担：**CMMI AIM＝縦軸（成熟度5段階）／SFIA＋AI Skills for Business＝横軸（次元・自律性・影響範囲）／NIST・ISO・OECD・EU AI Act＝ゲート（最低条件）**、測定の妥当性（Standards for Educational and Psychological Testing）。
- **単一総合点で人を序列化しない**：4層出力（下記）。
- **証跡ベース**：証跡強度 E0–E5。「証跡が無い≠能力が低い」→ `insufficient_evidence`。
- **本人の担当分とAI生成分を切り分ける**／**誤評価防止**（利用量・長さ・見栄え・モデル/ツール数・コード行数で加点しない、失敗/ログ不在/機密実績で減点しない）。
- **AIエンジニアとしてでなく、AIで顧客価値を生むコンサルタント**として評価。

## 出力の4層

1. **Capability Maturity**：総合成熟度 L1–5（ゲート補正あり）
2. **Capability Score**：10次元の加重合計 0–100（カバレッジ%付き）
3. **Evidence Confidence**：証跡の強さ E0–E5
4. **Business Impact**：組織・顧客への寄与（能力とは**別建て**。自己申告/推定/実測を区別）

## 10ディメンション（weight）
D1 AIリテラシー(6)／D2 課題設定(14)【ゲート】／D3 対話&プロンプト/コンテキスト設計(14)／D4 リサーチ&知識統合(12)／D5 コンサル適用(16)／D6 GPT・エージェント設計(8)／D7 AI支援開発&分析(8)／D8 評価&QA(8)【ゲート】／D9 Responsible AI・セキュリティ(8)【ゲート・会社ポリシー差し込み】／D10 ワークフロー&再利用(6)。

**ゲート方式**：D2／D8／D9 の最低LevelがL1なら総合Maturityを最大L2、L2なら最大L3に制限（証跡E0も最大L2）。総合が高くてもResponsible AI等が未成熟なら実務上信頼できないため。

## 「型」と会社ポリシー差し込み（重要）

このキットは**型（テンプレート）**。**セキュリティ・ガバナンス（D9）とゲートは各社が自社のガイドライン・規程を差し込んで**使います。

```
scoring-kit/
├── 採点キット_SYSTEM.md        … 型（汎用・会社ポリシーはスロット）※rubric_v2.jsonから自動生成
├── rubric_v2.json             … 評価モデルの正（10次元・5段階・ウェイト・ゲート・E0-E5）
├── company-policy.template.md … 会社ポリシー記入フォーム（差し込みスロット）
├── 使い方.md ／ scenarios.md
└── instances/
    └── rise/                   … 型のインスタンス例（Riseのガバナンスを差し込み済み）
        ├── 採点キット_SYSTEM_Rise.md
        └── company-policy_Rise.md
```

他社向けは `company-policy.template.md` を記入して差し替えれば同様にインスタンス化できます。

## 使う（2経路）

### A. 採点キット（主役）— 任意LLMにインポート
`採点キット_SYSTEM.md`（またはRise版）を、ChatGPT GPTs／Gemini Gems／Copilot／Claude Project／社内LLMのシステム指示に取り込み、証跡を渡して「採点して」。

### B. HTMLハーネス（可視化）— [`index.html`](./index.html)
- **公開Artifact**：https://claude.ai/code/artifact/4e85945c-23c2-45a3-a777-dad2b3ddb86d
- Step 1：証跡（＋任意で会社ポリシー）を入れて採点プロンプトを自動生成→コピー。
- Step 2：LLMの採点結果JSONを貼ると、**4層KPI／10次元レーダー／ディメンション別（引用・本人担当分）／ゲート／会社ポリシー違反／Business Impact／強み・次の一手**を描画。
- **PDF出力**：「📄 PDFで出力（印刷）」→ ブラウザの「PDFとして保存」で、採点結果を**1枚のレポートPDF**として出力（印刷用レイアウトに最適化）。Markdown保存も可。出力例：[`sample-scorecard.pdf`](./sample-scorecard.pdf)。

## 想定KPI
- UC-23：研修前後の Capability Maturity／Score／カバレッジの変化（証跡強度を上げながら）
- UC-29：外販時のクライアント社員の分布・ゲート該当率・改善度

## 出典・限界
評価モデルの根拠は [`research/`](./research/)（世界フレームワーク28件）と `rubric_v2.json`。Rise向けPDF（設計思想の一次資料）は9ページ目以降が画像で、結論・比較・提言部＋DeepResearchプロンプトから設計思想を反映。`company-policy_Rise.md` は社内資料G1–G8/A1–A7から構成したスターター版（正式運用前に情報セキュリティ／法務の承認を）。証跡が単一・少量（E0–E1）のときは暫定評価。人事評価に直結させない（G2）。

> 旧版：組織成熟度診断は [`index-org-maturity.html`](./index-org-maturity.html)。v1（リテラシー6＋セキュリティ5次元）はgit履歴に保存。

---
_アプリ・ユースケースラボ Prototype 01 v2 — Claude（Artifacts＋採点キット）で作成_
