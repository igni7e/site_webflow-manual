---
title: "B-2. Content Editor（最新版）でWebflowを開く方法"
description: "クライアント向けWebflow更新マニュアル：最新版のContent editor roleでWebflowを開く方法"
sidebar:
  order: 2
  label: "B-2. Content Editor（最新版）でWebflowを開く方法"
---

:::tip[通常はこちらを使います]
現在のWebflowでは、Content editor roleとしてcanvasを開き、デザインを触らずにコンテンツだけを更新する流れが推奨されています。日常的な文字・画像・リンクの更新は、この最新版の手順を使ってください。
:::

![Dashboard上のOpen in Webflow入口](../../../assets/captures/manual/a-02-site-card-actions.png)

ここからは、実際のサイト更新作業で最もよく使う <strong>Content editor roleでの開き方</strong> について解説します。

## 1. Dashboardから開く

ログイン後の最初の画面である「Dashboard」から対象サイトを開く、最も基本的な方法です。

1. <strong>Webflowにログイン:</strong>
   [作成したアカウントで初めてサイトにログインする方法](/01-getting-started/03-first-login/)で解説した手順で、まずはWebflowにログインします。

2. <strong>Dashboardでサイトを選択:</strong>
   ログインすると、編集権限のあるサイトが一覧表示されたDashboardが開きます。目的のサイトを探します。

3. <strong>編集用の入口をクリック:</strong>
   「Open in Webflow」または制作担当者から案内された編集用ボタンをクリックします。Content editor roleが付与されている場合、デザイン編集ではなくコンテンツ編集に必要な範囲でWebflowを開けます。

4. <strong>Webflowのcanvasでサイトが開く:</strong>
   サイトの見た目を確認しながら、編集可能なテキスト、画像、リンク、CMSコンテンツを更新できます。

:::note[キャプチャー指示]
撮影する画面: 最新版のContent editor roleでサイトを開いた直後のcanvas画面。
保存ファイル名: `b-08-content-editor-latest-canvas.png`
撮影直前の状態: Dashboardからサイトを開き、ロード完了後に編集可能なページが表示されている状態。
必ず写すもの: 最新UIであることが分かる上部または周辺UI、編集可能なページ、対象サイト名。
写さないもの: 未公開ページ、個人情報、通知、他社サイト情報。
:::

## 2. `?update` で直接開く

毎回Dashboardを経由せず、公開サイトの該当ページから直接Content editor roleの編集画面へ入る方法です。

1. <strong>専用URLにアクセス:</strong>
   お使いのブラウザで、編集したいページのURL末尾に `?update` を付けます。

   <strong>例:</strong>
   `https://www.example.com/service/?update`

2. <strong>ログイン:</strong>
   まだログインしていない場合は、ログイン画面が表示されます。メールアドレスとパスワードを入力してログインしてください。すでにログイン済みの場合は、直接Webflowの編集画面が開きます。

## 3. 編集できる状態の目印

Content editor roleで開けている場合、編集可能なテキスト、画像、リンクにマウスを合わせると編集用のアイコンやアウトラインが表示されます。

編集アイコンが表示されない場合は、ログインしているメールアドレス、Site role、編集対象ページ、編集不可に設定された要素ではないかを確認してください。

:::note[旧版の画面が表示される場合]
Dashboard上に「Open Editor (Legacy)」が表示される場合は、旧バージョンの入口です。その場合は [B-1. Content Editor（旧バージョン）でWebflowを開く方法](/02-editor/01-open-legacy-editor/) を確認してください。
:::

<strong>次のステップ:</strong>
無事にWebflowを開くことができたら、[エディターでサイトの文字を書き換える方法](/02-editor/03-edit-text/) に進みましょう。
