---
title: "Google検索結果に出る「ページのタイトル」を変更する方法 (SEO)"
description: "クライアント向けWebflow更新マニュアル：Google検索結果に出る「ページのタイトル」を変更する方法 (SEO)"
sidebar:
  order: 1
  label: "Google検索結果に出る「ページのタイトル」を変更する方法 (SEO)"
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- F-02: `src/assets/captures/manual/f-02-seo-settings-overview.png`。Site settings > SEO。SEO設定の入口が分かる
- F-03: `src/assets/captures/manual/f-03-page-seo-settings.png`。DesignerのPage settings > SEO。Title tag、Meta description入力欄が見える

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::tip[反映タイミングの目安]
Webflow上で保存しても、Google検索結果やSNSのプレビューはすぐに変わらないことがあります。Webflowの公開確認と、検索エンジンやSNS側の反映確認は分けて考えると混乱しにくくなります。
:::
<!-- body-callout:end -->


> 旧マニュアル番号: [No.47](/05-settings/01-seo-title/)

Webサイトの集客において、GoogleやYahoo!などの検索エンジンからの流入は非常に重要です。その検索結果に表示される「ページのタイトル（Title Tag）」は、ユーザーがクリックするかどうかを決める最も重要な要素の一つです。ここでは、各ページのタイトルを最適化する方法を解説します。

---

## 1. ページタイトル（Title Tag）とは？

-   <strong>検索結果の青い文字:</strong> Googleなどで検索した時に表示される、クリック可能な青い大きな見出しテキストのことです。
-   <strong>ブラウザのタブ:</strong> Webページを開いている時に、ブラウザのタブに表示されるテキストのことです。
-   <strong>SEOの最重要項目:</strong> 検索エンジンは、このタイトルタグを「このページが何について書かれているか」を理解するための最重要の手がかりとして利用します。

:::note[キャプチャー差し込み位置]
ここには「検索結果のページタイトル」が分かる実画面キャプチャーを入れてください。ページ上部のキャプチャー指示にある保存ファイル名へ差し替えます。
:::

## 2. ページタイトルを設定する場所

各ページのSEO関連設定は、デザイナーモードではなく、<strong>サイト設定（Site Settings）</strong>または<strong>ページ設定（Page Settings）</strong>から行います。CMSアイテム（ブログ記事など）の場合は、CMSの編集画面から設定します。
*実画面例: Site settingsのSEO画面です。ページ単位のTitle Tagは、DesignerのPage SettingsやCMS item側で設定します。*

### 静的ページ（トップページ、会社概要など）の場合

1.  <strong>デザイナーモードを開きます。</strong>
2.  左側のパネル群から<strong>「Pages」</strong>（ページのアイコン）をクリックします。
3.  ページ一覧が表示されるので、設定を変更したいページ（例: `About Us`）にカーソルを合わせ、表示される<strong>歯車アイコン（Settings）</strong>をクリックします。
4.  ページ設定パネルが開きます。その中の<strong>「SEO Settings」</strong>というセクションに<strong>「Title Tag」</strong>という入力欄があります。ここが設定場所です。

### CMSページ（ブログ記事、お知らせなど）の場合

1.  <strong>CMSのアイテム編集画面を開きます。</strong>
2.  編集パネルを一番下までスクロールすると、<strong>「SEO Settings」</strong>というセクションがあります。そこの<strong>「Title Tag」</strong>に入力します。

## 3. 効果的なページタイトルの付け方

-   <strong>キーワードを含める:</strong> ユーザーが検索しそうなキーワード（例: `Webflow 更新マニュアル`）を、タイトルのなるべく先頭に含めます。
-   <strong>クリックしたくなる工夫:</strong> 具体的な数字を入れたり（例: `5つのステップ`）、メリットを提示したり（例: `初心者でも簡単`）して、ユーザーの興味を引きます。
-   <strong>会社名・サイト名を入れる:</strong> タイトルの最後に `| 会社名` のようにサイト名を入れると、ブランド認知に繋がります。
-   <strong>文字数:</strong> PCでは約30文字、スマートフォンでは約35文字を超えると、末尾が「…」と省略される可能性が高いです。重要なキーワードは前半に配置しましょう。

<strong>例:</strong>
`【初心者向け】Webflow更新マニュアル | 株式会社サンプル`

## 4. 変更の反映

-   <strong>静的ページの場合:</strong> 変更後、サイト全体を<strong>Publish</strong>する必要があります。
-   <strong>CMSページの場合:</strong> 記事を<strong>Publish</strong>または<strong>Save</strong>すると反映されます。

<strong>注意:</strong> 変更がGoogleの検索結果に反映されるまでには、数日から数週間かかる場合があります。即座に変わるわけではありません。

---

<strong>次のステップ:</strong>
タイトルとセットで重要な、「[No.48](/05-settings/02-seo-description/) Google検索結果に出る「ページの説明文」を変更する方法 (SEO)」に進みましょう。
