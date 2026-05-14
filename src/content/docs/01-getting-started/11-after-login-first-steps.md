---
title: "ログイン直後に押すもの・押さないもの"
description: "Webflowにログインした直後、どのボタンを押せばよいか、どの操作を避けるべきかを初心者向けに整理します。"
sidebar:
  order: 11
  label: "ログイン直後の最初の操作"
---

> 旧マニュアル番号: なし

Webflowにログインした直後は、Dashboardにサイトのサムネイルや複数のボタンが表示されます。初めての方は、まず <strong>Content editor roleでWebflowを開く</strong> ことだけ覚えておけば大丈夫です。

## 最初に押すもの

| やりたいこと | 押すもの |
| --- | --- |
| 文章を直したい | Open in Webflow / Content editing |
| 画像を差し替えたい | Open in Webflow / Content editing |
| ボタンのリンク先を変えたい | Open in Webflow / Content editing |
| ブログやお知らせを投稿したい | CMS / Collections |
| 公開前に画面を確認したい | Preview |

通常の更新作業は、対象サイトのサムネイルにカーソルを合わせてWebflowを開き、Content editor roleで編集します。公開サイトのURL末尾に `?update` を付けて編集画面へ入る方法もあります。

## すぐに押さないもの

| 表示 | すぐに押さない理由 |
| --- | --- |
| Designer | レイアウトや構造を変更できるため、通常更新では不要です |
| Delete | サイトやデータを削除する操作につながる可能性があります |
| Archive | 記事や項目が表示されなくなる場合があります |
| Transfer | サイトの所有権や管理場所に関わる操作です |
| Billing / Plans | 契約や支払いに関わる画面です |

## 迷った時の判断

- 文章・画像・リンクの更新なら <strong>Content editor role</strong>。
- ブログ・お知らせなら <strong>CMS</strong> または <strong>Collections</strong>。
- デザインやレイアウトの変更なら、作業前にIGNITEへ確認。
- 公開に関わるボタンを押す前に、変更内容を確認。

## Dashboardで見るポイント

Dashboardは、Webflow内のサイト一覧です。複数のWorkspaceに参加している場合は、左上のWorkspace名を切り替えると別のサイト一覧が表示されることがあります。

対象サイトが見つからない場合は、次を確認してください。

- 招待されたメールアドレスでログインしているか
- 正しいWorkspaceを開いているか
- サイト名が制作時の仮名になっていないか
- 権限がContent editor、Marketer、または必要なSite roleになっているか

## 次に進む

実際の画面構成は [No.6 管理画面（ダッシュボード）の基本的な見方](/01-getting-started/06-dashboard-overview/) で確認できます。Webflowを開いた後は [Content Editor入門](/02-editor/00-editor-complete-guide/) に進んでください。
