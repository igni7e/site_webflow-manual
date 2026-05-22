---
title: "B-13. 最新Content Editor画面の見方"
description: "Webflow最新版Content editor roleで開いたcanvas画面の見方、編集アイコン、CMS、Assets、Publish、できない操作を整理します。"
sidebar:
  order: 13
  label: "B-13. 最新Content Editor画面の見方"
---

# B-13. 最新Content Editor画面の見方

## こんなときに使います

Webflowを最新版のContent editor roleで開いた後、画面のどこを見ればよいか、どのアイコンを押せばよいか分からない時に使います。

最新版のContent Editorは、旧Legacy Editorとは違い、Webflowのcanvas上で文章、画像、リンク、CMS記事、Assets、ページ設定の一部を扱えます。ただし、デザインや構造を作り替える画面ではありません。

:::note[公式画像またはキャプチャー指示]
撮影する画面: Webflow公式Help CenterのContent editor role説明画像、またはMorbidoサイトを最新版Content editor roleで開いたcanvas画面。
保存ファイル名: `b-09-latest-content-editor-screen-guide.png`
撮影直前の状態: Webflow canvasが読み込み完了し、編集できるテキストや画像にカーソルを合わせられる状態。
必ず写すもの: canvas、上部バー、Pages/CMS/Assetsなどの入口、編集可能な要素の青いアウトラインまたは編集アイコン。
写さないもの: 未公開ページ、個人情報、通知、他社サイト情報。
:::

![Webflow公式: content editingの紹介画像](https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/680fb9c7decb8c21fd926774_og-edit-mode.jpg)

:::tip[公式画像を追加する場合]
Content Editorの画面説明を増やす場合は、[B-14. 公式画像で見るContent Editor操作](/02-editor/14-official-content-editor-image-reference/) の差し込み位置リストを使ってください。公式画像で一般的なUIを説明し、Morbido固有の画面は別途キャプチャーで補う構成にします。
:::

## 最新Content Editorでできること

| できること | 例 | 確認ページ |
| --- | --- | --- |
| テキストを編集する | 見出し、本文、ボタン周辺の短い文言 | [B-3. エディターでサイトの文字を書き換える方法](/02-editor/03-edit-text/) |
| 画像を差し替える | ページ上の写真、バナー、アイキャッチ画像 | [B-6. エディターで画像を差し替える方法](/02-editor/06-replace-image/) |
| リンクを編集する | ボタン、文章リンク、外部URL | [B-7. リンク先URLを変更する方法](/02-editor/07-edit-link-url/) |
| CMS記事を作成・編集する | お知らせ、ブログ、ニュース | [C-1. ブログ記事を新規投稿する完全ガイド](/03-cms/00-blog-post-complete-guide/) |
| Assetsを管理する | 画像やファイルをアップロードする | [D-6. Asset Panelの使い方](/04-designer/05-asset-panel/) |
| SEO設定の一部を見る | SEO title、meta description、OGP | [F-2. SEO titleを変更する方法](/05-settings/01-seo-title/) |

:::tip[通常更新の入口]
日常的な更新は、まず最新版Content editor roleで開くことをお勧めします。Designerはレイアウトや構造を触れるため、必要な時だけ開きます。
:::

## 画面で見るポイント

### 1. Canvas

画面中央のサイト表示部分です。公開サイトに近い見た目で、文章や画像を確認しながら編集します。

編集できる要素にカーソルを合わせると、青いアウトラインや編集アイコンが表示されます。表示されない場合は、その要素が編集対象外になっているか、権限が足りない可能性があります。

### 2. 編集アイコン

編集可能な要素を選ぶと、内容に応じたアイコンが表示されます。

| アイコンの種類 | 使う場面 |
| --- | --- |
| Pencil | 文章を編集する |
| Link | リンク先URLを編集する |
| Image / Landscape | 画像やAssetを差し替える |
| Gear | 画像設定など、要素ごとの設定を確認する |

:::note[編集アイコンが出ない場合]
編集アイコンが表示されない時は、ログインしているメールアドレス、Site role、対象ページ、編集権限、編集不可に設定された要素ではないかを確認してください。
:::

### 3. Pages / CMS / Assets

最新版Content Editorでは、ページ、CMS、Assetsなどにアクセスできる場合があります。見える項目は権限やサイト設定によって変わります。

| 入口 | 使う場面 |
| --- | --- |
| Pages | 編集したいページへ移動する |
| CMS | お知らせ、ブログ、ニュースなどの記事を管理する |
| Assets | 画像やファイルを管理する |
| Settings | ページ設定、SEO、OGPなどを確認する |

### 4. Publish

Publish権限がある場合、変更を公開できます。Publishする前に、公開先ドメイン、変更したページ、スマートフォン表示、リンク先を確認します。

公開前の確認には [B-12. Editor公開前チェックリスト](/02-editor/12-before-publish-checklist/) を使ってください。

## `?update` で開く方法

公開サイトを見ている時に、そのページを直接Webflowのcanvasで開きたい場合は、URL末尾に `?update` を付けます。

例:

`https://example.com/service/?update`

ログイン済みで権限がある場合は、そのページのContent Editor画面が開きます。ログインしていない場合は、先にWebflowのログイン画面が表示されます。

:::tip[開かない場合]
`?update` で開けない場合は、ログイン状態、権限、対象サイトのPublish状態を確認してください。Webflow公式では、ショートカットが動かない場合はサイトの再Publishが必要になる場合があると案内されています。
:::

## CMS記事をcanvas上で見る場合

CMS記事は、CMSパネルから編集する方法と、CMSテンプレートページをcanvasで見ながら編集する方法があります。

canvas上でCMS記事を扱う場合は、次を確認します。

1. PagesからCMSテンプレートページを開きます。
2. 上部のページ切り替えやCMS itemの切り替えを確認します。
3. 対象の記事を選びます。
4. 編集できる本文や画像にカーソルを合わせます。
5. 必要な箇所だけ編集します。
6. CMS statusやPublish状態を確認します。

:::caution[共通部分の編集]
CMS一覧やテンプレート上の「共通部分」を編集すると、複数の記事や一覧に影響する場合があります。記事本文だけを直したい時は、対象Fieldに紐づいた内容か確認してから編集することをお勧めします。
:::

## Interactive elementを編集する場合

タブ、ドロップダウン、スライダー、ナビゲーションなどは、最初は中身が見えていない場合があります。

この場合は、要素を選び、表示メニューからTab 2、Slide 1、Show menuなどを選んで、編集したい中身を表示してから操作します。

:::caution[表示されていない中身]
隠れているメニューやタブ内の文章は見落としやすいです。公開前に、タブ、ドロップダウン、スライダーを実際に切り替えて確認してください。
:::

## 自分で触らない方がよい操作

最新版Content Editorでも、次の操作は通常更新の範囲を超えます。

| 操作 | 理由 |
| --- | --- |
| レイアウト、余白、フォントサイズを変える | デザイン変更にあたります |
| ページ名、フォルダ、ページSlugを変更する | URLやサイト構造に影響します |
| CMSのCollection自体を作る・設定する | サイト構造に影響します |
| Custom codeを触る | 計測タグや外部連携に影響します |
| Componentの構造を変える | 複数ページに影響する可能性があります |

:::caution[迷ったら止める]
画面にDesigner、Custom code、CMS settings、Billing、Domain、Deleteなどが出てきた場合は、作業を止めて制作担当者に確認することをお勧めします。
:::

## 公式情報

このページは、2026年5月時点のWebflow公式Help Centerを確認して作成しています。

- [Edit site content as a content editor](https://help.webflow.com/hc/en-us/articles/33961251014931-Edit-site-content-as-a-content-editor)
- [What’s the difference between the legacy Editor and content editing in Webflow?](https://help.webflow.com/hc/en-us/articles/39773828407827-What-s-the-difference-between-the-legacy-Editor-and-content-editing-in-Webflow)
- [Shortcut to edit your live site](https://help.webflow.com/hc/en-us/articles/48214769154579-Shortcut-to-edit-your-live-site)

## 次に進む

実際に最新版Content Editorを開く手順は [B-2. Content Editor（最新版）でWebflowを開く方法](/02-editor/02-open-content-editor/) を確認してください。文字の修正に進む場合は [B-3. エディターでサイトの文字を書き換える方法](/02-editor/03-edit-text/) に進んでください。
