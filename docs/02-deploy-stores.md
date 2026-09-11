# ストア公開の全手順（Windows から iOS / Android を出す）

このドキュメントは **Lv.3 の 060番** で初めて使います。それ以前に読む必要はありません。
ただし **アカウント登録だけは早めに**（審査・本人確認に時間がかかるため）。

---

## 0. Windowsユーザーの結論

| | Android | iOS |
|---|---|---|
| ビルド | ローカルでも可 / **EAS Build（クラウド）推奨** | **EAS Build 一択**（Appleのビルドには macOS が必要なため、Expoのクラウド上のMacを借りる） |
| 実機確認 | 端末をUSB接続 or Expo Go | **Expo Go または TestFlight**（Windows に iOSシミュレータは存在しない） |
| 提出 | `eas submit` | `eas submit` |

つまり **Mac を買わなくても App Store に出せます。** ただし iOSの細かい表示崩れは実機でしか確認できないので、**iPhone実機は1台用意してください**（古い機種で構いません）。

---

## 1. 事前に用意するもの（公開の1か月前に着手）

### 1-1. 開発者アカウント
| | Google Play Console | Apple Developer Program |
|---|---|---|
| URL | https://play.google.com/console | https://developer.apple.com/programs/ |
| 費用 | **$25（初回のみ・永久）** | **約$99 / 年（更新必須）** |
| 必要なもの | Googleアカウント、本人確認書類、住所・電話番号 | Apple ID（**2ファクタ認証必須**）、支払い用カード |
| 所要 | 数日〜2週間（本人確認） | 数日〜2週間（審査） |
| 注意 | **個人アカウントは「クローズドテストを一定人数・一定期間実施」しないと本番公開できません**（例：テスター12人以上を14日間継続。**要件は変更されるため必ず公式ページで最新を確認**）。テスターの確保を早めに始めること | 組織名で出す場合は D-U-N-S番号 が必要。個人名で出すなら不要 |

### 1-2. 必須アセット（作っておく）
- **アプリアイコン** 1024×1024 PNG（透過・角丸なし）
- **スプラッシュ画像**
- **スクリーンショット**
  - iOS: iPhone 6.7インチ級のサイズが必須（App Store Connect が指定するサイズを確認）
  - Android: スマホ用に最低2枚 + **フィーチャーグラフィック 1024×500**
  - → **これは「広告」です。**画面のスクショをそのまま貼るのではなく、キャッチコピーを載せた画像を作ること（Canva等でOK）
- **プライバシーポリシーのURL**（両ストアで必須）
  - GitHub Pages や Notion の公開ページで十分。「収集する情報 / 利用目的 / 第三者提供 / 問い合わせ先」を記載
- **問い合わせ先メールアドレス**
- ストア説明文（短い説明 / 長い説明）、キーワード

---

## 2. アプリ側の設定（`app.json`）

```jsonc
{
  "expo": {
    "name": "アプリ名",                    // ホーム画面に出る名前
    "slug": "my-app",
    "version": "1.0.0",                    // ユーザーに見えるバージョン
    "icon": "./assets/icon.png",
    "ios": {
      "bundleIdentifier": "com.yourname.myapp",  // ★一度決めたら変更不可
      "buildNumber": "1",
      "infoPlist": {
        "NSCameraUsageDescription": "写真を撮影してメモに添付するために使用します"
        // ★権限の説明文は「なぜ必要か」を具体的に書く。曖昧だと審査でリジェクトされます
      }
    },
    "android": {
      "package": "com.yourname.myapp",     // ★一度決めたら変更不可
      "versionCode": 1,
      "permissions": ["CAMERA"]
    }
  }
}
```

> `bundleIdentifier` / `package` は **公開後に変更できません**（変更＝別アプリ扱い）。ドメイン風の一意な文字列にしてください。

---

## 3. ビルド（EAS Build）

```powershell
cd C:\dev\Apps-UC\apps\060-my-app

eas login
eas build:configure          # eas.json が生成される

# Android（.aab ファイルが出来る）
eas build --platform android --profile production

# iOS（.ipa ファイルが出来る）
eas build --platform ios --profile production
```

- 初回の iOS ビルドで **Apple IDとパスワードを聞かれます**。「EASに証明書の管理を任せますか？」には **Yes**。
  （証明書・プロビジョニングプロファイルという難関を自動化してくれます。手動でやる必要はありません）
- 初回の Android ビルドで **キーストアを生成するか** 聞かれます → **Yes（EASに管理を任せる）**。
  > ⚠️ キーストアを失うとそのアプリを二度と更新できません。EAS管理にしておけば紛失リスクを避けられます。
- ビルドは**クラウド上で10〜30分**かかります。無料プランは順番待ちが発生します。

---

## 4. 提出（EAS Submit）

```powershell
# Google Play へ
eas submit --platform android --latest

# App Store へ
eas submit --platform ios --latest
```

- **Android の初回だけ手動作業が必要**：Play Console で先にアプリを作成し、**1本目の .aab は手動アップロード**する必要があります。また `eas submit` の自動化には **Google Cloud のサービスアカウントJSONキー** を作成して登録します（Expo公式ドキュメントに手順あり）。
- **iOS は `eas submit` で App Store Connect に上がります。** その後 App Store Connect の画面で、スクショ・説明文・年齢レーティング・輸出コンプライアンス（「暗号化を使用していますか？」→ 通常 HTTPS のみなら該当なしを選択）を入力し、**「審査へ提出」** を押します。

---

## 5. 審査を通すためのチェックリスト

### 両ストア共通
- [ ] クラッシュしない（審査員は必ず変な操作をします）
- [ ] ログインが必要なら **テスト用アカウントを審査メモに記載**（これ忘れが最頻出の差し戻し原因）
- [ ] プライバシーポリシーURLが実際に開ける
- [ ] 権限（カメラ・位置情報など）を**実際に使っている**。使わない権限は要求しない
- [ ] 他社の商標・キャラクター画像を使っていない

### Apple（特に厳しい点）
- [ ] **ガイドライン 4.2「最低限の機能」** — 単機能すぎる、Webサイトを包んだだけ、他アプリの模倣はリジェクト。
      **→ Lv.1〜2の練習アプリを出してはいけない理由がこれです。**
- [ ] **アカウント登録機能があるなら、アプリ内に「アカウント削除」機能が必須**
- [ ] SNSログイン（Google等）を提供するなら **「Appleでサインイン」も併せて提供**が必要になるケースがある
- [ ] デジタルコンテンツの販売は **必ずApp内課金（IAP）** を使う。外部決済へ誘導すると即リジェクト
- [ ] 未成年が使う可能性があるなら年齢レーティングを正しく申告

### Google Play
- [ ] **データセーフティ（Data safety）フォーム**を正確に記入（実装と食い違うと公開停止）
- [ ] コンテンツレーティングのアンケートに回答
- [ ] ターゲットAPIレベルの要件を満たす（Expo SDKを最新に保てば自動で満たせます）
- [ ] 個人アカウントは**クローズドテスト要件**をクリアしてから本番公開へ

### 審査期間の目安
- Apple: 数時間〜2日（初回は長め）
- Google: 数日〜1週間（新規アカウントは特に長い）

---

## 6. 公開後の更新フロー

```powershell
# JS/画像だけの修正 → 審査不要で即配信（OTA）
eas update --branch production --message "バグ修正"

# ネイティブ設定・ライブラリ追加を伴う変更 → 再ビルド＆再審査
# app.json の version / buildNumber / versionCode を上げてから
eas build --platform all --profile production
eas submit --platform all --latest
```

> **OTAアップデート（`eas update`）は強力です。**軽微な修正を審査待ちなしで直せます。
> ただし「アプリの主要機能を後から差し替える」用途はストア規約違反になり得るので、バグ修正・文言修正の範囲で使ってください。
