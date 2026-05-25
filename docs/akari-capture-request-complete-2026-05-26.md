---
title: "Akariさん向け Booost追加キャプチャー完全版 2026-05-26"
description: "Booost向けWebflowマニュアルで未撮影のキャプチャーを、Akariさんへ依頼するための完全版リスト。"
sidebar:
  order: 3
---

# Akariさん向け Booost追加キャプチャー完全版 2026-05-26

## 目的

Booost向けWebflow更新マニュアルに差し込む追加キャプチャーを撮影するための依頼リストです。`src/assets/captures/manual/` に既に存在する撮影済み37枚は除外し、未撮影分だけをまとめています。

## 件数

- 依頼対象: 84枚
- P0: 59枚
- P1: 25枚

## 保存先

撮影した画像は以下に保存してください。

`src/assets/captures/manual/`

ファイル名は、この依頼書の `保存ファイル名` と完全一致させてください。

## 共通ルール

- Webflow画面を開いたら、すぐ撮らずに3〜5秒待ってください。
- `Loading...`、スピナー、白紙、画像未読込、スケルトンUIが残っている状態は撮らないでください。
- 個人名、メールアドレス、問い合わせ本文、未公開記事、顧客情報、請求情報、カード情報は写さないでください。
- 他社サイト名や不要なサイトカードが写る場合は、撮影前に画面を調整するか、撮影後にマスクしてください。
- 保存、公開、削除、復元、招待、アーカイブなどは実行せず、実行前の確認画面またはボタンが見える状態で止めてください。
- ボタンだけを拡大しすぎず、押す場所と周辺の文脈が同時に分かる構図にしてください。
- 画像サイズは横1280px前後を目安にしてください。
- Webflow公式画像を使う場合は、公式Help Centerまたは公式サイトの最新版Content Editor画像を優先してください。
- 公式画像を保存する場合も、ファイル名はこの依頼書の `保存ファイル名` と完全一致させてください。

## 進め方

まずP0を撮影してください。時間が余る場合のみP1もお願いします。

## A. はじめの一歩

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| A-04 | P1 | `a-04-invitation-and-login.png` | 招待メールまたはログイン画面 | 招待メールならAccept Invitation、ログイン画面ならEmail、Password、Forgot passwordが分かる状態。実メールは隠す。 |
| A-06 | P0 | `a-06-booost-workspace-overview.png` | BooostのWorkspace全体 | `Booost Workspace`、対象サイトカード、Dashboardであることが分かる構図。他サイトや個人情報は隠す。 |
| A-07 | P0 | `a-07-workspace-plan-members.png` | Workspace plan / Members | 現在のWorkspace plan、メンバー数、UpgradeやPlan関連の表示。請求情報やメールアドレスは隠す。 |
| A-08 | P0 | `a-08-site-plan-settings.png` | Site plan / Publishing設定 | 対象サイト名、Site settings、Site plan名または公開設定。カード情報や請求情報は写さない。 |
| A-09 | P0 | `a-09-members-and-permissions.png` | Membersと権限 | Invite/Add member、Role、Can publishなど権限判断に必要な列。氏名・メールは隠す。 |
| A-10 | P0 | `a-10-open-site-from-dashboard.png` | Dashboardからサイト修正画面に入る入口 | 対象サイトカード、Open in Webflow、SettingsまたはDesignerへの入口。他サイト名は隠す。 |
| A-11 | P0 | `a-11-workspace-selector-open.png` | Workspace selectorを開いた状態 | 現在選択中のWorkspace名、対象Workspace候補、切り替え場所。他社Workspace名やメールアドレスは隠す。 |
| A-12 | P0 | `a-12-site-card-entry-points.png` | 対象Site cardの入口一覧 | 対象Site名、Open / Content editor、Settings、Designerの位置関係。他サイト名は隠す。 |
| A-13 | P0 | `a-13-workspace-members-role-list.png` | Workspace MembersのRole一覧 | Members見出し、RoleまたはSeat列、人数表示。氏名・メールは隠す。 |
| A-14 | P0 | `a-14-workspace-plan-billing-warning.png` | Plan / Upgrade / Billing入口 | Plan名、UpgradeやBilling入口、請求に関わる画面だと分かる見出し。カード情報や料金明細は写さない。 |

## B. Content Editor / 作業別手順

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| B-07 | P1 | `b-07-discard-changes-confirm.png` | 変更破棄の確認画面 | Discard、Cancelなどの判断ボタンが見える状態。実際に破棄する直前で止める。 |
| B-08 | P0 | `b-08-content-editor-latest-canvas.png` | Content Editor（最新版）でサイトを開いた直後 | 最新版のContent editor roleとしてcanvasを開いた状態。旧Legacy Editorの下部バーではなく、最新UIで編集可能な状態が分かる構図にする。 |
| B-11 | P0 | `b-09-latest-content-editor-screen-guide.png` | 最新Content Editorの画面構成 | Webflow公式Help CenterのContent editor role説明画像、またはBooostサイトを最新版Content editor roleで開いたcanvas画面。canvas、上部バー、Pages/CMS/Assetsなどの入口、編集可能な要素の青いアウトラインまたは編集アイコンが分かる状態。 |
| B-12 | P0 | `b-12-official-content-editor-canvas.png` | 公式画像: Content editor roleのcanvas全体 | Webflow公式Help Centerまたは公式サイトの画像を利用。canvas、編集対象ページ、Content editor roleであることが分かるUI。Legacy Editorの古い下部バーだけの画像は避ける。 |
| B-13 | P0 | `b-13-official-content-editor-panels.png` | 公式画像: Pages / CMS / Assets / Settingsの入口 | Webflow公式Help CenterのContent editor role説明画像を利用。各panelの入口と位置関係が分かる画像にする。 |
| B-14 | P0 | `b-14-official-text-editing.png` | 公式画像: 文字編集のアウトラインまたはPencilアイコン | 編集対象テキスト、青いアウトライン、Pencilなどの編集アイコンが分かる公式画像。 |
| B-15 | P0 | `b-15-official-image-replace.png` | 公式画像: 画像差し替えの入口 | 対象画像、画像編集アイコン、AssetsまたはUploadに進める入口が分かる公式画像。 |
| B-16 | P0 | `b-16-official-link-editing.png` | 公式画像: リンク編集の入口 | Link設定、URL入力欄、新しいタブ設定などが分かる公式画像。 |
| B-17 | P0 | `b-17-official-publish-flow.png` | 公式画像: Publish前の確認画面 | Publishボタン、公開対象、公開前確認の文脈が分かる公式画像。 |
| B-18 | P1 | `b-18-official-update-shortcut.png` | 公式画像: `?update` で直接編集画面を開く導線 | 公式Help Centerの `?update` shortcut説明と整合する画像。ブラウザURL欄を写す場合は実サイトURLを公開可能なものにする。 |
| B-19 | P1 | `b-19-official-legacy-vs-content-editor.png` | 公式画像: Legacy Editorと最新版Content Editorの違い | 旧Legacy Editorと最新版Content Editorを混同しないように、比較説明に使える公式画像または公式ページの画像。 |
| B-20 | P1 | `b-20-official-cms-item-editing.png` | 公式画像: CMS itemを作成・編集する画面 | CMS fields、preview、publishの流れが分かる公式画像。 |
| B-21 | P1 | `b-21-official-seo-ogp-controls.png` | 公式画像: SEO / Open Graphを確認する画面 | Page title、Meta description、Open Graph設定などが分かる公式画像。 |
| B-22 | P1 | `b-22-official-content-role-permissions.png` | 公式画像: Content editor roleの権限・Publish権限 | Content editor role、Can publish、権限範囲の説明に使える公式画像。 |
| B-23 | P1 | `b-23-official-cms-overview.png` | 公式画像: CMS機能の概要 | Webflow公式CMSページ画像。CMSで構造化コンテンツを管理する全体像が分かる画像にする。 |
| B-24 | P1 | `b-24-official-cms-draft-publishing.png` | 公式画像: CMS下書き・公開ワークフロー | Webflow公式Updates画像。Draft changes、個別公開、公開前確認の文脈が分かる画像にする。 |
| B-25 | P1 | `b-25-official-cms-auto-save.png` | 公式画像: CMS自動保存 | Webflow公式Updates画像。CMS編集の保存・公開操作を説明できる画像にする。 |
| B-26 | P1 | `b-26-official-cms-bulk-publishing.png` | 公式画像: CMS一括公開・一括非公開 | Webflow公式Updates画像。複数CMS itemをまとめて扱う操作の注意喚起に使う。 |
| B-27 | P1 | `b-27-official-cms-item-creation.png` | 公式画像: CMS item作成改善 | Webflow公式Updates画像。CMS item作成や編集の流れを補助する画像にする。 |
| B-28 | P1 | `b-28-official-seo-overview.png` | 公式画像: SEO機能の概要 | Webflow公式SEOページ画像。SEO title、meta description、Open Graphの説明に使う。 |
| B-29 | P1 | `b-29-official-localization-overview.png` | 公式画像: Localization機能の概要 | Webflow公式Localizationページ画像。Localeや翻訳作業の全体像に使う。 |
| B-30 | P1 | `b-30-official-collaboration-overview.png` | 公式画像: チーム編集・コメント・権限 | Webflow公式Collaborationページ画像。Content editor role、コメント、権限の説明に使う。 |
| B-31 | P1 | `b-31-official-single-page-publishing.png` | 公式画像: 1ページだけPublishする考え方 | Webflow公式Single page publishing画像。Publish対象ページと公開先を確認する説明に使う。 |
| B-32 | P1 | `b-32-official-single-page-publishing-access.png` | 公式画像: 1ページ公開権限 | Webflow公式Single page publishing access画像。Role、Can publish、公開権限の説明に使う。 |
| B-33 | P1 | `b-33-official-next-gen-cms.png` | 公式画像: Next-gen CMSの概要 | Webflow公式Next-gen CMS画像。CMS item作成フォームや主要Fieldの説明に使う。 |
| B-34 | P1 | `b-34-official-publishing-permission-toggle.png` | 公式画像: Publish権限のON/OFF | Webflow公式Publishing permission toggle画像。Publish権限がない場合の説明に使う。 |
| B-35 | P1 | `b-35-official-preview-roles.png` | 公式画像: Preview role | Webflow公式Preview roles画像。公開前レビューや確認担当者の説明に使う。 |
| B-36 | P1 | `b-36-official-hosting-domain.png` | 公式画像: Hosting / Domain / SSLの概要 | Webflow公式Hosting画像。Domain、SSL、Publishing設定の説明に使う。 |
| B-37 | P1 | `b-37-official-security-permissions.png` | 公式画像: Securityと権限管理 | Webflow公式Security画像。権限不足や安全確認の説明に使う。 |
| B-38 | P1 | `b-38-official-analyze-seo-settings.png` | 公式画像: Analyze / 計測の概要 | Webflow公式Analyze画像。検索表示、計測、反映タイミングの説明に使う。 |
| B-39 | P1 | `b-39-official-designer-overview.png` | 公式画像: Designerの概要 | Webflow公式Design画像。Designerが高機能で慎重に扱う画面だと伝える説明に使う。 |
| B-40 | P0 | `work-00-dashboard-workspace-site-check.png` | 作業前のWorkspace / Site確認 | DashboardでWorkspace名と対象Site cardが同時に見える構図。他社Site名、通知、メールは隠す。 |
| B-41 | P0 | `work-00-content-editor-entry-check.png` | 作業前のContent editor入口確認 | 対象Site card、Content editor入口、DesignerやSettingsとの位置関係。通常更新の入口を説明できる状態にする。 |
| B-42 | P0 | `work-00-before-publish-target-check.png` | 作業前ページのPublish前確認 | Publishボタン、公開対象、公開先ドメイン、Cancelできる状態。実行前で止める。 |
| B-09 | P0 | `work-01-edit-text-open-site.png` | テキスト修正作業の開始画面 | 対象サイトカードからContent editor roleを開く直前。Workspace名、対象サイトカード、編集入口が分かる構図。 |
| B-10 | P0 | `work-02-replace-image-edit-icon.png` | 画像差し替えアイコン | 対象画像と編集アイコンが同時に見える状態。未公開画像や個人情報は写さない。 |
| B-43 | P0 | `work-01-editable-text-indicator.png` | テキスト編集可能表示 | Content editorで修正対象テキスト、青枠、鉛筆アイコンが見える状態。未公開情報は隠す。 |
| B-44 | P0 | `work-01-text-before-publish-review.png` | テキスト修正後のPublish前確認 | 修正後テキスト、Publishボタン、対象ページが分かる周辺UI。実行前で止める。 |
| B-45 | P0 | `work-01-site-access-role-check.png` | テキスト編集できない時の権限確認 | Site access / Members、Role、Can publish、Content editorなど。氏名・メールは隠す。 |

## C. CMS更新

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| C-11 | P0 | `c-11-category-dropdown-open.png` | Categoryフィールドのドロップダウン | `Category`、`Pick a Category...`、選択肢が見える状態。未公開記事名や本文は隠す。 |
| C-12 | P0 | `c-12-rich-text-list-icons.png` | Rich Textのリストアイコン | 選択中の本文、番号なしリスト、番号付きリストのアイコンが見える状態。 |
| C-13 | P0 | `c-13-archive-button-visible.png` | CMS一覧のArchiveボタン | 記事選択後、上部のArchiveボタンが見える状態。実行前に止める。 |
| C-14 | P0 | `work-03-update-post-cms-list.png` | CMS記事一覧から投稿を始める画面 | CMS/Collection名、記事一覧、Newボタン。未公開記事名は必要に応じて隠す。 |
| C-15 | P0 | `c-15-booost-cms-fields-overview.png` | Booost記事入力フィールド全体 | Title、Slug、Summary、Thumbnail、Bodyなど主要Fieldと、Save/Create/Publish周辺の操作ボタンが分かる状態。未公開本文や個人情報は隠す。 |
| C-16 | P0 | `c-16-cms-entry-with-sidebar.png` | CMS / Collections入口 | Content editorまたは編集画面でCMS / Collections入口、左メニュー、対象Site名が分かる状態。 |
| C-17 | P0 | `c-17-collection-list-select-target.png` | Collection一覧から対象を選ぶ画面 | Blog、News、お知らせなどのCollection名とCMS見出し。未公開記事名は写さない。 |
| C-18 | P0 | `c-18-cms-items-status-list.png` | CMS item一覧のstatus確認 | item一覧、Status列、Draft / Published表示、Newボタン、検索欄。社外秘タイトルは隠す。 |
| C-19 | P0 | `c-19-new-item-from-collection-list.png` | Collection一覧からNew itemを押す直前 | Collection名、Newボタン、検索欄、既存itemのstatus表示。 |
| C-20 | P0 | `c-20-new-cms-item-fields-overview.png` | 新規CMS itemのField全体 | Title / Name、Slug、主要Field、Save as Draft、Publish / Create周辺。未公開本文は隠す。 |
| C-21 | P0 | `c-21-cms-save-publish-options.png` | CMS itemの保存・公開ボタン | Save as Draft、Publish、ScheduleまたはPublish options、現在のCMS item名。実行前で止める。 |
| C-22 | P0 | `c-22-save-as-draft-button-closeup.png` | Save as Draftボタン | Save as Draft、Publish / Create、item名、Draft対象だと分かる見出し。 |
| C-23 | P0 | `c-23-draft-status-in-item-list.png` | Draft statusの一覧表示 | 対象item名、Draft status、Collection名、一覧UI。未公開本文や個人情報は隠す。 |
| C-24 | P0 | `c-24-published-item-draft-changes.png` | 公開済みitemの未公開変更 | PublishedまたはDraft changesのstatus、Publish options、item名。未公開本文は隠す。 |
| C-25 | P0 | `c-25-draft-item-before-publish.png` | Draft itemを公開前に探す画面 | Draft status、対象item、Collection名、検索欄または一覧UI。 |
| C-26 | P0 | `c-26-draft-item-publish-options.png` | Draft itemのPublish入口 | Publish、Publish options、item名、Draft status。実行前で止める。 |
| C-27 | P0 | `c-27-publish-now-queue-options.png` | Publish now / Queue選択肢 | Publish now、Queue for next site publish、Scheduleがあればその選択肢、Cancelできる状態。 |
| C-28 | P0 | `c-28-published-item-status-list.png` | Published itemの一覧表示 | Published status、対象item、Collection名、検索欄または一覧UI。 |
| C-29 | P0 | `c-29-published-item-update-options.png` | 公開済みitem編集後のPublish options | item名、Published / Draft changesのstatus、Publish now、Queue for next site publish。 |

## D. Designer

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| D-05 | P1 | `d-05-undo-and-unsaved-warning.png` | Undoまたは未保存変更の確認 | Undo / Redo、または保存せず終了する確認画面が見える状態。 |

## E. Locale翻訳

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| E-06 | P0 | `e-06-locale-publish-and-url.png` | Locale公開と公開URL確認 | Publishモーダル、公開対象Locale、公開後の `/en` などのURLが分かる状態。 |
| E-07 | P0 | `work-06-edit-locale-selector.png` | Locale selectorで対象言語を確認する画面 | Locale selector、現在のLocale、対象ページの見出しが分かる状態。 |

## F. 設定・フォーム・権限

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| F-06 | P0 | `work-04-edit-seo-settings.png` | 作業ベースSEO設定画面 | Title tag、Meta description、対象ページ名。APIキーや請求情報は写さない。 |
| F-07 | P0 | `work-05-check-forms-submissions.png` | 作業ベースForms送信内容確認画面 | フォーム名、Submissions、CSVダウンロード入口。氏名、メール、問い合わせ本文は隠す。 |
| F-08 | P0 | `f-08-site-access-overview.png` | Site access全体 | Site access見出し、Members一覧、Role、Can publish、Invite member / Invite client。氏名・メールは隠す。 |
| F-09 | P0 | `f-09-site-settings-site-access-menu.png` | Site settingsからSite accessへ入る画面 | 対象Site名、Site settings、Site accessメニュー、左メニューの位置関係。 |
| F-10 | P0 | `f-10-invite-member-button.png` | Invite memberボタン | Invite member / Invite client、Members一覧見出し、Role列。既存メンバー情報は隠す。 |
| F-11 | P0 | `f-11-role-can-publish-setting.png` | RoleとCan publishの設定 | Site role、Content editor、Can publish、保存または招待前のボタン。実メールは写さない。 |
| F-12 | P0 | `f-12-existing-member-role-edit.png` | 既存メンバーの権限編集 | Role変更メニュー、Can publish、Removeまたは権限変更入口。氏名・メールは隠す。 |

## G. トラブル解決・保守

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影ポイント |
| --- | --- | --- | --- | --- |
| G-04 | P0 | `g-04-publishing-domain-status-check.png` | Publishing / Domain状態の確認 | Publishing、Production domain、Connected / Published状態、対象Site名。DNS機密値は隠す。 |
| G-05 | P0 | `g-05-cms-item-status-troubleshooting.png` | CMS item statusの確認 | 対象item、Draft / Published / Queuedなどのstatus、Collection名。未公開本文は隠す。 |
| G-06 | P0 | `g-06-editable-indicator-troubleshooting.png` | 編集できる要素の表示確認 | 編集対象、青枠または鉛筆アイコン、ページ上の周辺文脈。 |
| G-07 | P0 | `g-07-role-permission-troubleshooting.png` | Role / Can publish権限確認 | Site access、Role、Content editor、Can publish。氏名・メールは隠す。 |
| G-08 | P0 | `g-08-can-publish-permission-check.png` | Publishできない時の権限確認 | Publishボタン、権限不足メッセージがあればその表示、対象画面。 |
| G-09 | P0 | `g-04-maintenance-request-example.png` | 保守依頼時に送るキャプチャ例 | URL、困っている箇所、画面全体、発生日時を説明できる構図。 |

## 撮影後の確認

- ファイル名が依頼書と一致している
- `src/assets/captures/manual/` に保存されている
- ロード中の表示が写っていない
- 個人情報、メールアドレス、請求情報、未公開情報が写っていない
- ボタンや入力欄だけでなく、どの画面なのか分かる周辺UIも入っている

## 元リスト

元の管理リストは `docs/human-capture-shot-list.md` です。
