---
title: Webflow manual image check implementation plan
description: webflow指示書.md に基づく画像追加・変更・整理の実施計画
created: 2026-06-02
---

# Webflow manual image check implementation plan

## 目的

`/Users/das/Downloads/webflowマニュアルの画像チェック/webflow指示書.md` の指示に基づき、manual.booos7.com 用マニュアル本文へ画像追加・差し替え・冗長テキスト整理を反映する。

## 方針

- Downloads 配下の `images/image1.png`〜`image20.png` は、指示対象セクションを示す参照画像として扱う。
- 対象ページの既存本文に合わせ、実キャプチャが未撮影の箇所はStarlightの `:::note[キャプチャー指示]` または `:::note[キャプチャー差し込み位置]` で示す。
- 指示書付属画像はWebflow操作画面の実キャプチャではないため、本文画像としては採用しない。
- 指示書で「追加 or 削除」とあるページは、画像追加を優先し、冗長な注記がある場合のみ削る。
- `05-settings/06-form-csv-download` はページ内容と一致する `Forms > Submissions > Export all` 画像として採用する。メールアドレス変更画面への差し替えは別ページ指示の混入と判断する。
- `05-settings/08-invite-collaborator` は提供画像を重複解消用の別画角として採用し、既存の同種画像が連続している場合に差し替える。

## 対象

- `src/content/docs/work/02-update-post.md`
- `src/content/docs/02-editor/02-open-content-editor.md`
- `src/content/docs/02-editor/10-external-link-new-tab.md`
- `src/content/docs/02-editor/11-anchor-link.md`
- `src/content/docs/02-editor/14-official-content-editor-image-reference.md`
- `src/content/docs/03-cms/05-post-category.md`
- `src/content/docs/03-cms/11-resize-image.md`
- `src/content/docs/03-cms/22-image-alt.md`
- `src/content/docs/04-designer/05-asset-panel.md`
- `src/content/docs/04-designer/10-favicon.md`
- `src/content/docs/04-designer/11-duplicate-page.md`
- `src/content/docs/05-settings/03-ogp-image.md`
- `src/content/docs/05-settings/06-form-csv-download.md`
- `src/content/docs/05-settings/08-invite-collaborator.md`
- `src/content/docs/05-settings/10-search-engine-control.md`
- `src/content/docs/06-troubleshooting/00-common-checklist.md`

## 進捗

- [x] 指示書と対象画像の確認
- [x] 実施方針の決定
- [x] 指示書画像が参照画像であることを再確認
- [x] 対象 Markdown の差し込み位置・撮影指示を整理
- [x] ビルド確認
- [x] 差分確認

## 検証結果

- `npm run build` 成功。
- 既存の Starlight duplicate id 警告は継続して出るが、今回追加した画像パス・Markdown構文によるビルド失敗はなし。
- 対象ページ内の作業用文言 `新規追加（標準スコープ補完）` と `実画面例:` は削除・本文化済み。
- 指示書付属画像を実キャプチャとして差し込んだ箇所は取り下げ、撮影指示コールアウトへ修正済み。
