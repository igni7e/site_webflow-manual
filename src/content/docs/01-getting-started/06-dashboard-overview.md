---
title: "管理画面（ダッシュボード）の基本的な見方"
description: "クライアント向けWebflow更新マニュアル：管理画面（ダッシュボード）の基本的な見方"
sidebar:
  order: 6
  label: "管理画面（ダッシュボード）の基本的な見方"
---


<!-- body-callout:start -->
:::tip[最初に見る場所]
迷った時は、まずDashboardで対象サイト名を確認します。似た名前のサイトやテスト環境がある場合は、編集前に正しいサイトか確認してから進めます。
:::
<!-- body-callout:end -->


Webflowにログインすると、最初に表示されるのが「ダッシュボード」です。ここからサイトの編集や設定など、様々な操作を開始します。このマニュアルでは、ダッシュボードの基本的な画面構成と各部の役割について解説します。

---

## 1. ダッシュボードの全体像

Webflowのダッシュボードは、あなたがアクセス権を持つサイトの一覧が表示される場所です。複数のサイトに関わっている場合は、ここに複数のサイトが並びます。

通常、クライアントとして招待された場合は、編集対象のサイトが1つだけ表示されているはずです。
*実画面例: Dashboardでは対象サイトのカードと、開くための操作メニューを確認します。*

<strong>ダッシュボードの主な構成要素:</strong>

- <strong>サイト一覧:</strong> 中央に、あなたが編集できるサイトのサムネイル画像が表示されます。
- <strong>サイト名:</strong> 各サイトのサムネイルの下に、サイト名が表示されます。
- <strong>（右上の）アカウント設定:</strong> 画面右上のアイコンから、ご自身のアカウント情報（名前やパスワードの変更など）を編集できます。
- <strong>（左上の）Webflowロゴ:</strong> Webflowのホーム画面に戻るためのロゴです。

## 2. サイトを選択して編集を開始する

サイトの更新作業を始めるには、このダッシュボードから目的のサイトを選択する必要があります。

1.  <strong>サイトを探す:</strong>
    ダッシュボードに表示されているサイトの中から、編集したいサイトを見つけます。

2.  <strong>サイトにカーソルを合わせる:</strong>
    サイトのサムネイル画像の上にマウスカーソルを合わせます。

3.  <strong>「Open in Webflow」または編集用ボタンをクリック:</strong>
    カーソルを合わせると、いくつかのボタンが表示されます。2026年現在は、Content editor roleのユーザーもWebflow内のcanvasで編集する流れが基本です。表示されるボタン名はサイトや権限によって異なりますが、制作担当者から案内された編集用ボタンを開いてください。

    ![Webflow Dashboardのサイト一覧](../../../assets/captures/manual/a-01-dashboard-site-list.png)

    ![対象サイトカードの操作メニュー](../../../assets/captures/manual/a-02-site-card-actions.png)

## 3. 最初に押すボタン早見表

ログイン直後に迷った場合は、次の表で判断してください。

| やりたいこと | 押すもの | 押さないもの |
| --- | --- | --- |
| 文章を直したい | Open in Webflow / Content editing | Designer |
| 画像を差し替えたい | Open in Webflow / Content editing | Designer |
| ブログやお知らせを追加したい | CMS / Collections | Delete、Archive |
| サイトの設定を確認したい | Site settings | Billing、Transfer |
| 公開前に見た目を確認したい | Preview | Publish |

より詳しい判断は [ログイン直後に押すもの・押さないもの](/01-getting-started/11-after-login-first-steps/) を確認してください。

## 4. 「Content editor role」と「Designer」

Webflowでは、役割によってできることが変わります。日常更新では、Content editor roleで作業するのが基本です。

- <strong>Content editor role（コンテンツ更新担当）:</strong>
  -   <strong>普段の更新作業で使うモードです。</strong>
  -   文字の修正、画像の差し替え、お知らせやブログの投稿など、日常的な更新はすべてこのモードで行います。
  -   デザインやレイアウトを直接変更できないように制限されているため、安全に作業できます。

- <strong>Designer（デザイナー）:</strong>
  -   サイトの構造やデザインそのものを編集する、より専門的なモードです。
  -   Webサイト制作会社がサイトを構築する際に使用します。
  -   <strong>基本的に、クライアント様がこのモードを操作する必要はありません。</strong> 誤って操作すると、サイトのレイアウトが崩れるなどのトラブルの原因となります。

## 5. まとめ

- <strong>ダッシュボードは、サイト編集の入り口。</strong>
- <strong>サイトを更新する時は、Content editor roleでWebflowを開く。</strong>
- <strong>「Designer」は専門家用なので、触らないようにする。</strong>

---

<strong>次のステップ:</strong>
ダッシュボードの役割が理解できたところで、次は「[Content editor roleとDesignerの違い](/01-getting-started/07-editor-vs-designer/)」で、この2つのモードの違いについて、さらに詳しく学んでいきましょう。
