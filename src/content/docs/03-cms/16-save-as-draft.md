---
title: "C-17. 書いた記事を「下書き」で保存する方法"
description: "クライアント向けWebflow更新マニュアル：書いた記事を「下書き」で保存する方法"
sidebar:
  order: 16
  label: "C-17. 書いた記事を「下書き」で保存する方法"
---


<!-- body-callout:start -->
:::tip[下書きで確認]
CMS記事は、いきなり公開せず下書き状態でタイトル、本文、画像、リンク、公開日を確認します。特に一覧ページと詳細ページの両方で見え方を確認すると安心です。
:::
<!-- body-callout:end -->

![Webflow公式: CMS auto-save](https://cdn.prod.website-files.com/687e8d1b96312cc631cafec7/68cc49bba84b934bf98711aa_EHbEQwnDfRxN1-a2uTJAyomnc9Xl2tFSoa-5VfcU8wg.webp)

:::note[公式画像]
WebflowではCMS編集の保存・公開まわりのUIが継続的に改善されています。実際のBooost画面では、表示されるボタン名や公開状態を確認してから操作してください。
:::


記事を作成している途中で作業を中断したい時や、まだ公開する段階ではないけれど、書いた内容を保存しておきたい場合に使うのが「下書き（Draft）」保存機能です。

---

## 1. 下書き保存とは？

-   <strong>サイトには公開されない:</strong> 下書き状態で保存された記事は、管理者や編集者だけがCMSの管理画面から見ることができ、一般のサイト訪問者には表示されません。
-   <strong>いつでも編集を再開できる:</strong> 保存した下書きは、後からいつでも開いて編集を再開することができます。
-   <strong>複数人でのレビューに便利:</strong> 記事を公開する前に、他の担当者に内容を確認してもらう（校正・レビュー）といった使い方ができます。

## 2. 記事を下書きで保存する手順

### 新規記事の場合

1.  <strong>記事のコンテンツを入力:</strong>
    タイトルや本文など、保存しておきたい内容をCMSの入力フォームに入力します。

2.  <strong>「Save as Draft」をクリック:</strong>
    編集パネルの右下を見てください。青い「Create」や「Publish」ボタンの隣に、通常は<strong>「Save as Draft」</strong>というボタンがあります。これをクリックします。

    ![下書き保存・公開操作](../../../assets/captures/manual/c-07-save-draft-and-publish.png)

    :::note[キャプチャー指示]
    撮影する画面: CMS item編集画面でSave as Draftが見えている画面。
    保存ファイル名: `c-22-save-as-draft-button-closeup.png`
    撮影直前の状態: CMS itemの入力後、Save as Draftを押す直前で止める。
    必ず写すもの: Save as Draft、PublishまたはCreate、item名、Draftにする対象だと分かる見出し。
    写さないもの: 未公開本文、個人情報、社外秘画像、他社情報。
    この画像で読者に確認してほしいポイント: 未完成の記事はPublishではなくSave as Draftを選ぶこと。
    :::

3.  <strong>下書き保存完了:</strong>
    クリックすると、記事が下書きとして保存され、CMSの記事一覧画面に戻ります。一覧画面では、その記事のステータスが「<strong>Draft</strong>」と表示されているはずです。

    :::note[キャプチャー指示]
    撮影する画面: CMS item一覧で、保存した記事のstatusがDraftになっている画面。
    保存ファイル名: `c-23-draft-status-in-item-list.png`
    撮影直前の状態: Save as Draft後、CMS item一覧に戻り、対象itemのDraft表示が見えている状態。
    必ず写すもの: 対象item名、Draft status、Collection名、一覧画面であることが分かるUI。
    写さないもの: 未公開本文、個人情報、社外秘タイトル、他社情報。
    この画像で読者に確認してほしいポイント: Draftは管理画面には残るが、公開サイトには出ない状態であること。
    :::

### 公開済みの記事を編集している場合

一度公開した記事を編集している途中で、その変更内容をまだ公開したくない場合は、編集パネルの右上にある「<strong>Save</strong>」ボタンをクリックします。これにより、変更内容は下書きとして保存されますが、<strong>サイト上で公開されているのは変更前のバージョンのまま</strong>となります。

:::note[キャプチャー指示]
撮影する画面: 公開済みCMS itemを編集し、未公開の変更があることが分かるstatusまたはPublish options周辺。
保存ファイル名: `c-24-published-item-draft-changes.png`
撮影直前の状態: Published itemを編集後、変更を公開せずにstatusやPublish optionsを確認している状態。
必ず写すもの: PublishedまたはDraft changesのstatus、Publish options、item名。
写さないもの: 未公開本文、個人情報、社外秘タイトル、他社情報。
この画像で読者に確認してほしいポイント: 公開済み記事を編集しても、変更内容は明示的にPublishするまで公開サイトへ出ないこと。
:::

## 3. 下書き記事の注意点

-   <strong>公開日を設定していても公開されない:</strong> たとえ公開日を過去の日付に設定していても、ステータスが「Draft」である限り、その記事がサイト上に表示されることはありません。
-   <strong>下書きのまま放置しない:</strong> 下書き機能は便利ですが、公開するつもりの記事をいつまでも下書きのままにしておくと、情報発信の機会を逃してしまいます。定期的にCMS管理画面を確認し、不要な下書きは削除するか、完成させて公開するようにしましょう。

---

<strong>次のステップ:</strong>
下書きの保存方法がわかりましたね。それでは、完成した下書きをいよいよ世に出すための[下書きした記事を「公開」する方法](/03-cms/17-publish-draft/)に進みましょう。

![下書きから公開までの図解](../../../assets/ai-diagrams/manual/cms-publish-status-options.png)

:::note[図解の見方]
今どの状態かを確認してから操作します。
:::
