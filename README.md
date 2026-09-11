# Apps-UC

アプリやユースケース用のレポジトリ。
**React Native + Expo で100本のアプリを作り、後半はGoogle Play / App Storeで収益化する**ための作業場です。

## まずここから

| ドキュメント | 内容 |
|---|---|
| [ROADMAP.md](ROADMAP.md) | **全体計画**（5レベル・約12〜15か月のスケジュール） |
| [docs/00-setup-windows.md](docs/00-setup-windows.md) | **Windows環境構築 / インストールするもの一覧** ← 最初にやること |
| [docs/01-app-list-100.md](docs/01-app-list-100.md) | 100本のアプリ一覧とチェックリスト |
| [docs/02-deploy-stores.md](docs/02-deploy-stores.md) | ストア公開の全手順（Windowsから iOS も出す方法） |
| [docs/03-monetization.md](docs/03-monetization.md) | 収益化・計測・ASO |

## 構成

```
apps/
├─ 001-counter/        ← 1本1フォルダ。各フォルダに README.md で学びを記録
├─ 002-tip-calculator/
└─ ...
```

## 技術スタック

- **言語**: TypeScript
- **フレームワーク**: React Native (Expo)
- **ビルド/提出**: EAS Build / EAS Submit（Windowsから iOS もビルド可）
- **バックエンド**: Supabase（Lv.4以降）
- **課金**: RevenueCat（Lv.4以降）
