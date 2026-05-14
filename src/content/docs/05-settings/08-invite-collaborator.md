---
title: "Webflowの共同編集者を招待する"
description: "クライアント向けWebflow更新マニュアル：Content editor roleなどのチームメンバー権限を招待・管理する方法"
sidebar:
  order: 8
  label: "共同編集者を招待する"
---

> 新規追加（標準スコープ補完）

社内で複数人がサイトを更新する場合、メンバーごとにWebflowのSeatとSite roleを割り当てます。これにより、誰がいつ編集したか、誰が公開できるかを管理できます。

---

## 1. 編集権限の種類

Webflowでは、Workspace roleとSite roleによってできることが変わります。日常運用でよく使うSite roleは次の通りです。

| 権限 | できること | 想定ユーザー |
|---|---|---|
| **Content editor** | テキスト、画像、リンク、CMS itemを更新 | クライアントの運用担当者 |
| **Marketer** | コンポーネントを使ったページ作成やコンテンツ更新 | マーケティング担当者 |
| **Reviewer** | 閲覧、コメント、レビュー | 承認担当者 |
| **Designer** | レイアウト、スタイル、構造の編集 | 制作会社・上級担当者 |
| **Site manager** | サイト設定、権限、公開、契約に近い管理 | 管理者 |

> **ヒント**: 通常のクライアント運用は **Content editor** が基本です。ページ制作まで任せる場合は Marketer、確認だけなら Reviewer を検討します。DesignerやSite managerは影響範囲が大きいため、必要な人だけに限定します。

## 2. Content editorを招待する手順

1. Webflowにログインし、WorkspaceのTeam settingsまたは対象サイトのSite accessを開きます。
2. **Invite member** または **Invite client** を選びます。
3. 招待相手のメールアドレスを入力します。
4. SeatとSite roleで **Content editor** を選びます。
5. 必要に応じて **Can publish** をオンまたはオフにします。
6. 内容を確認して招待を送信します。

招待された相手には Webflow から招待メールが届きます。受信側の操作は「招待メールを確認しよう」と同じ流れです。

## 3. メンバーを削除・権限変更する手順

1. WorkspaceのTeam settingsまたは対象サイトのSite accessを開きます。
2. 対象メンバーを選びます。
3. Site role、Site access、Can publishを見直します。
4. 不要なメンバーはRemoveします。

退職者など、サイト編集権限を持たせるべきでないメンバーは **必ず削除** しましょう。

## 4. Seatと人数の考え方

2026年現在、Legacy Editorは廃止に向けて移行中です。既存のLegacy Editorユーザーは、Limited seatまたはClient seatに移行され、Content editor roleが割り当てられる流れです。

- Client seatは、フリーランサー・代理店向けWorkspaceでクライアントに付与するSeatです。
- Limited seatは、Content editorやMarketerなど限定的な役割を付与するSeatです。
- 招待できる人数や料金はWorkspace planによって変わります。

> **ヒント**: 人数上限や料金は変更されるため、招待前にWebflow公式の最新プランとWorkspace設定を確認してください。

## 5. 招待時のベストプラクティス

- **個人の業務メールアドレス** を使う（共有メールは避ける）
- **退職時は速やかに削除**
- **本当に必要なメンバーのみ** に絞る
- 通常更新は **Content editor** を基本にする
- 公開権限が不要な人は **Can publishをオフ** にする
- DesignerやSite managerは必要な人だけに限定する

## 6. よくある質問 (Q&A)

Q. 招待メールが相手に届きません。
A. 迷惑メールフォルダを確認してもらってください。それでも届かない場合は、Team settingsまたはSite accessから再送してください。

Q. 招待した相手のメールアドレスを変更したいです。
A. 一度 **Remove して、新しいアドレスで再招待** してください。直接の変更機能はありません。

Q. 制作会社（IGNITE）の担当者は Designer 権限を持っていますか？
A. サイトのメンテナンス・改修作業のために、必要に応じてDesignerまたは管理権限を保持します。運用担当者には、作業範囲に応じてContent editor、Marketer、ReviewerなどのSite roleを割り当てます。

---

**次のステップ:**
独自ドメインがちゃんと接続されているか確認する方法を学びましょう → 「独自ドメインの接続状態を確認する」
