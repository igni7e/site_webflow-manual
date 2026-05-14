---
title: "Locale公開前チェックリスト"
description: "Webflow Localizationで翻訳したページやCMS記事をPublishする前に確認する項目をまとめます。"
sidebar:
  order: 7
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- E-19: `src/assets/captures/manual/e-19-publish-modal-locale.png`。Publish modalでLocale / domain確認。公開対象を間違えない構図
- E-21: `src/assets/captures/manual/e-21-public-locale-switcher.png`。公開サイト上の言語切り替えUI。Japanese / Englishなど切替UIが見える
- E-22: `src/assets/captures/manual/e-22-mobile-locale-check.png`。スマホ幅で翻訳ページを確認。見出し、CTA、ナビゲーションが崩れていない

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::caution[公開前チェック]
Publishする前に、公開先ドメイン、変更したページ、スマートフォン表示、リンク先を確認します。公開後は一般の閲覧者に見えるため、少しでも不安があればスクリーンショットを撮って確認してから進めます。
:::
<!-- body-callout:end -->


# Locale公開前チェックリスト

Locale翻訳は、本文だけでなくURL、SEO、CMS、言語切り替えにも影響します。Publish前にこのチェックリストで確認してください。
*実画面例: Locale公開前は、公開対象のドメインや公開状態を確認してからPublishします。*

## 作業前

- 現在選択しているLocaleが正しい
- 翻訳対象のページまたはCMS itemが明確
- Primary localeの内容が最新
- 既に手動翻訳済みの内容を上書きしない
- 新しいLocale追加やURL変更はIGNITEへ確認済み

## 翻訳内容

- 機械翻訳のまま不自然な文章が残っていない
- 固有名詞、サービス名、会社名が勝手に訳されていない
- 問い合わせ導線が正しい
- 価格、日付、住所、電話番号が正しい
- CTA文言が自然

## 表示確認

- PC表示で文字がはみ出していない
- スマートフォン表示で改行が崩れていない
- ボタンやナビゲーションの文字が収まっている
- 画像が対象Localeに合っている
- 画像altテキストも翻訳されている

## CMS確認

- 記事詳細ページが対象Localeで表示される
- 一覧ページに対象Localeの記事が出ている
- CategoryやAuthorなど参照項目が正しい
- 下書き・公開状態が正しい
- Primary localeの内容が残っていない

## SEO・公開確認

- Page titleが対象言語で自然
- Meta descriptionが対象言語で自然
- OGP title / descriptionが対象言語で自然
- OGP画像が適切
- 対象LocaleのPublishing statusが正しい
- Publish後に実際のLocale URLで確認した

> <strong>キャプチャー指示</strong>: このページには、E-21「Locale switcher」とE-22「スマートフォン表示」を入れてください。言語切り替え後のURL、ヘッダー、CTA、フッターが確認できる画面を優先します。

## 困った場合

新しい言語追加、URL変更、公開設定、SEO、表示崩れが関係する場合は、自己判断で進めずIGNITEへ相談してください。
