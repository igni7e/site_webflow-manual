---
title: "Locale翻訳の基本手順"
description: "WebflowのLocale selectorを使い、対象言語を選んで翻訳・確認・公開する基本手順を説明します。"
sidebar:
  order: 1
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- E-01: `src/assets/captures/manual/e-01-locale-selector-topbar.png`。Designer上部のLocale selector。現在のLocaleが一目で分かる
- E-08: `src/assets/captures/manual/e-08-select-secondary-locale.png`。Secondary localeを選ぶ直前。Locale selectorを開いた状態
- E-09: `src/assets/captures/manual/e-09-secondary-locale-canvas.png`。Secondary localeのキャンバス。対象Locale選択後のページ表示

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::caution[Locale確認]
翻訳作業では、今どのLocaleを編集しているかを最初に確認します。日本語、英語などのLocaleを間違えると、意図しない言語ページを書き換える可能性があります。
:::
<!-- body-callout:end -->


# Locale翻訳の基本手順

Locale翻訳では、最初に「どの言語を編集しているか」を確認することが最も重要です。別のLocaleを選んだまま編集すると、意図しない言語の内容を変更してしまうことがあります。
*実画面例: Locale翻訳では、ページの見た目だけでなく、現在選択しているLocaleも確認します。*

## 作業の流れ

1. Webflowにログインし、対象サイトをDesignerで開きます。
2. 画面上部のLocale selector、またはSettings panelのLocalizationから対象Localeを確認します。
3. 修正したいSecondary localeを選びます。
4. 静的ページ、CMS item、SEO設定など、翻訳したい場所を開きます。
5. 必要に応じてWebflowの機械翻訳を使います。
6. 翻訳結果を人の目で確認し、不自然な表現を直します。
7. PC表示とスマートフォン表示を確認します。
8. 必要なLocaleとドメインを選んでPublishします。
9. 公開後、実際のLocale URLで確認します。

> <strong>キャプチャー指示</strong>: このページには、E-08「Locale selectorを開いた状態」とE-09「Secondary localeのキャンバス」を入れてください。どちらもBOOSTサイトで、編集対象のLocaleが一目で分かるように上部バーを含めて撮影します。

## 翻訳前に確認すること

- Primary localeの内容が最新か
- 編集するSecondary localeが正しいか
- 翻訳対象が静的ページかCMSかSEOか
- 既に手動修正済みの翻訳を上書きしないか
- Publishしてよいタイミングか

## 機械翻訳を使う時の考え方

機械翻訳は最初のたたき台として便利です。ただし、公開前に必ず人の目で確認してください。

特に確認するもの:

- 固有名詞
- 商品名・サービス名
- 専門用語
- ボタン文言
- 問い合わせ導線
- 価格や日付
- 法務・医療・採用など誤訳リスクが高い文章

## 翻訳後に起きやすい問題

| 症状 | 原因 | 対応 |
| --- | --- | --- |
| ボタン文字がはみ出す | 翻訳後に文章が長くなった | 文言を短くするか、レイアウト調整を依頼 |
| 一部だけ原文のまま | 未翻訳フィールドが残っている | ページ、CMS、SEOを順番に確認 |
| 公開サイトに出ない | 対象LocaleがPublishされていない | Publishing statusと公開対象を確認 |
| URLが想定と違う | SubdirectoryやSlug設定の影響 | 自己判断で変更せず相談 |

## 次に進む

まだ対象Localeが用意されていない場合は [新しいLocaleを追加する時の流れ](/07-localization/06-add-new-locale/) を確認してください。固定ページを翻訳する場合は [静的ページをLocaleごとに翻訳する](/07-localization/02-static-page-translation/) を確認してください。
