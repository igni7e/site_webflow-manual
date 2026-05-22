---
title: Morbido Webflowマニュアル改善 2026-05-22 実装TODO
description: Morbido向けWebflow更新マニュアルのフィードバック反映計画。
---

# Morbido Webflowマニュアル改善 2026-05-22 実装TODO

## 方針

- Astro Starlight の既存構成に合わせ、編集対象は `src/content/docs/` を中心にする。
- 未撮影のWebflow画面は仮画像を置かず、本文には `:::note[キャプチャー指示]` を入れる。
- 画像撮影が必要な項目は `docs/human-capture-shot-list.md` と整合させる。
- 作業後は `npm run build` で確認し、push後に `main` へマージする。

## 実ファイルマッピング

- `/` -> `src/content/docs/index.md`
- `/01-getting-started/02-create-account/` -> `src/content/docs/01-getting-started/02-create-account.md`
- `/02-editor/00-editor-complete-guide/` -> `src/content/docs/02-editor/00-editor-complete-guide.md`
- `/02-editor/02-open-content-editor/` -> `src/content/docs/02-editor/02-open-content-editor.md`
- `/03-cms/01-where-is-cms/` -> `src/content/docs/03-cms/01-where-is-cms.md`
- `/03-cms/05-post-category/` -> `src/content/docs/03-cms/05-post-category.md`
- `/03-cms/09-bullet-list/` -> `src/content/docs/03-cms/09-bullet-list.md`
- `/03-cms/20-archive-post/` -> `src/content/docs/03-cms/20-archive-post.md`

## TODO

- [x] main を `origin/main` と同期し、作業ブランチを作る
- [x] 実ファイルマッピングを確認する
- [x] トップページを作業ベースに再構成する
- [x] A-0「Webflowの構造を知る」5ページを追加する
- [x] WORK章の作業ベースページ6本を追加する
- [x] A〜G章の sidebar 表示を通し番号に揃える
- [x] Content Editor入門ページの導入文を初心者向けに直す
- [x] FAQ/理解度チェックの `<details>` を常時表示に変える
- [x] CMS表記と画像不整合箇所を本文・キャプチャー指示で直す
- [x] `docs/human-capture-shot-list.md` に追加撮影項目を反映する
- [x] `npm run build` で検証する
- [ ] commit、push、main merge、main push を行う
