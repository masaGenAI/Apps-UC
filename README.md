# Apps-UC — アプリ・ユースケースラボ

社内AIユースケース・ポートフォリオ資料（39件・2段スクリーニング通過）をもとに、
**実際に触れるプロトタイプ**を作っていくラボ。まずは Claude / Claude Code / Claude Cowork の
それぞれの強みに合わせて、代表ユースケースを1つずつ形にした。

## プロトタイプ一覧

| # | プロトタイプ | プラットフォーム | 元ユースケース | 形式 |
|---|---|---|---|---|
| 01 | [AIケイパビリティ成熟度アセスメント](./prototypes/01-claude-ai-maturity-diagnostic/) | **Claude**（Artifacts＋採点キット） | UC-29 AI成熟度診断（外販）＋ UC-23 測定キット | 採点キット（型＋Rise版）＋HTMLハーネス |
| 02 | [会議自動化パック](./prototypes/02-claudecode-meeting-pack/) | **Claude Code** | UC-16 会議自動化（議事録・タスク抽出） | Python CLIキット |
| 03 | [競合モニタリング Skill](./prototypes/03-cowork-competitive-monitor/) | **Claude Cowork** | UC-05 競合モニタリング配信 ＋ UC-53 ベンチマーク更新 | SKILL.mdキット |

> **公開Artifact（01）**：https://claude.ai/code/artifact/4e85945c-23c2-45a3-a777-dad2b3ddb86d

## なぜこの3つを、この3プラットフォームで作ったか

3プラットフォームは「同じことを別の場所でやる」ものではなく、**担当領域が違う**。
選抜資料の適格性テスト（チャットで済むものはUC化しない）に沿って役割分担した。

- **Claude（Artifacts＋採点キット）** … *触ってもらう体験*が価値になるもの。採点キットをLLMに読ませ、実際に書いた文章をスコア化。
  → AIリテラシー＆セキュリティ・ガバナンス アセスメント（UC-29/23）。世界標準フレームワーク準拠の外販ツールに最適。
- **Claude Code** … *コード資産・パイプライン*として持つべきもの。CLI化・自動化・様式の外部化。
  → 会議自動化パック（UC-16）。適格性テストで「チャット代替不可（ルールA）」判定の領域。
- **Claude Cowork** … *複数アプリを横断するエージェント作業*。Web検索・Gmail・Notionを跨いで完結。
  → 競合モニタリング（UC-05/53）。定期起動と配信の仕組みが要る領域。

## 各プロトタイプが守っている共通原則（元資料より）

- **G1**：データ投入可否の区分（公開/社内限/顧客秘密/個人情報）。プロトタイプは公開情報のみ／匿名化前提。
- **G5**：プロンプト・様式は Markdown/JSON の汎用形式で外部化し、製品交代に耐える。
- **A1 / G2**：出力の最終責任は人間。生成物はレビュー欄・下書き止まりにして無断確定を防ぐ。
- **G6**：重要な示唆は2モデルで独立検証（該当プロトタイプで任意運用）。

## リポジトリ構成

```
prototypes/
├── 01-claude-ai-maturity-diagnostic/   # Claude（採点キット＋HTMLハーネス）
│   ├── index.html                      # 採点結果を可視化するハーネス（Artifact）
│   ├── index-org-maturity.html         # 旧・組織成熟度診断（温存）
│   ├── scoring-kit/                    # LLMに読ませる採点キット（主役）
│   ├── research/                       # 世界フレームワークのエビデンス一覧(md+xlsx)
│   └── README.md
├── 02-claudecode-meeting-pack/         # Claude Code（Python CLI）
│   ├── meeting_pack.py
│   ├── sample_transcript.txt
│   └── README.md
└── 03-cowork-competitive-monitor/      # Claude Cowork（Skill）
    ├── SKILL.md
    ├── references/
    └── README.md
```

## 次にやること（このラボの続き）

- 第1波の★ユースケース（UC-12 会社フォーマット再現スライドキット 等）のプロトタイプ化
- 各プロトタイプの Before 実測テンプレ整備（KPIを取れる状態にする）
- UC-44 マルチクラウドLLM評価ハーネス（◆本命）の骨格
