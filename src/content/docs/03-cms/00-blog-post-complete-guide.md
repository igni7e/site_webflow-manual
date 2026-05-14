---
title: ブログ記事を新規投稿する完全ガイド
description: Webflow CMSでブログやお知らせを作成し、本文、画像、カテゴリー、公開設定まで入力する流れをまとめます。
sidebar:
  order: 0
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に `src/assets/captures/manual/c-01-cms-collections-entry.png` を入れてください。
撮影対象: C-01「Collections / CMS入口」。左メニューやCollectionsタブが分かる

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::tip[下書きで確認]
CMS記事は、いきなり公開せず下書き状態でタイトル、本文、画像、リンク、公開日を確認します。特に一覧ページと詳細ページの両方で見え方を確認すると安心です。
:::
<!-- body-callout:end -->


# ブログ記事を新規投稿する完全ガイド

ブログ、お知らせ、導入事例など、同じ形式の記事を追加していく機能は <strong>CMS</strong> で管理します。CMSは「Content Management System」の略で、記事のタイトル、本文、画像、カテゴリー、公開日などを入力して管理する仕組みです。

![WebflowでBooostサイトを開いた画面](../../../assets/captures/webflow-booost-designer.png)
*実画面例: CMSで更新した記事は、公開後に実際のページや一覧で表示を確認します。*

## 作業全体の流れ

1. Collectionsを開きます。
2. 対象のCollectionを選びます。
3. New ItemまたはNew Blogなどの新規作成ボタンを押します。
4. タイトルとSlugを入力します。
5. サムネイル画像、カテゴリー、概要、公開日を設定します。
6. 本文を入力し、見出し・画像・リンクを整えます。
7. 下書き保存、予約公開、即時公開のいずれかを選びます。
8. 公開後に実際のページを確認します。

## 画像差し込み枠

CMS更新は入力項目が多いため、画面キャプチャーがあるほど操作ミスを減らせます。後でBOOSTのWebflow画面を使って、以下の位置に画像を差し込んでください。実際の顧客名、問い合わせ内容、非公開URL、個人情報は写さないでください。

| No. | 対象ページ | 撮影する画面 | 強調する箇所 |
| --- | --- | --- | --- |
| C-01 | CMS完全ガイド | Dashboardまたは編集画面からCMSに入る前の状態 | CollectionsまたはCMS入口 |
| C-02 | CMS完全ガイド | Collections一覧が表示された状態 | Blog、News、お知らせなど対象Collection |
| C-03 | CMS完全ガイド | 対象Collectionを選択した直後 | 既存記事一覧、検索欄 |
| C-04 | CMS完全ガイド | New Itemを押す直前 | New Item、New Blogなど新規作成ボタン |
| C-05 | CMS完全ガイド | 新規記事フォームが開いた状態 | 入力欄全体、保存ボタン |
| C-06 | CMS完全ガイド | NameまたはTitleを入力している状態 | タイトル欄、必須項目 |
| C-07 | CMS完全ガイド | Slug欄を入力している状態 | 半角英数字、ハイフン、URL末尾 |
| C-08 | CMS完全ガイド | サムネイル画像欄が見えている状態 | Thumbnail Image、Uploadボタン |
| C-09 | CMS完全ガイド | カテゴリー選択欄が開いている状態 | Category、選択中のカテゴリー |
| C-10 | CMS完全ガイド | SummaryまたはDescription欄を入力している状態 | 一覧ページに出る説明文 |
| C-11 | CMS完全ガイド | Rich Text本文欄が見えている状態 | Body、Rich Text、本文入力エリア |
| C-12 | CMS完全ガイド | Google Docsなどから本文を貼り付けた直後 | 改行、余計な装飾がないか |
| C-13 | CMS完全ガイド | 本文中の見出しを設定している状態 | Heading 2、Heading 3 |
| C-14 | CMS完全ガイド | 本文中の太字・斜体メニュー | Bold、Italic、選択範囲 |
| C-15 | CMS完全ガイド | 箇条書きメニューを開いた状態 | Bullet list、Numbered list |
| C-16 | CMS完全ガイド | 本文中に画像を挿入する直前 | `+` ボタン、Image |
| C-17 | CMS完全ガイド | 画像アップロード画面 | Choose Image、Upload |
| C-18 | CMS完全ガイド | 挿入後の本文画像 | 画像の位置、余白、見切れ |
| C-19 | CMS完全ガイド | 画像サイズ変更メニュー | Small、Medium、Full widthなど |
| C-20 | CMS完全ガイド | YouTube埋め込みURLを入力している状態 | Embed、YouTube URL |
| C-21 | CMS完全ガイド | 本文リンク設定画面 | リンクURL、Open in new tab |
| C-22 | CMS完全ガイド | 公開日フィールドを入力している状態 | Published On、Date |
| C-23 | CMS完全ガイド | Save as Draftを押す直前 | Save as Draft、下書き状態 |
| C-24 | CMS完全ガイド | Publishを押す直前 | Publish、公開確認 |
| C-25 | CMS完全ガイド | Schedule公開を設定している状態 | 日時指定、Schedule |
| C-26 | CMS完全ガイド | 下書き記事一覧 | Draft表示、対象記事 |
| C-27 | CMS完全ガイド | 公開済み記事を再編集している状態 | Published、編集対象項目 |
| C-28 | CMS完全ガイド | ArchiveまたはUnpublish操作の確認画面 | Archive、Unpublish、Cancel |
| C-29 | CMS完全ガイド | 公開後の記事ページ | タイトル、本文、画像、リンク |
| C-30 | CMS完全ガイド | 一覧ページで記事が表示された状態 | サムネイル、タイトル、公開日 |

## 投稿前に用意するもの

- 記事タイトル
- 記事本文の原稿
- アイキャッチ画像またはサムネイル画像
- カテゴリー
- 記事概要またはDescription
- 公開日
- 本文中で使う画像、動画URL、リンク先URL

## 新規記事を作成する

まずEditorまたはDesigner内のCollectionsを開き、ブログ・お知らせなどの対象Collectionを選びます。表示名はサイトによって `Blog Posts`、`News`、`お知らせ` など異なります。

詳しい手順は [No.17 CMSの場所](/03-cms/01-where-is-cms/) と [No.18 新しい記事を追加する方法](/03-cms/02-create-new-post/) を確認してください。

## 基本情報を入力する

<strong>Name</strong> または <strong>Title</strong> には記事の正式タイトルを入れます。<strong>Slug</strong> はURLの末尾に使われる文字列です。日本語ではなく、半角英数字とハイフンで、内容が分かる短い文字列にします。

例:

- `summer-campaign-2026`
- `how-to-use-webflow-editor`
- `new-service-announcement`

公開後にSlugを変更するとURLが変わるため、公開前に必ず確認してください。

## 本文を作成する

本文は、直接入力するよりもGoogle Docsなどで下書きしてから貼り付けると安全です。貼り付け後は、見出し、太字、箇条書き、画像、リンクを整えます。

| 操作 | 詳細ページ |
| --- | --- |
| 本文を書く | [No.22 本文を書き込む](/03-cms/06-write-body/) |
| 太字・斜体 | [No.23 太字・斜体にする](/03-cms/07-bold-italic-body/) |
| 見出し | [No.24 見出しを付ける](/03-cms/08-headings/) |
| 箇条書き | [No.25 箇条書きにする](/03-cms/09-bullet-list/) |
| 画像挿入 | [No.26 本文に画像を入れる](/03-cms/10-insert-image/) |
| YouTube埋め込み | [No.28 YouTube動画を埋め込む](/03-cms/12-embed-youtube/) |
| 本文リンク | [No.29 本文にリンクを貼る](/03-cms/13-body-link/) |

## メタ情報を設定する

記事の表示やSEOに関わる項目です。サイトによって項目名は異なりますが、以下は公開前に必ず確認してください。

- サムネイル画像またはアイキャッチ画像
- カテゴリー
- Post summaryまたはDescription
- 公開日
- 画像のaltテキスト
- 関連記事や一覧ページでの表示

公開前の抜け漏れ確認には [CMS記事の公開前チェックリスト](/03-cms/25-cms-before-publish-checklist/) を使ってください。

## 公開方法を選ぶ

すぐに公開する場合はPublish、後で公開する場合はSchedule、まだ完成していない場合はSave as Draftを使います。誤って公開しないよう、公開ボタンを押す前に内容を再確認してください。

| 公開方法 | 詳細ページ |
| --- | --- |
| 公開日を設定する | [No.30 公開日を設定する](/03-cms/14-publish-date/) |
| 予約公開する | [No.31 公開を予約する](/03-cms/15-schedule-publish/) |
| 下書き保存する | [No.32 下書きで保存する](/03-cms/16-save-as-draft/) |
| 下書きを公開する | [No.33 下書きを公開する](/03-cms/17-publish-draft/) |

## 公開後チェック

- 記事ページが表示される
- 一覧ページにも表示される
- タイトルと画像が正しい
- リンクが切れていない
- スマートフォンで読みやすい
- SNSで共有する場合、タイトル・説明文・画像が意図通りになっている

表示されない場合は [トラブル時にまず確認するチェックリスト](/06-troubleshooting/00-common-checklist/) を確認してください。

## 理解度チェック

1. Slugの説明として正しいものはどれですか？
   - A. 記事URLの末尾に使われる文字列
   - B. 記事本文の文字数
   - C. 画像のファイルサイズ

<details>
<summary>答えを見る</summary>

正解: A

Slugは記事URLに使われます。公開後に変更するとURLが変わるため、公開前に確認します。

</details>

2. 記事がまだ完成していない場合に選ぶべき状態はどれですか？
   - A. Publish
   - B. Save as Draft
   - C. Delete

<details>
<summary>答えを見る</summary>

正解: B

未完成の記事は下書きとして保存します。Publishは一般公開する操作、Deleteは削除です。

</details>

3. CMS記事の公開前に確認するものとして正しい組み合わせはどれですか？
   - A. タイトル、Slug、本文、画像、リンク、スマートフォン表示
   - B. タイトルだけ
   - C. 公開日だけ

<details>
<summary>答えを見る</summary>

正解: A

記事は一覧ページ、詳細ページ、SNS共有にも影響するため、複数の項目をまとめて確認します。

</details>

## 次に進む

実際の操作に入る場合は [No.17 CMSの場所](/03-cms/01-where-is-cms/) から進んでください。
