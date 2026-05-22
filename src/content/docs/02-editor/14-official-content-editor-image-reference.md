---
title: "B-14. 公式画像で見るContent Editor操作"
description: "Webflow公式画像と公式Help Centerを使って、最新版Content Editorで確認したい画面の差し込み位置を整理します。"
sidebar:
  order: 14
  label: "B-14. 公式画像で見るContent Editor操作"
---

# B-14. 公式画像で見るContent Editor操作

このページは、Webflow公式サイトや公式Help Centerの画像をマニュアル内に追加するための整理ページです。公式画像を使う場合も、Morbido固有のサイト名、未公開ページ、個人情報が写る画面は避けてください。

![Webflow公式: content editingの紹介画像](https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/680fb9c7decb8c21fd926774_og-edit-mode.jpg)

:::note[公式画像の扱い]
上の画像はWebflow公式サイトの `Create and edit website content with edit mode` で公開されているOG画像です。本文内で公式画像を使う場合は、古いLegacy Editorではなく、最新版のContent editor roleを説明している画像を優先してください。
:::

## 公式画像を入れる場所

| ID | 画像で見せたい内容 | 差し込み先 | 公式情報 |
| --- | --- | --- | --- |
| B-12 | Content editor roleで開いたcanvas全体 | [B-2. Content Editor（最新版）でWebflowを開く方法](/02-editor/02-open-content-editor/) | [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor) |
| B-13 | Pages / CMS / Assets / Settingsの入口 | [B-13. 最新Content Editor画面の見方](/02-editor/13-latest-content-editor-screen-guide/) | [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor) |
| B-14 | 文字編集時のアウトラインまたはPencilアイコン | [B-3. エディターでサイトの文字を書き換える方法](/02-editor/03-edit-text/) | [Edit site content in Webflow](https://webflow.com/feature/edit-content) |
| B-15 | 画像差し替えの入口 | [B-6. エディターで画像を差し替える方法](/02-editor/06-replace-image/) | [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor) |
| B-16 | リンク設定またはリンク編集の入口 | [B-7. リンク先URLを変更する方法](/02-editor/07-edit-link-url/) | [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor) |
| B-17 | Publish前の確認画面 | [B-12. Editor公開前チェックリスト](/02-editor/12-before-publish-checklist/) | [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor) |
| B-18 | `?update` で直接編集画面を開く導線 | [B-2. Content Editor（最新版）でWebflowを開く方法](/02-editor/02-open-content-editor/) | [Shortcut to edit your live site](https://help.webflow.com/hc/en-us/articles/48214769154579-Shortcut-to-edit-your-live-site) |
| B-19 | Legacy Editorと最新版Content Editorの違い | [B-13. 最新Content Editor画面の見方](/02-editor/13-latest-content-editor-screen-guide/) | [What's the difference between the legacy Editor and content editing in Webflow?](https://help.webflow.com/hc/en-us/articles/39773828407827-What-s-the-difference-between-the-legacy-Editor-and-edit-mode) |
| B-20 | CMS itemを作成・編集する画面 | [C-1. ブログ記事を新規投稿する完全ガイド](/03-cms/00-blog-post-complete-guide/) | [Edit site content in Webflow](https://webflow.com/feature/edit-content) |
| B-21 | SEO / Open Graphを確認する画面 | [F-2. SEO titleを変更する方法](/05-settings/01-seo-title/) | [Edit site content in Webflow](https://webflow.com/feature/edit-content) |
| B-22 | Content editor roleの権限・Publish権限 | [A-8. Editorだけで作業した方がよい理由](/01-getting-started/08-editor-only-recommendation/) | [Create and manage custom roles](https://help.webflow.com/hc/en-us/articles/46651804072467-Create-and-manage-custom-roles) |

## 差し込み時の判断基準

:::tip[公式画像を優先する場面]
Webflowの一般的なUI、Content editor roleの考え方、Pages / CMS / Assets / Publishの位置関係を説明する場合は、公式画像を使うと読者が最新版UIを理解しやすくなります。
:::

:::caution[Morbido画面を優先する場面]
対象サイト名、Morbido固有のCollection名、実際に押すサイトカード、実際の投稿Fieldなどを説明する場合は、公式画像ではなくMorbido画面のキャプチャーを使ってください。個人情報、未公開記事、問い合わせ本文、請求情報は必ず隠します。
:::

## 公式画像差し込み位置

### Content editor roleのcanvas全体

:::note[公式画像差し込み位置]
使う画像: Webflow公式Help Center `Edit site content as a content editor` のContent editor role画面、またはWebflow公式サイト `Edit content` ページのcontent editing紹介画像。
保存ファイル名: `b-12-official-content-editor-canvas.png`
差し込み先: `02-editor/02-open-content-editor.md`、`02-editor/13-latest-content-editor-screen-guide.md`
必ず見せるもの: canvas、編集対象のページ、Content editor roleであることが分かるUI。
避けるもの: Legacy Editorの下部バーだけが写る古い画面、個人情報、未公開ページ。
:::

### Pages / CMS / Assets / Settingsの入口

:::note[公式画像差し込み位置]
使う画像: Webflow公式Help Center `Edit site content as a content editor` で、Pages panel、CMS panel、Assets panel、Settings panelの入口が分かる画像。
保存ファイル名: `b-13-official-content-editor-panels.png`
差し込み先: `02-editor/13-latest-content-editor-screen-guide.md`
必ず見せるもの: Pages、CMS、Assets、Settingsなどの入口と、画面全体の位置関係。
避けるもの: 入口だけを極端に拡大した画像、ロード中のUI、通知。
:::

### 文字編集

:::note[公式画像差し込み位置]
使う画像: Webflow公式のcontent editing紹介画像、またはHelp Center内でテキスト編集のアウトラインや編集アイコンが分かる画像。
保存ファイル名: `b-14-official-text-editing.png`
差し込み先: `02-editor/03-edit-text.md`
必ず見せるもの: 編集対象テキスト、青いアウトライン、Pencilなどの編集アイコン。
避けるもの: デザイン編集パネル中心の画面、意図が分からない拡大画像。
:::

### 画像差し替え

:::note[公式画像差し込み位置]
使う画像: Webflow公式Help Center内で、画像またはAssetの編集・差し替え入口が分かる画像。
保存ファイル名: `b-15-official-image-replace.png`
差し込み先: `02-editor/06-replace-image.md`
必ず見せるもの: 対象画像、画像編集アイコン、AssetsまたはUploadに進める入口。
避けるもの: 著作権や個人情報のある画像、未公開素材。
:::

### リンク編集

:::note[公式画像差し込み位置]
使う画像: Webflow公式Help Center内で、リンク設定またはリンク編集の入口が分かる画像。
保存ファイル名: `b-16-official-link-editing.png`
差し込み先: `02-editor/07-edit-link-url.md`、`02-editor/10-external-link-new-tab.md`
必ず見せるもの: Linkの設定入口、URL入力欄、必要であれば新しいタブ設定。
避けるもの: 実在する非公開URL、ログイン情報、外部サービスの管理画面。
:::

### Publish

:::note[公式画像差し込み位置]
使う画像: Webflow公式Help Center内で、Publishまたは公開前確認が分かる画像。
保存ファイル名: `b-17-official-publish-flow.png`
差し込み先: `02-editor/08-save-and-publish.md`、`02-editor/12-before-publish-checklist.md`
必ず見せるもの: Publishボタン、公開対象、公開前に確認する文脈。
避けるもの: 実際にPublish完了してしまった後だけの画面、公開してはいけないドメイン。
:::

## 公式情報

- [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor)
- [Create and edit website content with edit mode](https://webflow.com/feature/edit-content)
- [Shortcut to edit your live site](https://help.webflow.com/hc/en-us/articles/48214769154579-Shortcut-to-edit-your-live-site)
- [What's the difference between the legacy Editor and content editing in Webflow?](https://help.webflow.com/hc/en-us/articles/39773828407827-What-s-the-difference-between-the-legacy-Editor-and-edit-mode)
- [Create and manage custom roles](https://help.webflow.com/hc/en-us/articles/46651804072467-Create-and-manage-custom-roles)
