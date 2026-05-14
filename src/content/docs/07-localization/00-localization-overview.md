---
title: "Locale翻訳の全体像"
description: "Webflow LocalizationとLocale機能の基本、翻訳できる範囲、作業前の注意点をまとめます。"
sidebar:
  order: 0
---

# Locale翻訳の全体像

Webflowの <strong>Localization</strong> は、1つのWebflowサイトの中で複数言語・複数地域向けのページを管理する機能です。IGNITEで多言語サイトを制作している場合、英語ページや日本語ページは、この <strong>Locale</strong> 機能を使って翻訳・修正していることがあります。

このセクションでは、「翻訳はどこから入れるのか」「CMS記事はどう翻訳するのか」「SEOや言語切り替えは何を確認するのか」を順番に説明します。

> <strong>注意</strong>: Locale設定、公開設定、URL構造、SEOに関わる作業は影響範囲が大きいです。既存サイトで新しい言語を追加したい場合や、公開中の言語URLを変えたい場合は、自己判断で進めずIGNITEへ相談してください。

## Localeとは

Localeは、サイトの言語や地域を表す設定です。例えば、日本語をPrimary locale、英語をSecondary localeとして管理できます。

| 項目 | 意味 |
| --- | --- |
| Language | 日本語、英語などの言語 |
| Country | 日本、米国、英国などの地域。必要な場合だけ設定 |
| Display name | 言語切り替えに表示する名前 |
| Subdirectory | `/en` や `/ja` など、URLに使う言語パス |
| Display image | 言語切り替えに使う旗やアイコン |
| Publishing status | Secondary localeを公開するかどうか |

Primary localeはサイトの基準になる言語です。最初に作成したLocaleがPrimary localeになり、あとからSecondary localeをPrimary localeへ変更することはできません。

## 翻訳できる主な場所

| 対象 | 例 | 確認ポイント |
| --- | --- | --- |
| 静的ページ | トップページ、会社概要、サービスページの見出しや本文 | 文章、ボタン、リンク、画像、altテキスト |
| CMS | ブログ、お知らせ、導入事例 | タイトル、本文、概要、カテゴリー、画像alt |
| SEO | ページタイトル、meta description、OGP、Slug | 検索結果・SNS共有で自然に見えるか |
| Components | ヘッダー、フッター、CTAなど共通パーツ | 全ページに影響するため慎重に確認 |

## 読む順番

1. [Locale翻訳の基本手順](/07-localization/01-locale-translation-workflow/)
2. [静的ページをLocaleごとに翻訳する](/07-localization/02-static-page-translation/)
3. [CMS記事をLocaleごとに翻訳する](/07-localization/03-cms-locale-translation/)
4. [LocaleごとのSEO・OGP確認](/07-localization/04-localized-seo-ogp/)
5. [Locale公開前チェックリスト](/07-localization/05-locale-publish-checklist/)

## 基本方針

- 機械翻訳は下書きとして使い、公開前に人の目で確認する
- 固有名詞、サービス名、会社名、問い合わせ導線は勝手に訳されていないか確認する
- ボタンや見出しは、翻訳後に長くなりやすいため表示崩れを確認する
- CMS記事は一覧ページと詳細ページの両方を確認する
- SEO項目とOGPもLocaleごとに確認する

## 参考リンク

- [Webflow Help Center: Localization overview](https://help.webflow.com/hc/en-us/articles/33961240752147-Localization-overview)
- [Webflow Help Center: Locales list and locale data](https://help.webflow.com/hc/en-us/articles/47395993517587-Locales-list-and-locale-data)
- [Webflow Help Center: Locale-specific access](https://help.webflow.com/hc/en-us/articles/50401263212947-Locale-specific-access)
- [Webflow: Localize text and SEO](https://webflow.com/webflow-way/localization/localize-text-and-seo)

