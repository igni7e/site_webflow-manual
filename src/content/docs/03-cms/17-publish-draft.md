---
title: "C-18. 下書きした記事を「公開」する方法"
description: "クライアント向けWebflow更新マニュアル：下書きした記事を「公開」する方法"
sidebar:
  order: 17
  label: "C-18. 下書きした記事を「公開」する方法"
---


<!-- body-callout:start -->
:::caution[公開前チェック]
Publishする前に、公開先ドメイン、変更したページ、スマートフォン表示、リンク先を確認します。公開後は一般の閲覧者に見えるため、少しでも不安があればスクリーンショットを撮って確認してから進めます。
:::
<!-- body-callout:end -->


「下書き（Draft）」として保存しておいた記事が完成し、いよいよサイトに公開する準備が整いました。このマニュアルでは、下書き記事を本番のサイトに反映させるための「公開」手順を解説します。

---

## 1. 下書き記事を公開する流れ

1.  <strong>CMS管理画面で、公開したい下書き記事を探す</strong>
2.  <strong>記事を開いて、最終確認をする</strong>
3.  <strong>「Publish」ボタンを押す</strong>

## 2. 操作手順の詳細

1.  <strong>CMS管理画面を開く:</strong>
    WebflowのCMSを開き、目的の記事一覧（例: `お知らせ`）を選択して、記事一覧画面に移動します。

2.  <strong>公開したい下書き記事を探す:</strong>
    記事一覧の中から、公開したい記事を探します。ステータスが「<strong>Draft</strong>」になっているものが下書き記事です。目的の記事をクリックして、編集パネルを開きます。

    :::note[キャプチャー指示]
    撮影する画面: CMS item一覧でDraft記事を探している画面。
    保存ファイル名: `c-25-draft-item-before-publish.png`
    撮影直前の状態: 対象Collectionの記事一覧を開き、Draft statusのitemが見えている状態。
    必ず写すもの: Draft status、対象item、Collection名、検索欄または一覧UI。
    写さないもの: 未公開本文、個人情報、社外秘タイトル、他社情報。
    この画像で読者に確認してほしいポイント: 公開する前に、対象itemがDraftであることを一覧で確認する場所。
    :::

3.  <strong>内容の最終チェック:</strong>
    公開する前に、誤字脱字はないか、画像やリンクの設定は正しいかなど、記事の内容を最後にもう一度見直しましょう。

4.  <strong>公開日を確認・設定:</strong>
    「公開日（Published On）」のフィールドを確認します。もし公開日を「今」にしたい場合は、日付や時刻を現在の日時に設定してください。

5.  <strong>「Publish」ボタンをクリック:</strong>
    編集パネルの右下にある、青い<strong>「Publish」</strong>（公開する）ボタンをクリックします。

    ![下書き保存・公開操作](../../../assets/captures/manual/c-07-save-draft-and-publish.png)

    :::note[キャプチャー指示]
    撮影する画面: Draft itemの編集画面でPublishまたはPublish optionsが見えている画面。
    保存ファイル名: `c-26-draft-item-publish-options.png`
    撮影直前の状態: 内容確認後、Publish実行前で止め、Publish optionsを開ける状態。
    必ず写すもの: Publish、Publish options、item名、Draft status。
    写さないもの: 未公開本文、個人情報、社外秘画像、他社情報。
    この画像で読者に確認してほしいポイント: Draftから公開する時に押すボタンと、公開オプションの位置。
    :::

6.  <strong>公開の確認:</strong>
    クリックすると、「`Publish 1 item`」のような確認メッセージが表示されます。問題がなければ、もう一度「<strong>Publish now</strong>」ボタンをクリックします。

    :::note[キャプチャー指示]
    撮影する画面: Publish now / Queue for next site publish / Scheduleなどの公開オプションが見えている画面。
    保存ファイル名: `c-27-publish-now-queue-options.png`
    撮影直前の状態: Publish optionsを開き、まだ公開を実行していない状態。
    必ず写すもの: Publish now、Queue for next site publish、Scheduleがあればその選択肢、Cancelできる状態。
    写さないもの: 未公開本文、個人情報、社外秘タイトル、他社情報。
    この画像で読者に確認してほしいポイント: 今すぐ公開するのか、次回Site publishに回すのかを選ぶ場所。
    :::

7.  <strong>公開完了:</strong>
    「Published successfully!」というメッセージが表示されれば、公開は成功です。CMSの記事一覧画面に戻ると、該当記事のステータスが「<strong>Published</strong>」に変わっているはずです。

## 3. 公開後の確認

操作が完了したら、必ず実際のWebサイトにアクセスし、以下の点を確認しましょう。

-   記事一覧ページに、新しい記事が意図した通りに表示されているか？
-   記事の詳細ページの内容は、正しく表示されているか？
-   リンクや画像の表示は問題ないか？

もし変更が反映されていないように見える場合は、[「変更を保存したのに、サイトに反映されません！」なぜ？（キャッシュ解説）](/06-troubleshooting/01-cache-not-reflecting/)で解説する「キャッシュ」が影響している可能性があります。ブラウザのスーパーリロード（`Ctrl+F5` / `Cmd+Shift+R`）を試してみてください。

---

<strong>次のステップ:</strong>
これで新規記事の作成から公開までの一連の流れが完了しました。次は、すでに公開されている記事の内容を修正したい場合の[一度公開した記事を「修正」する方法](/03-cms/18-edit-published/)です。
