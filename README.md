# site_webflow-manual

クライアント向け **Webflow更新マニュアル**（IGNITE提供）。Astro Starlight で構築。

## 構成

- 公開対象: Webflow を使ってサイト運用する非エンジニアのクライアント
- カテゴリ: A. はじめの一歩 / B. エディター / C. CMS更新 / D. デザイナー / E. 便利な設定 / F. トラブル解決
- ソース: `src/content/docs/<category>/*.md`
- ホスティング想定: Cloudflare Pages（後日設定）

## 開発

```bash
npm install
npm run dev    # http://localhost:4321/
npm run build  # dist/ にビルド成果物
```

## 編集ワークフロー

- 本リポジトリ `src/content/docs/` が **正本**。Obsidian Vault `24_Webflow更新マニュアル動画/` はアーカイブ
- 新規マニュアル追加時は frontmatter に `title` / `description` / `sidebar.order` を必ず付与
- カテゴリフォルダ内のファイルは `sidebar.order` の昇順で並ぶ

## 拡充方針

| カテゴリ | 補完したトピック |
|---|---|
| B. エディター | 外部リンク新タブ / アンカーリンク |
| C. CMS | alt属性 / 並び替え / ファイル添付 |
| D. デザイナー | ファビコン / ページ複製 |
| E. 設定 | フォーム編集 / 共同編集者招待 / ドメイン確認 / sitemap・noindex |
| F. トラブル | メール不達対応 / モバイルプレビュー |

## ライセンス

社内・クライアント配布用。Public化は要相談。
