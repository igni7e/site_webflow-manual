---
title: "【基本】Content editor roleでWebflowを開く方法"
description: "クライアント向けWebflow更新マニュアル：Content editor roleでWebflowを開く方法"
sidebar:
  order: 1
  label: "Content editor roleで開く"
---

> 旧マニュアル番号: [No.9](/02-editor/01-open-editor/)

ここからは、実際のサイト更新作業で最もよく使う **Content editor roleでの開き方** について解説します。

従来のLegacy Editorは2026年8月4日から利用できなくなる予定です。現在は、Webflowの中でContent editor roleとしてcanvasを開き、デザインを触らずにコンテンツだけを更新する流れが推奨されています。

---

## 1. 方法1：ダッシュボードから開く（基本）

ログイン後の最初の画面である「Dashboard」から対象サイトを開く、最も基本的な方法です。

1.  **Webflowにログイン:**
    「[No.3](/01-getting-started/03-first-login/)」で解説した手順で、まずはWebflowにログインします。

2.  **ダッシュボードでサイトを選択:**
    ログインすると、編集権限のあるサイトが一覧表示された「ダッシュボード」が開きます。目的のサイトのサムネイル画像の上に、マウスカーソルを合わせます。

3.  **「Open in Webflow」または案内された編集用ボタンをクリック:**
    カーソルを合わせると表示されるメニューの中から、制作担当者から案内された編集用ボタンをクリックします。Content editor roleが付与されている場合、デザイン編集ではなくコンテンツ編集に必要な範囲でWebflowを開けます。

    ![ダッシュボードからWebflowを開く](../../../assets/captures/editor-button.svg)
    *※画像はイメージです。*

4.  **Webflowのcanvasでサイトが開く:**
    サイトの見た目を確認しながら、編集可能なテキスト、画像、リンク、CMSコンテンツを更新できます。

## 2. 方法2：`?update` で直接開く

毎回Dashboardを経由せず、公開サイトの該当ページから直接Content editor roleの編集画面へ入る方法です。

1.  **専用URLにアクセス:**
    お使いのブラウザで、編集したいページのURL末尾に `?update` を付けます。

    **例:**
    `https://www.example.com/service/?update`

2.  **ログイン:**
    まだログインしていない場合は、ログイン画面が表示されます。メールアドレスとパスワードを入力してログインしてください。
    すでにログイン済みの場合は、直接Webflowの編集画面が開きます。

## 3. 編集できる状態の目印

Content editor roleで開けている場合、編集可能なテキスト、画像、リンクにマウスを合わせると編集用のアイコンやアウトラインが表示されます。

![Webflow編集画面のツールバー](../../../assets/captures/editor-toolbar.svg)
*※画像はイメージです。*

編集アイコンが表示されない場合は、ログインしているメールアドレス、Site role、編集対象ページ、編集不可に設定された要素ではないかを確認してください。

---

**次のステップ:**
無事にWebflowを開くことができましたね。次はいよいよ、Content editor roleで「[No.10](/02-editor/02-edit-text/) サイトの文字を書き換える方法」を実践してみましょう。
