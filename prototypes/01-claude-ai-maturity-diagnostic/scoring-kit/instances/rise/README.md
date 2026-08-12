# Rise Consulting Group 専用インスタンス（型の使用例）

汎用テンプレート（`../../採点キット_SYSTEM.md`）の「会社ポリシー」スロットに、
Rise のAI利用ガバナンス（G1〜G8・A1〜A7準拠のスターター版）を差し込んだ**完成版キット**です。

## ファイル
- `採点キット_SYSTEM_Rise.md` … LLMにそのまま取り込める完成版（会社ポリシー差し込み済み）。
- `company-policy_Rise.md` … 差し込んだRiseのガバナンス（スターター版）。

## 使い方
1. `採点キット_SYSTEM_Rise.md` の中身を、お使いのLLM（ChatGPT/Gemini/Copilot/Claude/社内LLM）のシステム指示/カスタムアシスタントに丸ごと取り込む。
2. コンサルタントの証跡（プロンプト／会話ログ／シナリオ回答／成果物／GPT設定 等）を渡して「採点して」。
3. 4層（Maturity / Score100 / Evidence / Business Impact）＋10次元で採点され、Riseポリシー違反は red_flags に出る。

## 注意
`company-policy_Rise.md` は社内資料のガバナンス原則から構成した**スターター版**です。正式運用前に情報セキュリティ／法務の承認を得てください。会社ポリシーを差し替えれば、他社向けインスタンスも同様に作れます。
