# Lv.0 環境構築（Windows）— インストールするもの一覧

所要時間の目安：**2〜4時間**。ここを丁寧にやると以降が全部ラクになります。
インストールは上から順番に。1つ終わるごとに「確認コマンド」を実行して、表示が出ることを確かめてください。

---

## A. 今すぐ入れるもの（Lv.0〜Lv.2で必要）

### 1. Git for Windows
- URL: https://git-scm.com/download/win
- インストール中の選択肢は **すべてデフォルトのままEnterでOK**。
- 確認: `git --version` → `git version 2.x.x`

インストール後、1度だけ名前とメールを設定します（コミットの署名になります）：
```powershell
git config --global user.name "あなたの名前"
git config --global user.email "masa06111015@gmail.com"
git config --global core.autocrlf true
```

### 2. Node.js（LTS版）
- URL: https://nodejs.org/ → **LTS** と書かれた方をダウンロード
- 確認: `node -v` （v20 以上ならOK） / `npm -v`

> 将来バージョンを切り替えたくなったら `fnm`（https://github.com/Schniz/fnm ）を導入。**今は不要です。**

### 3. Visual Studio Code（コードエディタ）
- URL: https://code.visualstudio.com/
- インストール時、**「エクスプローラーのコンテキストメニューに追加」に全部チェック**を入れると便利。

入れる拡張機能（VS Code左の四角いアイコン → 検索してInstall）：

| 拡張機能名 | 用途 |
|---|---|
| **Expo Tools** | Expo設定ファイルの補完 |
| **ESLint** | 書き間違いをその場で指摘 |
| **Prettier - Code formatter** | 保存時に自動で整形 |
| **Japanese Language Pack** | VS Codeの日本語化 |
| **Error Lens** | エラーを行内に赤字表示（初心者に効果大） |
| **GitLens** | 変更履歴の可視化 |

Prettierの自動整形を有効化：`Ctrl + ,` → 検索欄に `format on save` → チェックを入れる。

### 4. Windows Terminal
- Microsoft Store で「Windows Terminal」を検索してインストール（Windows 11 は標準搭載）。
- 以降のコマンドはここで実行します。

### 5. スマホに Expo Go アプリ（★これが実機確認の要）
- iPhone: App Store で **「Expo Go」**
- Android: Google Play で **「Expo Go」**
- PCとスマホを **同じWi-Fi** に接続しておくこと。

### 6. Expo アカウント（無料）
- https://expo.dev/signup で登録。後の EAS Build で必須になります。

### 7. EAS CLI（ビルド・提出のコマンド）
```powershell
npm install -g eas-cli
eas --version
eas login
```

---

## B. Windows特有の事前設定（トラブル予防・必ずやる）

1. **プロジェクトは OneDrive 配下に置かない**
   `C:\Users\<名前>\OneDrive\...` は同期で壊れます。**`C:\dev\` を作ってそこで作業**してください。
   ```powershell
   mkdir C:\dev
   cd C:\dev
   git clone https://github.com/masaGenAI/Apps-UC.git
   cd Apps-UC
   ```

2. **長いパスを許可する**（`node_modules` はパスが非常に長くなります）
   PowerShellを**管理者として実行**し、以下を1行実行：
   ```powershell
   Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -Value 1
   git config --system core.longpaths true
   ```

3. **ウイルス対策ソフトの除外に `C:\dev` を追加**（`npm install` が極端に遅くなるのを防ぐ）

4. **ファイアウォールの確認**：`npx expo start` 初回に「Node.js のアクセスを許可しますか」と出たら **プライベートネットワークを許可**。ここを拒否するとスマホから繋がりません。

---

## C. 動作確認：1本目のアプリを起動する

```powershell
cd C:\dev\Apps-UC
mkdir apps
cd apps
npx create-expo-app@latest 001-counter --template blank-typescript
cd 001-counter
npx expo start
```

ターミナルにQRコードが出ます。
- **Android**: Expo Go アプリでQRをスキャン
- **iPhone**: 標準のカメラアプリでQRをスキャン → Expo Go が開く

スマホに画面が出たら **環境構築は成功**です。`App.tsx` の文字を書き換えて保存すると、スマホに即反映されます（ホットリロード）。

---

## D. Lv.3 以降で入れるもの（今は不要・3〜4か月後）

### Android Studio（Androidエミュレータ / ネイティブビルド用）
- URL: https://developer.android.com/studio
- インストーラで **Android SDK / SDK Platform-Tools / Android Virtual Device** にチェック。
- 併せて **JDK 17**（Android Studio に同梱されるものでOK）。
- 環境変数 `ANDROID_HOME` を `C:\Users\<名前>\AppData\Local\Android\Sdk` に設定。
- 確認: `adb --version`

> Expo Go で開発する間は**不要**です。実機があるなら当面エミュレータも要りません（実機の方が速い）。

### 各種アカウント（必要になった時点で）

| サービス | 費用 | いつ必要か |
|---|---|---|
| GitHub | 無料 | 今すぐ（このリポジトリ用） |
| Expo (EAS) | 無料枠あり / 有料プランあり | Lv.3 初公開時。無料枠はビルド回数と待ち時間に上限があるため、最新の料金は https://expo.dev/pricing で確認 |
| **Google Play Console** | **$25（初回のみ）** | Lv.3。登録後に本人確認と、個人アカウントはクローズドテスト要件あり |
| **Apple Developer Program** | **約$99 / 年** | Lv.3。Apple ID に2ファクタ認証の設定が必須 |
| Supabase | 無料枠あり | Lv.4 |
| RevenueCat | 一定売上まで無料 | Lv.4 |
| Google AdMob | 無料 | Lv.4 |

> **Apple/Googleの登録は審査・本人確認に数日〜2週間かかることがあります。** Lv.3に入る1か月前には申し込んでおくのが安全です。

---

## E. よく出るエラーと対処

| 症状 | 原因 / 対処 |
|---|---|
| スマホからQRを読んでも繋がらない | PCとスマホが別のWi-Fi / ファイアウォール拒否。`npx expo start --tunnel` を試す |
| `npm install` が終わらない | OneDrive配下 or ウイルス対策。`C:\dev` へ移動し除外設定 |
| `'expo' は認識されていません` | `npx expo` と `npx` を付けて実行する |
| 変更がスマホに反映されない | ターミナルで `r` キー（リロード）。それでも駄目ならExpo Goを再起動 |
| 赤い画面いっぱいのエラー | **落ち着いてエラー1行目を読む。** 大体ファイル名と行番号が書いてある |
