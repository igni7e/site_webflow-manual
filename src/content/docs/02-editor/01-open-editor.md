---
title: "【基本】Content editor roleでWebflowを開く方法"
description: "クライアント向けWebflow更新マニュアル：Content editor roleでWebflowを開く方法"
sidebar:
  order: 1
  label: "Content editor roleで開く"
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に以下のキャプチャーを入れてください。
- B-01: `src/assets/captures/manual/b-01-open-content-editor.png`。Content editor roleで対象サイトを開く入口。Dashboardから編集画面へ入るボタンが分かる状態
- B-02: `src/assets/captures/manual/b-02-editor-canvas-opened.png`。Content editorでサイトを開いた直後。上部バー、ページ画面、編集可能な雰囲気が分かる状態

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::tip[編集の基本]
Content editor roleでは、文章、画像、リンクなどの内容を安全に更新できます。レイアウトやデザインを変えたい時は、無理に触らずDesigner操作が必要か確認してください。
:::
<!-- body-callout:end -->


> 旧マニュアル番号: [No.9](/02-editor/01-open-editor/)

ここからは、実際のサイト更新作業で最もよく使う <strong>Content editor roleでの開き方</strong> について解説します。

従来のLegacy Editorは2026年8月4日から利用できなくなる予定です。現在は、Webflowの中でContent editor roleとしてcanvasを開き、デザインを触らずにコンテンツだけを更新する流れが推奨されています。

---

## 1. 方法1：ダッシュボードから開く（基本）

ログイン後の最初の画面である「Dashboard」から対象サイトを開く、最も基本的な方法です。

1.  <strong>Webflowにログイン:</strong>
    「[No.3](/01-getting-started/03-first-login/)」で解説した手順で、まずはWebflowにログインします。

2.  <strong>ダッシュボードでサイトを選択:</strong>
    ログインすると、編集権限のあるサイトが一覧表示された「ダッシュボード」が開きます。目的のサイトのサムネイル画像の上に、マウスカーソルを合わせます。

3.  <strong>「Open in Webflow」または案内された編集用ボタンをクリック:</strong>
    カーソルを合わせると表示されるメニューの中から、制作担当者から案内された編集用ボタンをクリックします。Content editor roleが付与されている場合、デザイン編集ではなくコンテンツ編集に必要な範囲でWebflowを開けます。

    :::note[キャプチャー差し込み位置]
    ここには「ダッシュボードからWebflowを開く」が分かる実画面キャプチャーを入れてください。ページ上部のキャプチャー指示にある保存ファイル名へ差し替えます。
    :::

4.  <strong>Webflowのcanvasでサイトが開く:</strong>
    サイトの見た目を確認しながら、編集可能なテキスト、画像、リンク、CMSコンテンツを更新できます。

## 2. 方法2：`?update` で直接開く

毎回Dashboardを経由せず、公開サイトの該当ページから直接Content editor roleの編集画面へ入る方法です。

1.  <strong>専用URLにアクセス:</strong>
    お使いのブラウザで、編集したいページのURL末尾に `?update` を付けます。

    <strong>例:</strong>
    `https://www.example.com/service/?update`

2.  <strong>ログイン:</strong>
    まだログインしていない場合は、ログイン画面が表示されます。メールアドレスとパスワードを入力してログインしてください。
    すでにログイン済みの場合は、直接Webflowの編集画面が開きます。

## 3. 編集できる状態の目印

Content editor roleで開けている場合、編集可能なテキスト、画像、リンクにマウスを合わせると編集用のアイコンやアウトラインが表示されます。

:::note[キャプチャー差し込み位置]
ここには「Webflow編集画面のツールバー」が分かる実画面キャプチャーを入れてください。ページ上部のキャプチャー指示にある保存ファイル名へ差し替えます。
:::

編集アイコンが表示されない場合は、ログインしているメールアドレス、Site role、編集対象ページ、編集不可に設定された要素ではないかを確認してください。

---

<strong>次のステップ:</strong>
無事にWebflowを開くことができましたね。次はいよいよ、Content editor roleで「[No.10](/02-editor/02-edit-text/) サイトの文字を書き換える方法」を実践してみましょう。
