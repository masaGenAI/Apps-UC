# 世界のAIリテラシー枠組み・セキュリティ／ガバナンス基準 — エビデンス一覧

個人のAIリテラシーとセキュリティ・ガバナンス意識をスコア化するルーブリック（`../scoring-kit/rubric.json`）の根拠として、世界の主要フレームワークを収集した一覧。

## サマリ

- 掲載: **28件**（ランク別 S:15 / A:3 / B:10 / C:0）
- 検証内訳: **本文fetch成功 4件** ／ **検索確認（fetch不可）24件**
- 領域: AIリテラシー教育枠組み（UNESCO/OECD/EU/Long&Magerko/AI4K12 等）＋ セキュリティ・ガバナンス基準（NIST/ISO/OWASP/MITRE/各国政府ガイドライン）

> **⚠ 検証方法に関する重要な但し書き（正直な開示）**  
> 本調査を実行した環境は、組織のegressポリシーにより **外部ドメインへの `WebFetch` が全面遮断（EGRESS_BLOCKED / 403）** されていました。そのため、`raw.githubusercontent.com` 上の文書（OWASP/MITRE）を除き、**一次文書の本文を開いて照合する完全検証は実施できていません**。  
> - **検証済（本文fetch成功）**: GitHub上の一次リポジトリを実際に取得し本文一致を確認した4件。  
> - **検索確認（本文fetch不可）**: URL・タイトル・発行機関・構造（コンピテンシー数・段階等）を **ライブWeb検索の結果で確認** したもの。URLは検索エンジンが返した実在の正規ページだが、本文全文の照合は未実施。数値・構造は検索要約由来であり、正式引用前に各一次文書の原本確認を推奨する。  
> この但し書きは、エビデンス調査スキルのハルシネーション防止原則（未検証を検証済と偽らない）に従うもの。

## エビデンス一覧

| No | タイトル | 発行機関 | 種別 | 地域 | 年 | ランク | 評価軸への示唆（要旨） | 検証 | URL |
|---|---|---|---|---|---|---|---|---|---|
| 1 | EU AI Act 第4条（AIリテラシー義務）— Regulation (EU) 2024/1689 | European Union（官報 EUR-Lex） | 政府機関（規制） | EU | 2024 | S | AIの提供者・利用者に、スタッフ等の十分なAIリテラシー確保を義務づける条文（2025-02-02適用開始）。組織的リテラシー要求の法的根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202401689> |
| 2 | DigComp 2.2: The Digital Competence Framework for Citizens | European Commission JRC | 政府機関（研究） | EU | 2022 | S | 市民のデジタル・コンピテンシー枠組み。5領域にAI関連の新規例示を70件超追加。情報評価・安全・問題解決の次元がL3・S1に接続。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://publications.jrc.ec.europa.eu/repository/handle/JRC128415> |
| 3 | Model AI Governance Framework for Generative AI (2024) | IMDA／AI Verify Foundation | 政府機関（関連団体） | シンガポール | 2024 | S | 生成AIガバナンスの9次元（Accountability／Data／Trusted Development & Deployment／Incident Reporting／Testing & Assurance／Security 等）。S1・S3・S4の実務枠組み。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://aiverifyfoundation.sg/wp-content/uploads/2024/05/Model-AI-Governance-Framework-for-Generative-AI-May-2024-1-1.pdf> |
| 4 | UNESCO AI competency framework for students (2024) | UNESCO | 国際機関 | 国際 | 2024 | S | 学生向けAIコンピテンシー枠組み。4側面（Human-centred mindset／Ethics of AI／AI techniques and applications／AI system design）×12コンピテンシーを、3段階の進行（Understand→Apply→Create）で整理。リテラシー次元L1・L4・L5・L6の根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.unesco.org/en/articles/ai-competency-framework-students> |
| 5 | UNESCO AI competency framework for teachers (2024) | UNESCO | 国際機関 | 国際 | 2024 | S | 教師向けAIコンピテンシー枠組み。5側面×3段階で15コンピテンシーを構成。人間中心アプローチ。育成・研修設計（UC-23/24）の参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.unesco.org/en/articles/ai-competency-framework-teachers> |
| 6 | Empowering Learners for the Age of AI — AI Literacy Framework (AILit) | OECD／European Commission | 国際機関 | 国際 | 2025 | S | 初等中等教育向けAIリテラシー枠組み。4ドメイン（Engage with AI／Create with AI／Manage AI／Shape AI）×22コンピテンス、basic/intermediate/advancedの進行。リテラシー次元L2・L3・L6の根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.oecd.org/en/publications/empowering-learners-for-the-age-of-ai_65cd27d4-en.html> |
| 7 | AI Literacy Framework for Primary & Secondary Education (AILit 公式サイト) | OECD／European Commission (with Code.org) | 国際機関 | 国際 | 2025 | S | AILit枠組みの一次公開サイト。knowledge/skills/attitudesの構造とドメイン別のLearner Expectationsを提供。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://ailiteracyframework.org/> |
| 8 | AI事業者ガイドライン（第1.1版） | 総務省・経済産業省 | 政府機関 | 日本 | 2025 | S | 人間中心・安全性・公平性・透明性等の原則を、AI開発者/提供者/利用者の別に整理したソフトロー。S3（人間中心）・S5（安全性）の国内根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.soumu.go.jp/main_content/001002576.pdf> |
| 9 | 初等中等教育段階における生成AIの利活用に関するガイドライン Ver.2.0 | 文部科学省 | 政府機関 | 日本 | 2024 | S | 教育現場での生成AI利活用の考え方・留意点。適用範囲の判断（L6）と統制（S3）の国内参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.mext.go.jp/content/20241226-mxt_shuukyo02-000030823_001.pdf> |
| 10 | デジタルスキル標準（DXリテラシー標準／DX推進スキル標準） | IPA・経済産業省 | 政府機関 | 日本 | 2024 | S | 全ビジネスパーソン向けのDXリテラシーに生成AIのマインド・スタンス（問い立て・仮説検証・継続学習）を追加。L4・L2の国内根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.ipa.go.jp/jinzai/skill-standard/dss/rcu1hd000000j76k-att/dss_ver1.2.pdf> |
| 11 | 行政の進化と革新のための生成AIの調達・利活用に係るガイドライン（DS-920） | デジタル庁 | 政府機関 | 日本 | 2025 | S | 行政における生成AIの調達・利活用の統制指針。S1・S3・S4の国内実務参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/e2a06143-ed29-4f1d-9c31-0f06fca67afc/80419aea/20250527_resources_standard_guidelines_guideline_01.pdf> |
| 12 | Artificial Intelligence and the Future of Teaching and Learning | U.S. Department of Education, Office of Ed Tech | 政府機関 | 米国 | 2023 | S | 教育におけるAIの機会とリスク、7つの提言。人間中心・信頼・公平の原則。育成方針の一次参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.ed.gov/sites/ed/files/documents/ai-report/ai-report.pdf> |
| 13 | NIST AI Risk Management Framework (AI RMF 1.0), AI 100-1 | NIST（米国国立標準技術研究所） | 政府機関 | 米国 | 2023 | S | AIリスク管理の中核枠組み。4機能（Govern／Map／Measure／Manage）と7つの信頼性特性。S3（統制・説明責任）の骨格。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf> |
| 14 | NIST Generative AI Profile, NIST AI 600-1 | NIST | 政府機関 | 米国 | 2024 | S | 生成AI固有/増幅の12リスク（Confabulation, Data Privacy, Information Security, Information Integrity, IP 等）と、Govern/Content Provenance/Pre-deployment Testing/Incident Disclosureの統制アクション。S1・S2・S4・S5の根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf> |
| 15 | Generative AI Framework for HMG | UK Cabinet Office / CDDO | 政府機関 | 英国 | 2024 | S | 英国政府職員向け生成AI活用の10原則（限界の理解、合法・倫理・責任、安全、意味ある人間の統制、適材適所、ライフサイクル管理 等）。S2・S3の実務原則。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.gov.uk/government/publications/generative-ai-framework-for-hmg> |
| 16 | Elements of AI（無料オンライン講座） | University of Helsinki + MinnaLearn/Reaktor | 大学 | フィンランド | 2018 | A | AIの基礎を6章（What is AI／problem solving／real world AI／machine learning／neural networks／implications）で学ぶ世界的リテラシー講座。L1の到達基準の参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.elementsofai.com/> |
| 17 | MITRE ATLAS — Adversarial Threat Landscape for AI Systems | MITRE Corporation | 研究所（FFRDC） | 国際／米国 | 2026 | A | AIシステムへの敵対的TTPの公開ナレッジベース。16戦術と100超の技術（LLM Prompt Injection／Jailbreak／Data Leakage／RAG Poisoning 等）。S2の脅威モデリング基盤。 | 検証済（本文fetch成功） | <https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/ATLAS.yaml> |
| 18 | What is AI Literacy? Competencies and Design Considerations | Long, D. & Magerko, B.（ACM CHI 2020） | 学術（査読） | 米国 | 2020 | A | AIリテラシーを16コンピテンシー＋設計上の考慮として定義した被引用数の多い査読論文。『理解・効果的な協働・批判的評価』の学術的定義。L1・L3・L4の根拠。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://dl.acm.org/doi/10.1145/3313831.3376727> |
| 19 | Article 4: AI literacy（条文参照リポジトリ） | Future of Life Institute（非公式集約） | 業界団体・第三者 | EU | 2024 | B | EU AI Act第4条の全文と関連リサイタルを参照しやすく集約した著名な二次サイト（一次はEUR-Lex）。条文の実務解釈の入口。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://artificialintelligenceact.eu/article/4/> |
| 20 | ISO/IEC 42001:2023 — AI management system (AIMS) | ISO/IEC | 標準化機関 | 国際 | 2023 | B | 世界初のAIマネジメントシステム標準。条項4-10（文脈・リーダーシップ・計画・支援・運用・評価・改善）とデータガバナンス。組織統制S3・S4の枠組み。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.iso.org/standard/42001> |
| 21 | ISO/IEC 23894:2023 — AI risk management guidance | ISO/IEC | 標準化機関 | 国際 | 2023 | B | AIに関するリスクマネジメントの指針（ISO 31000のAI適用）。リスク特定・分析・対応の共通言語。S1・S3の参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.iso.org/standard/77304.html> |
| 22 | ISO/IEC 22989:2022 — AI concepts and terminology | ISO/IEC | 標準化機関 | 国際 | 2022 | B | AIの概念と用語の国際標準。評価・統制の用語基盤。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://www.iso.org/standard/74296.html> |
| 23 | OWASP Top 10 for LLM Applications 2026 | OWASP GenAI Security Project | 業界団体・NPO | 国際 | 2026 | B | LLMアプリの重大脅威Top10（LLM01 Prompt Injection／LLM02 Sensitive Information Disclosure／LLM03 Excessive Agency／LLM04 Supply Chain／LLM05 Data & Model Poisoning／…／LLM10 Improper Output Handling）。S2の中核。 | 検証済（本文fetch成功） | <https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md> |
| 24 | OWASP LLM01:2026 Prompt Injection（詳細） | OWASP GenAI Security Project | 業界団体・NPO | 国際 | 2026 | B | プロンプトインジェクションの定義・直接/間接分類・信頼レベル（untrusted/semi-trusted/trusted）・防御（役割制限、出力スキーマ検証、権限最小化、不可逆操作前の人間承認 等）。S2の評価軸を直接提供。 | 検証済（本文fetch成功） | <https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/2026/final/LLM01_PromptInjection.md> |
| 25 | OWASP LLM01:2025 Prompt Injection（詳細） | OWASP GenAI Security Project | 業界団体・NPO | 国際 | 2025 | B | 2025版の7緩和策（役割定義、出典引用を含む出力検証、入出力フィルタ、最小権限、機微操作への人間承認、外部コンテンツ分離、敵対的テスト）。S2・S5の根拠。 | 検証済（本文fetch成功） | <https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/2025/LLM01_PromptInjection.md> |
| 26 | AI4K12 — Five Big Ideas in AI | AI4K12 Initiative（AAAI／CSTA） | 業界団体・NPO | 米国 | 2020 | B | K-12向けの5大アイデア（Perception／Representation & Reasoning／Learning／Natural Interaction／Societal Impact）。AIの仕組み理解（L1）と社会影響（L5）の骨格。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://ai4k12.org/> |
| 27 | ISTE Standards（Students/Educators/Leaders） | ISTE（International Society for Technology in Education） | 業界団体・NPO | 米国 | 2024 | B | AIの能力と限界の理解、倫理的利用、責任ある創作、批判的評価などをうたう教育標準。リテラシー次元の実践的アンカー。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://iste.org/standards> |
| 28 | AI Literacy: A Framework to Understand, Evaluate, and Use Emerging Technology | Digital Promise | 研究所・NPO | 米国 | 2024 | B | AIリテラシーを3モード（Understand／Evaluate／Use）×6実践で整理。L2・L3の実務的分解の参照。 | 検索確認（本文fetch不可・当環境egress遮断） | <https://digitalpromise.org/2024/06/18/ai-literacy-a-framework-to-understand-evaluate-and-use-emerging-technology/> |

## 調査メタ

- 調査日: 2026-08-11
- 手法: 並列調査ワークフロー（8クラスタ）＋主ループでのWebSearch確認。候補URL 78件超を収集。
- 制約: 当環境のegressポリシーにより外部WebFetchが遮断。GitHub raw のみfetch可。
- ランク定義: S=政府・国際機関 / A=大学・研究機関・査読 / B=業界団体・標準化機関・第三者 / C=民間調査（本一覧にC無し）。

_アプリ・ユースケースラボ Prototype 01 — evidence-research スキルに基づく_