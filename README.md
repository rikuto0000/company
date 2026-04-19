# iPhoneからVS Code + GitHub Copilotを使う

このフォルダは、GitHub Codespacesを使ってiPhoneからVS Code風の編集環境とGitHub Copilotを使いやすくするための最小構成です。

## 一番現実的な構成

一番手堅い方法は、ローカルのWindowsをiPhoneに直接載せるのではなく、GitHub CodespacesをiPhoneのブラウザで開く構成です。

この方法なら以下が使えます。

- VS Code系のWebエディタ
- ターミナル
- GitHubリポジトリ連携
- GitHub Copilot補完
- GitHub Copilot Chat

## 事前に必要なもの

- GitHubアカウント
- GitHub Copilotが使える契約または権限
- GitHub Codespacesが使えるアカウント
- このフォルダをGitHubリポジトリに置くこと

## 使い始める手順

1. このフォルダをGitHubへpushします。
2. iPhoneで対象のGitHubリポジトリを開きます。
3. `Code` -> `Codespaces` -> `Create codespace on main` を選びます。
4. ブラウザでCodespaceを開きます。
5. GitHub Copilotのサインインや有効化を求められたら許可します。
6. READMEが開いた状態で開始できます。

## GitHubへ上げる最短手順

まだGitHubリポジトリがない場合は、先にGitHub上で空のリポジトリを1つ作ります。

ローカルでは以下の流れです。

```powershell
git init
git add .
git remote add origin <あなたのGitHubリポジトリURL>
git branch -M main
git commit -m "Add Codespaces setup for iPhone"
git push -u origin main
```

`<あなたのGitHubリポジトリURL>` は、たとえば `https://github.com/yourname/IOS2PC.git` です。

push が終わったら、iPhone のブラウザからそのリポジトリを開いて Codespaces を作成できます。

## このリポジトリに入っている設定

- `.devcontainer/devcontainer.json`
  - Codespaces起動時にREADMEを開きます。
  - GitHub Copilot拡張とGitHub Copilot Chat拡張を追加します。
- `.vscode/extensions.json`
  - ローカルVS Codeで開いたときもCopilot拡張を推奨します。

## iPhoneで使う時の注意点

- iPhone単体でも使えますが、長時間の作業は外付けキーボード前提の方が現実的です。
- Safariでも使えますが、ショートカットや画面サイズの都合で操作性はPCより落ちます。
- ファイル編集、軽いターミナル操作、Copilotへの相談は十分可能です。
- 複雑なマルチウィンドウ作業やローカルデバイス接続は不向きです。

## Claude Codeに近い使い方をしたい場合

ブラウザ版Codespaces + Copilot Chatが最も近いです。

ただし、完全に同じ操作感にはなりません。iPhoneでは画面サイズとキーボード操作が制約になるためです。

## 本当にPCそのものをiPhoneから使いたい場合

VS Codeを入れたWindowsマシンを遠隔操作する方法の方が機能は完全です。

候補は以下です。

- Chrome Remote Desktop
- Microsoft Remote Desktop
- Tailscale経由のリモート接続

この方法なら、Windows上のVS CodeとGitHub Copilotをそのまま操作できます。

向いているケース:

- ローカルのファイルを直接触りたい
- Windowsアプリも一緒に使いたい
- 拡張機能や端末操作を完全にPC同等で使いたい

## おすすめの結論

まずはGitHub Codespacesで始めるのが最短です。

もし目的が「自宅PCのVS Code環境をそのままiPhoneで使う」なら、Codespacesではなくリモートデスクトップ構成に切り替えた方が合っています。