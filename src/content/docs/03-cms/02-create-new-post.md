---
title: "C-3. 新しい「お知らせ（ブログ記事）」を追加する方法"
description: "クライアント向けWebflow更新マニュアル：新しい「お知らせ（ブログ記事）」を追加する方法"
sidebar:
  order: 2
  label: "C-3. 新しい「お知らせ（ブログ記事）」を追加する方法"
---


<!-- body-callout:start -->
:::tip[下書きで確認]
CMS記事は、いきなり公開せず下書き状態でタイトル、本文、画像、リンク、公開日を確認します。特に一覧ページと詳細ページの両方で見え方を確認すると安心です。
:::
<!-- body-callout:end -->


CMSの管理画面にアクセスできるようになったら、次はいよいよ新しい記事を追加してみましょう。ここでは例として「お知らせ」を新規作成する手順を解説しますが、「ブログ記事」や「導入事例」など、他のCMSコンテンツでも基本的な流れは同じです。

![Webflow公式: Next-gen CMS](https://cdn.prod.website-files.com/687e8d1b96312cc631cafec7/69d6ae8aa741ebac229650fc_NEXTGEN%20CMS_BlogInline_1280x720.png)

:::note[公式画像]
上の画像はWebflow公式UpdatesのNext-gen CMSに関する画像です。実際のBooost画面では、Collection名や入力Fieldが異なるため、画面上の項目名を確認してから入力します。
:::

---

## 1. 新規記事追加の基本ステップ

1.  <strong>CMS管理画面を開く</strong>
2.  <strong>「New」ボタンをクリックする</strong>
3.  <strong>記事の各項目（タイトル、本文など）を入力する</strong>
4.  <strong>記事を保存・公開する</strong>

## 2. 作成前に用意するもの

記事作成画面を開く前に、次の素材を先に用意しておくと作業が止まりにくくなります。

- 記事タイトル
- 本文原稿
- アイキャッチ画像またはサムネイル画像
- カテゴリー
- 公開日
- リンク先URL
- 本文に入れる画像やYouTube URL
- 公開前に確認する担当者

下書きがまだ固まっていない場合は、Webflow上で直接書き始めるより、Google Docsなどで先に原稿を作ってから貼り付ける方が安全です。

## 3. 操作手順の詳細

1.  <strong>CMS管理画面を開く:</strong>
    [「お知らせ」や「ブログ」はどこで管理してるの？](/03-cms/01-where-is-cms/)の手順に従って、WebflowのCMSから追加したいコンテンツ（例: `お知らせ`）を選択します。すると、そのコンテンツの記事一覧画面が表示されます。

    :::note[キャプチャー指示]
    撮影する画面: 対象Collectionの記事一覧画面。
    保存ファイル名: `c-19-new-item-from-collection-list.png`
    撮影直前の状態: CMSで対象Collectionを選択し、Newボタンと既存item一覧が見えている状態。
    必ず写すもの: Collection名、Newボタン、検索欄、既存itemのstatus表示。
    写さないもの: 未公開記事名、個人情報、社外秘タイトル、他社情報。
    この画像で読者に確認してほしいポイント: 新規記事は対象Collectionを選んでからNewボタンで作ること。
    :::

2.  <strong>「New」ボタンをクリック:</strong>
    画面の右上を見てください。<strong>「+ New [項目名]」</strong>（例: `+ New Announcement`）という青いボタンがあります。これが新規追加ボタンです。このボタンをクリックします。

    ![記事一覧画面](../../../assets/captures/manual/c-02-collection-items-list.png)

    ![新規CMS item入力フォーム](../../../assets/captures/manual/c-03-new-cms-item-form.png)

    :::note[キャプチャー差し込み位置]
    撮影する画面: CMS item作成フォーム、またはNext-gen CMSの公式画像。
    保存ファイル名: `b-33-official-next-gen-cms.png`
    撮影直前の状態: 新規CMS itemフォームが開き、主要Fieldが見えている状態。
    必ず写すもの: New item、Title/Name、Slug、主要Field、Save / Create / Publish周辺。
    写さないもの: 未公開本文、個人情報、社外秘画像、他社情報。
    :::


3.  <strong>記事の入力フォームが開く:</strong>
    クリックすると、新しい記事の情報を入力するための専用フォーム（編集パネル）が画面右側に表示されます。ここには、「タイトル」「公開日」「本文」など、あらかじめ制作会社が設定した項目が並んでいます。

    :::note[キャプチャー指示]
    撮影する画面: 新規CMS itemの入力フォーム全体。
    保存ファイル名: `c-20-new-cms-item-fields-overview.png`
    撮影直前の状態: New itemフォームを開き、Title / Name、Slug、Summary、Thumbnail、Bodyなど主要Fieldが見えている状態。
    必ず写すもの: TitleまたはName、Slug、主要Field、Save as Draft、PublishまたはCreate周辺。
    写さないもの: 未公開本文、個人情報、社外秘画像、他社情報。
    この画像で読者に確認してほしいポイント: CMS記事はページを直接作るのではなく、決まったFieldに入力して作ること。
    :::

4.  <strong>各項目を埋めていく:</strong>
    このフォームの上から順に、必要な情報を入力したり、設定したりしていきます。
    具体的な入力方法については、次のマニュアルから一つずつ詳しく解説します。
    -   [記事の「タイトル」を入力する](/03-cms/03-post-title/)
    -   [記事の「アイキャッチ画像」を設定する方法](/03-cms/04-thumbnail-image/)
    -   [記事の「カテゴリー」を選択する方法](/03-cms/05-post-category/)
    -   [記事の「本文」を書き込む](/03-cms/06-write-body/)
    など。

5.  <strong>記事を保存または公開する:</strong>
    すべての項目を入力し終えたら、最後にこの記事をどうするかを決めます。
    -   <strong>すぐに公開したい場合:</strong> 「Publish」ボタンをクリックします。（→ [下書きした記事を公開する方法](/03-cms/17-publish-draft/)）
    -   <strong>一旦下書きとして保存したい場合:</strong> 「Save as Draft」ボタンをクリックします。（→ [下書きで保存する方法](/03-cms/16-save-as-draft/)）
    -   <strong>未来の日時で公開を予約したい場合:</strong> 公開日時を設定して「Schedule」ボタンをクリックします。（→ [未来の日時で公開を予約する方法](/03-cms/15-schedule-publish/)）

    :::note[キャプチャー指示]
    撮影する画面: CMS itemフォーム下部または上部の保存・公開ボタン周辺。
    保存ファイル名: `c-21-cms-save-publish-options.png`
    撮影直前の状態: 入力後、Save as Draft、Publish、Scheduleなどの操作ボタンが見えている状態。実行前で止める。
    必ず写すもの: Save as Draft、Publish、ScheduleまたはPublish options、現在のCMS item名。
    写さないもの: 未公開本文、個人情報、社外秘画像、他社情報。
    この画像で読者に確認してほしいポイント: 下書き、即時公開、予約公開の入口は同じCMS item画面にあること。
    :::

## 4. 保存方法の選び方

| 状況 | 選ぶ操作 | 理由 |
| --- | --- | --- |
| まだ内容確認中 | `Save as Draft` | 公開されず、あとで編集できます |
| 公開日時が決まっている | `Schedule` | 指定した日時に公開できます |
| 今すぐ公開してよい | `Publish` | 公開サイトに反映されます |

迷った場合は、まず `Save as Draft` を選んでください。公開は、内容確認が終わってからでも問題ありません。

## 5. 公開前に必ず見る場所

CMS記事は、1つの記事ページだけでなく複数の場所に表示されることがあります。

- 記事の詳細ページ
- 記事一覧ページ
- トップページの最新情報欄
- 関連記事やカテゴリー一覧
- SNSで共有した時の表示

公開後に「一覧には出ているが詳細ページが変」「トップページの表示だけ崩れている」といったことが起きないよう、複数箇所で確認してください。

## 6. まとめ

新しい記事を追加する流れは、<strong>「CMS管理画面へ行く → 新規追加ボタンを押す → フォームを埋める → 保存/公開する」</strong>というシンプルなものです。まずはこの大きな流れを掴んでください。

---

<strong>次のステップ:</strong>
記事の入力フォームを開くところまでできました。次からは、各入力項目の詳細な設定方法を見ていきましょう。まずは最も基本の「[記事の「タイトル」を入力する](/03-cms/03-post-title/)」を入力する」です。

![CMS item作成フローの図解](../../../assets/ai-diagrams/manual/cms-item-creation-flow.png)

:::note[図解の見方]
まず下書き保存し、公開前に確認します。
:::
