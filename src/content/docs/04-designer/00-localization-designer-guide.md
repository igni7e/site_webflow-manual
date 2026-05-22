---
title: DesignerでLocale関連画面を触る前の注意
description: Webflow DesignerでLocale関連画面を触る前に確認する注意点と、Eセクションへの案内をまとめます。
sidebar:
  order: 0
---


<!-- body-callout:start -->
:::caution[Locale確認]
翻訳作業では、今どのLocaleを編集しているかを最初に確認します。日本語、英語などのLocaleを間違えると、意図しない言語ページを書き換える可能性があります。
:::
<!-- body-callout:end -->

![Designerを開いた状態](../../../assets/captures/manual/d-01-designer-opened.png)


# DesignerでLocale関連画面を触る前の注意

Designerは、Webflowサイトのデザイン、レイアウト、構造、Locale設定まで編集できる強力な画面です。Editorより自由度が高い一方で、誤操作の影響も大きいため、通常の文章・画像更新では使わず、必要な場合だけ使ってください。

Locale翻訳の実作業は、独立した [E. Locale翻訳](/07-localization/00-localization-overview/) セクションで説明します。このページでは、Designer側でLocale関連画面を触る前の注意点だけ確認します。
*実画面例: Locale関連の修正もDesigner上で確認することがあります。現在のLocaleと公開対象を確認してから作業します。*

## Designerを使う前の注意

- 作業前に変更箇所を決めておく
- 触る必要のない要素は変更しない
- レイアウトやスタイルを不用意に変更しない
- Publish前にPreviewで確認する
- 不安な場合は、作業前に [IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) から確認する

Designerの基本的な注意点は [Designerを開く時の注意点](/04-designer/01-designer-warning/) を先に確認してください。

## Locale関連作業の入口

1. Webflowにログインし、対象サイトをDesignerで開きます。
2. 画面上部のLocale selectorで、今どのLocaleを見ているか確認します。
3. Localeを追加するのか、既存翻訳を直すのか、CMS記事を翻訳するのかを決めます。
4. 詳しい手順は [E. Locale翻訳](/07-localization/00-localization-overview/) に移動して確認します。

Locale機能で翻訳を追加・修正する詳しい流れは、[E. Locale翻訳](/07-localization/00-localization-overview/) セクションを確認してください。

## Designer側で特に注意すること

- 今選んでいるLocaleを確認してから編集する
- Primary localeとSecondary localeを混同しない
- 新しいLocale追加やSubdirectory変更は自己判断で進めない
- Translate実行前に、既に手動修正済みの翻訳がないか確認する
- Publish前に対象Localeと公開ドメインを確認する

## よくあるトラブル

| 症状 | 対応 |
| --- | --- |
| Translateボタンが出ない | Localization設定と対象Localeの有無を確認する |
| 翻訳したのに反映されない | Publish対象ドメインとLocaleを確認する |
| 文字がはみ出す | 文章を短くするか、[IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) からレイアウト調整を依頼する |
| CMSだけ翻訳されない | CMSアイテム側で対象Localeのフィールドを確認する |

## 理解度チェック

1. Designerを使う前の姿勢として正しいものはどれですか？
   - A. 必要な箇所以外もまとめて触っておく
   - B. 作業箇所を決め、不要な要素は変更しない
   - C. Preview確認は省略する

#### 答え

正解: B

Designerはサイト構造や見た目に影響するため、変更範囲を決めてから作業します。


2. 多言語ページを修正するとき、最初に確認するものはどれですか？
   - A. 対象Localeが選ばれているか
   - B. ブラウザのズーム率
   - C. 請求プランの支払い方法

#### 答え

正解: A

別Localeを選んだまま修正すると、意図しない言語の内容を変更してしまう可能性があります。


3. 機械翻訳を使った後に必要な確認はどれですか？
   - A. 翻訳結果を人の目で確認し、固有名詞や専門用語を直す
   - B. 翻訳ボタンを押したら確認せずPublishする
   - C. 原文をすべて削除する

#### 答え

正解: A

機械翻訳は補助です。公開前に意味、表記、レイアウト崩れを確認します。


## 次に進む

Designerを開く場合は、先に [Designerを開く時の注意点](/04-designer/01-designer-warning/) を読んでから進んでください。Locale翻訳の具体的な操作は [E. Locale翻訳](/07-localization/00-localization-overview/) に進んでください。
