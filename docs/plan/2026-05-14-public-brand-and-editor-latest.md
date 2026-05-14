---
title: "2026-05-14 公開版ブランド表記とEditor最新化計画"
description: "公開用にIGNITE提供表記を明確化し、WebflowのContent editor role最新情報へ更新する計画"
sidebar:
  order: 4
---

# 2026-05-14 公開版ブランド表記とEditor最新化計画

- [x] Webflow公式情報でLegacy Editor、Content editor role、権限、公開仕様を確認する
- [x] 左上タイトルとトップページでIGNITE提供・公開版・責任範囲を明確にする
- [x] Editor章を2026年のContent editor role前提へ更新する
- [x] `?edit` や `/editor` など旧導線を `?update` とDashboard導線へ修正する
- [x] 招待・権限ページをContent editor / Marketer / Reviewer / Can publish前提へ更新する
- [x] 旧Editor前提の入口ページをContent editor role前提へ更新する
- [x] 細かい操作ページに残った旧エディターモード表現を更新する
- [x] ビルドとブラウザ表示で検証する

## 公式確認メモ

- Legacy Editorは2026年8月4日から利用不可予定。新規Legacy Editorユーザー追加は不可。
- 現在の推奨はContent editor roleでWebflow内のcanvas上からコンテンツ編集する形。
- Content editor roleはLimited seatまたはClient seatに割り当てられ、デザインを触らずにcopy、media、CMS contentを更新できる。
- 旧 `?edit` ではなく、Content editor role向けのクイックアクセスは `?update`。
- PublishはCan publishがオンの場合に可能。Legacy EditorからのPublishは全変更を巻き込む可能性があるため注意が必要。
