---
title: "Locale翻訳の全体像"
description: "Webflow LocalizationとLocale機能の基本、翻訳できる範囲、作業前の注意点をまとめます。"
sidebar:
  order: 0
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- E-01: `src/assets/captures/manual/e-01-locale-selector-topbar.png`。Designer上部のLocale selector。現在のLocaleが一目で分かる
- E-02: `src/assets/captures/manual/e-02-localization-settings-panel.png`。Settings panel > Localization。Primary locale、Secondary localeが分かる

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::caution[Locale確認]
翻訳作業では、今どのLocaleを編集しているかを最初に確認します。日本語、英語などのLocaleを間違えると、意図しない言語ページを書き換える可能性があります。
:::
<!-- body-callout:end -->


# Locale翻訳の全体像

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

## キャプチャー方針

Locale機能は画面を見た方が理解しやすいため、この章ではBOOSTサイトを使ってキャプチャーを多めに入れる前提で構成します。後から撮影する時は、以下の指示に沿って画面を用意してください。

同じIDのキャプチャーは、複数ページで使い回して問題ありません。例えばE-21とE-22は「公開反映ページ」と「公開前チェックリスト」の両方に同じ画像を配置する想定です。

> <strong>キャプチャー指示</strong>: 個人情報、未公開記事、顧客名、社内コメント、分析数値、問い合わせ内容が映る場合は、撮影前に別画面へ切り替えるか、公開してよいテストデータに差し替えてください。

| ID | 入れる場所 | 撮影する画面 | 撮影指示 |
| --- | --- | --- | --- |
| E-01 | Locale翻訳の全体像 | Designer上部のLocale selector | BOOSTサイトをDesignerで開き、上部バーにLocale selectorが見える状態で撮影 |
| E-02 | Locale翻訳の全体像 | Settings panel > Localization | 左側パネルからLocalization設定を開き、Primary localeとSecondary localeの関係が分かる状態で撮影 |
| E-03 | 新しいLocaleを追加する時の流れ | Locale一覧 | 既存Localeの一覧、Display name、Subdirectory、Publishing statusが分かる状態で撮影 |
| E-04 | 新しいLocaleを追加する時の流れ | Add localeの入口 | 新しいLocaleを追加するボタンまたは入力エリアが見える状態で撮影 |
| E-05 | 新しいLocaleを追加する時の流れ | Language / Country入力 | LanguageとCountryを選ぶ画面を撮影。実運用では変更確定前の状態で止める |
| E-06 | 新しいLocaleを追加する時の流れ | Subdirectory入力 | `/en` などURLに関わる項目が見える状態で撮影。既存URLと衝突しない注意書きとセットで使う |
| E-07 | 新しいLocaleを追加する時の流れ | Publishing status | Enable publishing to the subdirectoryのオン・オフが分かる状態で撮影 |
| E-08 | Locale翻訳の基本手順 | Locale selectorを開いた状態 | 編集対象Localeを選ぶ直前の画面を撮影 |
| E-09 | Locale翻訳の基本手順 | Secondary localeのキャンバス | 英語などSecondary localeを選択した後、ページが表示されている状態で撮影 |
| E-10 | 静的ページ翻訳 | テキスト要素を選択 | 見出しや本文を選択し、翻訳対象のテキストが分かる状態で撮影 |
| E-11 | 静的ページ翻訳 | 機械翻訳の操作 | Translateまたは翻訳候補を使う画面を撮影 |
| E-12 | 静的ページ翻訳 | 翻訳後の表示確認 | 翻訳後にボタンや見出しがはみ出していない状態を撮影 |
| E-13 | CMS記事翻訳 | CMS Collection一覧 | 対象Collectionと記事一覧が分かる状態で撮影 |
| E-14 | CMS記事翻訳 | CMS itemのLocale切り替え | CMS item内で対象Localeを選んでいる状態を撮影 |
| E-15 | CMS記事翻訳 | Translate all fields | CMS itemの複数フィールド翻訳操作が分かる状態で撮影 |
| E-16 | CMS記事翻訳 | Rich Text本文 | 見出し、本文、リンク、画像が入った本文編集画面を撮影 |
| E-17 | SEO・OGP確認 | Page settingsのSEO欄 | 対象LocaleのPage titleとMeta descriptionが見える状態で撮影 |
| E-18 | SEO・OGP確認 | OGP設定 | OGP title、description、imageが見える状態で撮影 |
| E-19 | 公開反映 | Publish modal | 公開対象のドメイン・Localeを確認している状態で撮影 |
| E-20 | 公開反映 | 公開後のLocale URL | `/en` など実際の公開URLをブラウザで開き、言語が切り替わっている状態で撮影 |
| E-21 | 公開前チェック | Locale switcher | 公開サイト上の言語切り替えUIを開いた状態で撮影 |

## 参考リンク

- [Webflow Help Center: Localization overview](https://help.webflow.com/hc/en-us/articles/33961240752147-Localization-overview)
- [Webflow Help Center: Locales list and locale data](https://help.webflow.com/hc/en-us/articles/47395993517587-Locales-list-and-locale-data)
- [Webflow Help Center: Locale-specific access](https://help.webflow.com/hc/en-us/articles/50401263212947-Locale-specific-access)
- [Webflow: Localize text and SEO](https://webflow.com/webflow-way/localization/localize-text-and-seo)
