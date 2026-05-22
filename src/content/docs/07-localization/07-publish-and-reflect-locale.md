---
title: "E-7. Locale翻訳を公開サイトに反映する方法"
description: "Webflow Localizationで翻訳した内容をPublishし、公開URLで確認する流れを説明します。"
sidebar:
  label: "E-7. Locale翻訳を公開サイトに反映する方法"
  order: 6
---


<!-- body-callout:start -->
:::caution[公開前チェック]
Publishする前に、公開先ドメイン、変更したページ、スマートフォン表示、リンク先を確認します。公開後は一般の閲覧者に見えるため、少しでも不安があればスクリーンショットを撮って確認してから進めます。
:::
<!-- body-callout:end -->


# E-7. Locale翻訳を公開サイトに反映する方法

Localeの翻訳は、DesignerやCMS上で編集しただけでは公開サイトに反映されません。対象Localeの公開設定とPublish対象を確認し、公開後に実際のURLで表示を確認します。
*実画面例: 翻訳を公開サイトに反映する時は、Publish対象と公開後URLを確認します。*

## 反映前に確認すること

- 翻訳対象のLocaleを選んでいる
- 翻訳したページまたはCMS itemが保存されている
- 対象LocaleのPublishing statusが公開可能な状態になっている
- Page title、Meta description、OGPも確認済み
- ボタン、リンク、フォーム、言語切り替えが対象Localeで正しく動く
- 公開してよいタイミングである

## 基本手順

1. DesignerまたはCMSで翻訳内容を保存します。
2. Locale selectorで対象Localeをもう一度確認します。
3. 対象LocaleのPublishing statusを確認します。
4. Publishを開きます。
5. 公開対象のドメインとLocaleを確認します。
6. Publishを実行します。
7. 公開後、実際のLocale URLをブラウザで開きます。
8. PC表示とスマートフォン表示を確認します。
9. Locale switcherで他言語へ切り替えられるか確認します。

## 公開後に見るURL

Secondary localeにSubdirectoryを設定している場合、公開URLは次のような形になります。

```text
https://example.com/en/
https://example.com/en/blog/sample-post/
```

Primary localeにはSubdirectoryが付かない構成もあります。サイトによってURL設計が異なるため、実際の公開URLは必ずWebflowの設定と公開サイトで確認してください。

## 反映されない時に見る場所

| 症状 | 確認する場所 |
| --- | --- |
| 翻訳した文章が出ない | 編集したLocale、保存状態、Publish対象 |
| `/en` のページが開けない | Publishing status、Subdirectory、公開ドメイン |
| 言語切り替えに出ない | Locale list、Publishing status、Publish済みか |
| CMS記事だけ出ない | CMS itemのLocale、公開状態、一覧ページの条件 |
| SEOだけ原文のまま | Page settings、CMS SEO fields、OGP fields |


## 困った場合

公開設定、URL、SEO、表示崩れ、言語切り替えが関係する場合は、自己判断で何度も変更せず、現在のURLと状況を添えてIGNITEへ相談してください。すでに保守契約を結んでいる方は、問い合わせフォームではなく、Google Chatや担当者宛に保守連絡として送ってください。

## 次に進む

Publish前後の最終確認には [Locale公開前チェックリスト](/07-localization/05-locale-publish-checklist/) を使ってください。
