---
title: "CMS記事をLocaleごとに翻訳する"
description: "ブログ、お知らせ、導入事例などのCMS itemをLocaleごとに翻訳・確認する方法を説明します。"
sidebar:
  order: 4
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- E-13: `src/assets/captures/manual/e-13-cms-collection-locale.png`。CMS Collection一覧とLocale切り替え。Collectionと対象Localeが同時に分かる
- E-14: `src/assets/captures/manual/e-14-cms-item-locale-fields.png`。CMS item内のLocaleフィールド。Title、Body、SEOなどが見える
- E-15: `src/assets/captures/manual/e-15-translate-all-fields.png`。Translate all fields操作。複数フィールド翻訳の入口
- E-16: `src/assets/captures/manual/e-16-rich-text-locale-body.png`。Locale版Rich Text本文。翻訳済み本文、見出し、画像が分かる

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::caution[Locale確認]
翻訳作業では、今どのLocaleを編集しているかを最初に確認します。日本語、英語などのLocaleを間違えると、意図しない言語ページを書き換える可能性があります。
:::
<!-- body-callout:end -->


# CMS記事をLocaleごとに翻訳する

ブログやお知らせは、CMS itemごとに翻訳します。Primary localeの内容がSecondary localeへ継承されることがありますが、Secondary locale側で上書きしたフィールドは独立して管理される場合があります。
*実画面例: CMS翻訳後は、記事詳細ページと一覧ページの両方で表示を確認します。*

## 作業手順

1. CMS Collectionを開きます。
2. 対象記事を選びます。
3. 対象Localeに切り替えます。
4. タイトル、Slug、本文、概要、画像alt、SEO項目を確認します。
5. 必要に応じて `Translate all fields` などの翻訳機能を使います。
6. 翻訳後、本文の改行、見出し、画像、リンクを確認します。
7. 対象LocaleでPublishされているか確認します。

> <strong>キャプチャー指示</strong>: このページには、E-13「CMS Collection一覧」、E-14「CMS itemのLocale切り替え」、E-15「Translate all fields」、E-16「Rich Text本文」を入れてください。未公開記事や実名情報が映らないように、撮影用の記事または公開済みサンプル記事を使います。

## CMSで確認する項目

| 項目 | 確認内容 |
| --- | --- |
| Title / Name | 記事タイトルが自然か |
| Slug | URLとして分かりやすいか |
| Summary / Description | 一覧ページで自然に読めるか |
| Rich Text | 見出し、本文、リンク、画像が崩れていないか |
| Thumbnail Image | 一覧ページやSNSで適切か |
| Category | 翻訳先Localeで正しく紐づいているか |
| SEO fields | 検索結果向けに翻訳されているか |

## 継承と上書きの考え方

Primary localeを更新すると、Secondary localeにも内容が反映されることがあります。ただし、Secondary localeで手動修正したフィールドは、Primary localeとは別の内容として扱われる場合があります。

確認すること:

- 翻訳済みの本文をPrimary localeの更新で上書きしていないか
- CategoryやAuthorなど参照項目が正しいLocale版を指しているか
- 新規記事をPrimary locale側で作成してから翻訳しているか

## 公開後の確認

- 記事詳細ページが対象Localeで表示される
- 一覧ページにも対象Localeの記事が出ている
- 日本語ページから英語ページへ切り替えられる
- 英語ページから日本語ページへ戻れる
- OGPやSEO項目がPrimary localeのまま残っていない

## 次に進む

検索結果やSNS共有の表示も確認する場合は [LocaleごとのSEO・OGP確認](/07-localization/04-localized-seo-ogp/) を確認してください。
