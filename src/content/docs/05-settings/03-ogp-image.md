---
title: "SNSでシェアされた時の画像（OGP画像）を変更する方法"
description: "クライアント向けWebflow更新マニュアル：SNSでシェアされた時の画像（OGP画像）を変更する方法"
sidebar:
  order: 3
  label: "SNSでシェアされた時の画像（OGP画像）を変更する方法"
---

> 旧マニュアル番号: [No.49](/05-settings/03-ogp-image/)

FacebookやX (Twitter) などのSNSでWebサイトのURLがシェアされた際、自動的に表示される画像やタイトル、説明文は、その投稿がクリックされるかどうかを大きく左右します。これらは「OGP（Open Graph Protocol）」と呼ばれる設定によって制御されています。

---

## 1. OGPとは？

OGPは、WebページがSNSでシェアされた時に、どのように表示されるかを指定するための仕組みです。特に重要なのは以下の3点です。

-   <strong>OGP画像 (og:image):</strong> 投稿に表示される画像。視覚的なインパクトが最も大きいです。
-   <strong>OGPタイトル (og:title):</strong> 投稿に表示されるページのタイトル。
-   <strong>OGP説明文 (og:description):</strong> 投稿に表示されるページの説明文。

これらを適切に設定することで、SNSでの拡散効果を高めることができます。

![OGP表示例](../../../assets/captures/ogp-example.svg)
*※画像はイメージです。*

## 2. OGP画像を設定する場所

OGP画像の設定場所は、ページのSEO設定と同じ場所にあります。

### 静的ページ（トップページ、会社概要など）の場合

1.  <strong>デザイナーモードを開きます。</strong>
2.  左側のパネル群から<strong>「Pages」</strong>（ページのアイコン）をクリックします。
3.  ページ一覧が表示されるので、設定を変更したいページにカーソルを合わせ、表示される<strong>歯車アイコン（Settings）</strong>をクリックします。
4.  ページ設定パネルが開きます。その中の<strong>「Open Graph Settings」</strong>というセクションに<strong>「Open Graph Image」</strong>という項目があります。ここが設定場所です。

### CMSページ（ブログ記事、お知らせなど）の場合

1.  <strong>CMSのアイテム編集画面を開きます。</strong>
2.  編集パネルを一番下までスクロールすると、<strong>「Open Graph Settings」</strong>というセクションがあります。そこの<strong>「Open Graph Image」</strong>に入力します。

## 3. OGP画像を設定する手順

1.  <strong>「Open Graph Image」の画像アップロードエリアをクリック:</strong>
    設定場所にある画像アップロードエリアをクリックします。

2.  <strong>ファイル選択ウィンドウが開く:</strong>
    お使いのパソコンのファイル選択ウィンドウが開きます。

3.  <strong>OGP画像ファイルを選択:</strong>
    あらかじめSNSシェア用に準備しておいた画像ファイルを選択し、「開く」ボタンをクリックします。

4.  <strong>アップロードとプレビュー確認:</strong>
    画像がWebflowにアップロードされ、設定欄にプレビューが表示されます。意図した画像が正しく設定されたかを確認してください。

## 4. OGP画像の推奨サイズ

-   <strong>推奨サイズ:</strong> `1200px × 630px` の画像が推奨されます。この比率で作成すると、主要なSNSで適切に表示されやすくなります。
-   <strong>ファイル形式:</strong> JPGまたはPNG。
-   <strong>ファイルサイズ:</strong> 1MB以下が望ましいです。

## 5. OGPタイトル・説明文の設定

OGPタイトルとOGP説明文は、通常、SEO設定の「Title Tag」と「Meta Description」が自動的に引き継がれます。もしSNS用に異なるタイトルや説明文を設定したい場合は、それぞれの入力欄に直接入力してください。

## 6. 変更の反映確認

設定を変更したら、以下のツールでSNSでの表示をシミュレーションできます。

-   <strong>Facebook:</strong> [Sharing Debugger](https://developers.facebook.com/tools/debug/)
-   <strong>X (Twitter):</strong> [Card Validator](https://cards-dev.twitter.com/validator)

URLを入力して「Debug」または「Preview card」をクリックすると、最新のOGP情報が取得され、どのように表示されるかを確認できます。

---

<strong>次のステップ:</strong>
SNSでの見栄えもバッチリですね。次は、Webサイトの重要な機能の一つである「お問い合わせフォーム」に関する「[No.50](/05-settings/04-form-submissions/) 「お問い合わせフォーム」から連絡が来たか確認する方法」です。
