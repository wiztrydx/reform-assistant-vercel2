# リフォーム提案アシスタント - Vercel版

Vercelに最適化されたリフォーム提案アシスタントです。

## 🚀 Vercelでのデプロイ手順

### 1. GitHubリポジトリの作成

```bash
git init
git add .
git commit -m "Initial commit for Vercel"
git remote add origin https://github.com/yourusername/reform-assistant-vercel.git
git push -u origin main
```

### 2. Vercelでのプロジェクト作成

1. [Vercel](https://vercel.com)にログイン
2. 「New Project」をクリック
3. GitHubリポジトリを選択
4. 「Import」をクリック

### 3. 環境変数の設定

Vercelダッシュボードで以下の環境変数を設定:

- **Name**: `ANTHROPIC_API_KEY`
- **Value**: `sk-ant-your-api-key-here`

### 4. デプロイ設定

Vercelが自動的に `vercel.json` を読み込んで適切にデプロイします。

## 📁 プロジェクト構成

```
reform-assistant-vercel/
├── vercel.json              # Vercel設定
├── requirements.txt         # Python依存関係
├── api/
│   └── index.py            # サーバーレス関数
└── public/
    ├── index.html          # フロントエンド
    └── assets/             # CSS/JS
```

## ⚙️ 設定の説明

### vercel.json

- **builds**: PythonとStaticファイルのビルド設定
- **routes**: URLルーティング設定
- **env**: 環境変数の設定

### api/index.py

- Flask アプリケーションをサーバーレス関数として実行
- `/api/chat` と `/api/initial-message` エンドポイントを提供

## 🔧 カスタマイズ

### APIの変更

`api/index.py` を編集してAPIロジックを変更できます。

### フロントエンドの変更

`public/` ディレクトリ内のファイルを編集してUIを変更できます。

## 🚨 トラブルシューティング

### 404エラーが発生する場合

1. `vercel.json` の設定を確認
2. ファイル構成が正しいか確認
3. 環境変数が設定されているか確認

### APIが動作しない場合

1. `ANTHROPIC_API_KEY` が正しく設定されているか確認
2. Vercelの関数ログを確認
3. Python依存関係が正しくインストールされているか確認

### ビルドエラーが発生する場合

1. `requirements.txt` の内容を確認
2. Python バージョンの互換性を確認

## 💰 料金

- **Hobby Plan**: 無料（月100GB転送、100GBストレージ）
- **Pro Plan**: 月20ドル（1TB転送、無制限ストレージ）

## 🔗 参考リンク

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Anthropic API Documentation](https://docs.anthropic.com/)

