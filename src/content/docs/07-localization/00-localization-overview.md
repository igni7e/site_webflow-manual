---
title: "E-1. Locale翻訳の全体像"
description: "Webflow LocalizationとLocale機能の基本、翻訳できる範囲、作業前の注意点をまとめます。"
sidebar:
  order: 0
  label: "E-1. Locale翻訳の全体像"
---


<!-- body-callout:start -->
:::caution[Locale確認]
翻訳作業では、今どのLocaleを編集しているかを最初に確認します。日本語、英語などのLocaleを間違えると、意図しない言語ページを書き換える可能性があります。
:::
<!-- body-callout:end -->

![Designer上部のLocale selector](../../../assets/captures/manual/e-01-locale-selector.png)

![Webflow公式: Localization](https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/680fb9c78c1f42a6c861a3f5_og-localization.jpg)

:::note[公式画像]
上の画像はWebflow公式Localizationページの画像です。Booostで翻訳作業をする時は、公式画像で全体像を確認し、実際の作業では現在選択中のLocaleを必ず確認してください。
:::


![Locale翻訳の流れの図解](../../../assets/ai-diagrams/manual/localization-workflow.png)

:::note[図解の見方]
今どのLocaleを触っているかを最初に確認します。
:::


Webflowの <strong>Localization</strong> は、1つのWebflowサイトの中で複数言語・複数地域向けのページを管理する機能です。IGNITEで多言語サイトを制作している場合、英語ページや日本語ページは、この <strong>Locale</strong> 機能を使って翻訳・修正していることがあります。

このセクションでは、「Localeはどう追加するのか」「翻訳はどこから入れるのか」「CMS記事はどう翻訳するのか」「公開サイトへどう反映するのか」「SEOや言語切り替えは何を確認するのか」を順番に説明します。
*実画面例: Booostのような多言語サイトでは、表示中の言語や公開状態を確認しながら翻訳を扱います。*

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
2. [新しいLocaleを追加する時の流れ](/07-localization/06-add-new-locale/)
3. [静的ページをLocaleごとに翻訳する](/07-localization/02-static-page-translation/)
4. [CMS記事をLocaleごとに翻訳する](/07-localization/03-cms-locale-translation/)
5. [LocaleごとのSEO・OGP確認](/07-localization/04-localized-seo-ogp/)
6. [Locale翻訳を公開サイトに反映する方法](/07-localization/07-publish-and-reflect-locale/)
7. [Locale公開前チェックリスト](/07-localization/05-locale-publish-checklist/)

## 基本方針

- 機械翻訳は下書きとして使い、公開前に人の目で確認する
- 固有名詞、サービス名、会社名、問い合わせ導線は勝手に訳されていないか確認する
- ボタンや見出しは、翻訳後に長くなりやすいため表示崩れを確認する
- CMS記事は一覧ページと詳細ページの両方を確認する
- SEO項目とOGPもLocaleごとに確認する
