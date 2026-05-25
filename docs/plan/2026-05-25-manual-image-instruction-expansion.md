---
title: "Webflowマニュアル 画像追加指示 強化計画 2026-05-25"
description: "Webflow更新マニュアルに、後続の撮影担当者が迷わず画像を追加できるキャプチャー指示を増やす実装TODO。"
---

# Webflowマニュアル 画像追加指示 強化計画 2026-05-25

## 方針

- 実画像ファイルは追加せず、本文内に `:::note[キャプチャー指示]` を増やす。
- 操作ステップの直後に、読者が見るべき画面とUIを指定する。
- 撮影指示は `docs/human-capture-shot-list.md` と同じ保存ファイル名にする。
- 個人情報、請求情報、メールアドレス、問い合わせ本文、他社Site名は写さない。

## TODO

- [x] 既存ページの `キャプチャー指示` を確認し、画像指示が足りない重点ページを決める
- [x] `work/` の作業前・テキスト編集ページにキャプチャー指示を追加する
- [x] `01-getting-started/` のWorkspace / planページにキャプチャー指示を追加する
- [x] `03-cms/` のCMS入口、記事作成、公開状態ページにキャプチャー指示を追加する
- [x] `05-settings/08-invite-collaborator.md` にSite access / Role / Can publishのキャプチャー指示を追加する
- [x] `06-troubleshooting/00-common-checklist.md` に原因別確認画面のキャプチャー指示を追加する
- [x] `docs/human-capture-shot-list.md` に追加撮影項目を反映する
- [x] `npm run build` で検証する
- [x] `rg -n "キャプチャー指示|キャプチャー差し込み位置" src/content/docs docs/human-capture-shot-list.md` で指示の残り方を確認する

## 重点ページ

- `src/content/docs/work/06-before-start.md`
- `src/content/docs/work/00-edit-text.md`
- `src/content/docs/01-getting-started/00-workspace-intro.md`
- `src/content/docs/01-getting-started/00-workspace-plan.md`
- `src/content/docs/03-cms/01-where-is-cms.md`
- `src/content/docs/03-cms/02-create-new-post.md`
- `src/content/docs/03-cms/16-save-as-draft.md`
- `src/content/docs/03-cms/17-publish-draft.md`
- `src/content/docs/03-cms/18-edit-published.md`
- `src/content/docs/05-settings/08-invite-collaborator.md`
- `src/content/docs/06-troubleshooting/00-common-checklist.md`
