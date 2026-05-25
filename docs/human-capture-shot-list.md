# Webflowマニュアル 人間撮影用キャプチャー一覧

この一覧は、マニュアル内の仮画像や汎用画像を、実際のWebflow画面キャプチャーへ差し替えるための撮影リストです。

以前の一覧は細かすぎたため、まず撮るべき画像を約35枚に絞っています。迷った場合は、この一覧の上から順に撮影してください。

## 撮影ルール

- Webflow画面を開いたら、すぐ撮らずに3〜5秒待つ。
- `Loading...`、スピナー、白紙、画像未読込、スケルトンUIが残っている画像は使わない。
- 個人名、メールアドレス、問い合わせ本文、未公開記事、顧客情報、請求情報は写さない。
- ボタンだけを拡大しすぎず、押す場所と周辺の文脈が同時に分かる構図にする。
- 保存、公開、削除、復元などは実行前の確認画面で止める。
- ファイルは `src/assets/captures/manual/` に保存する想定。

## 優先度

- P0: 最優先。これがないと手順が分かりにくい。
- P1: 余力があれば撮る。理解を補強する画像。

## A. はじめの一歩

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| A-01 | P0 | `a-01-dashboard-site-list.png` | Webflow Dashboardのサイト一覧 | `01-getting-started/00-site-update-overview.md`, `06-dashboard-overview.md` | Booostのサイトカード、Workspace名、Dashboard画面であることが分かる構図。不要なサイトや個人情報は隠す。 |
| A-02 | P0 | `a-02-site-card-actions.png` | 対象サイトカードの操作メニュー | `01-getting-started/06-dashboard-overview.md`, `07-editor-vs-designer.md`, `08-editor-only-recommendation.md` | Content editor入口とDesigner入口の違いが分かる状態。普段押す場所と触らない場所を説明できるようにする。 |
| A-03 | P0 | `a-03-site-settings-left-menu.png` | Site settingsの左メニュー | `01-getting-started/06-dashboard-overview.md`, `05-settings/00-site-settings-complete-guide.md` | General、Publishing、SEO、Forms、Backupsが見える状態。請求情報は写さない。 |
| A-04 | P1 | `a-04-invitation-and-login.png` | 招待メールまたはログイン画面 | `01-getting-started/01-invitation-email.md`, `02-create-account.md`, `03-first-login.md`, `05-reset-password.md` | 招待メールならAccept Invitation、ログイン画面ならEmail、Password、Forgot passwordが分かる状態。実メールは隠す。 |
| A-05 | P1 | `a-05-chrome-translate-extension.png` | Chrome翻訳またはIGNITE日本語化拡張機能 | `01-getting-started/09-chrome-translate-webflow.md` | Webflow画面とChrome拡張機能メニューが同時に見える構図。日本語化が便利だと分かる状態にする。 |
| A-06 | P0 | `a-06-booost-workspace-overview.png` | BooostのWorkspace全体 | `01-getting-started/00-workspace-intro.md` | `Booost Workspace`、対象サイトカード、Dashboardであることが分かる構図。他サイトや個人情報は隠す。 |
| A-07 | P0 | `a-07-workspace-plan-members.png` | Workspace plan / Members | `01-getting-started/00-workspace-plan.md` | 現在のWorkspace plan、メンバー数、UpgradeやPlan関連の表示。請求情報やメールアドレスは隠す。 |
| A-08 | P0 | `a-08-site-plan-settings.png` | Site plan / Publishing設定 | `01-getting-started/00-site-plan.md` | 対象サイト名、Site settings、Site plan名または公開設定。カード情報や請求情報は写さない。 |
| A-09 | P0 | `a-09-members-and-permissions.png` | Membersと権限 | `01-getting-started/00-add-member.md` | Invite/Add member、Role、Can publishなど権限判断に必要な列。氏名・メールは隠す。 |
| A-10 | P0 | `a-10-open-site-from-dashboard.png` | Dashboardからサイト修正画面に入る入口 | `01-getting-started/00-open-site.md` | 対象サイトカード、Open in Webflow、SettingsまたはDesignerへの入口。他サイト名は隠す。 |
| A-11 | P0 | `a-11-workspace-selector-open.png` | Workspace selectorを開いた状態 | `01-getting-started/00-workspace-intro.md` | 現在選択中のWorkspace名、対象Workspace候補、切り替え場所。他社Workspace名やメールアドレスは隠す。 |
| A-12 | P0 | `a-12-site-card-entry-points.png` | 対象Site cardの入口一覧 | `01-getting-started/00-workspace-intro.md` | 対象Site名、Open / Content editor、Settings、Designerの位置関係。他サイト名は隠す。 |
| A-13 | P0 | `a-13-workspace-members-role-list.png` | Workspace MembersのRole一覧 | `01-getting-started/00-workspace-plan.md` | Members見出し、RoleまたはSeat列、人数表示。氏名・メールは隠す。 |
| A-14 | P0 | `a-14-workspace-plan-billing-warning.png` | Plan / Upgrade / Billing入口 | `01-getting-started/00-workspace-plan.md` | Plan名、UpgradeやBilling入口、請求に関わる画面だと分かる見出し。カード情報や料金明細は写さない。 |

## B. Content Editor

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| B-01 | P0 | `b-01-open-content-editor.png` | Content Editor（旧バージョン）を開く入口 | `02-editor/01-open-legacy-editor.md` | Dashboard上の「Open Editor (Legacy)」が分かる状態。旧版の入口であることが伝わるようにする。 |
| B-02 | P0 | `b-02-editor-canvas-opened.png` | Content Editor（旧バージョン）でサイトを開いた直後 | `02-editor/01-open-legacy-editor.md` | 旧Editorの下部バー、ページ画面、編集できるサイト画面が見える状態。ロード完了後に撮る。 |
| B-03 | P0 | `b-03-editable-text-active.png` | テキスト編集状態 | `02-editor/03-edit-text.md`, `04-bold-text.md` | 編集できるテキスト、選択枠、入力カーソル、太字などの簡易ツールバーが分かる状態。 |
| B-04 | P0 | `b-04-link-settings-panel.png` | リンク設定画面 | `02-editor/05-add-link.md`, `07-edit-link-url.md`, `10-external-link-new-tab.md`, `11-anchor-link.md` | URL入力欄、Open in new tab、リンク先設定が分かる状態。外部URLは公開してよいものにする。 |
| B-05 | P0 | `b-05-image-replace.png` | 画像差し替え操作 | `02-editor/06-replace-image.md` | 画像にカーソルを合わせた状態、Replace / Upload画面、対象画像が分かる構図。 |
| B-06 | P0 | `b-06-publish-button-editor.png` | EditorのPublish操作 | `02-editor/08-save-and-publish.md`, `12-before-publish-checklist.md` | Publishボタン、公開前に確認すべきページ全体、保存状態が分かる状態。 |
| B-07 | P1 | `b-07-discard-changes-confirm.png` | 変更破棄の確認画面 | `02-editor/09-discard-changes.md` | Discard、Cancelなどの判断ボタンが見える状態。実際に破棄する直前で止める。 |
| B-08 | P0 | `b-08-content-editor-latest-canvas.png` | Content Editor（最新版）でサイトを開いた直後 | `02-editor/02-open-content-editor.md`, `02-editor/00-editor-complete-guide.md` | 最新版のContent editor roleとしてcanvasを開いた状態。旧Legacy Editorの下部バーではなく、最新UIで編集可能な状態が分かる構図にする。 |
| B-11 | P0 | `b-09-latest-content-editor-screen-guide.png` | 最新Content Editorの画面構成 | `02-editor/13-latest-content-editor-screen-guide.md` | Webflow公式Help CenterのContent editor role説明画像、またはBooostサイトを最新版Content editor roleで開いたcanvas画面。canvas、上部バー、Pages/CMS/Assetsなどの入口、編集可能な要素の青いアウトラインまたは編集アイコンが分かる状態。 |
| B-12 | P0 | `b-12-official-content-editor-canvas.png` | 公式画像: Content editor roleのcanvas全体 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/02-open-content-editor.md` | Webflow公式Help Centerまたは公式サイトの画像を利用。canvas、編集対象ページ、Content editor roleであることが分かるUI。Legacy Editorの古い下部バーだけの画像は避ける。 |
| B-13 | P0 | `b-13-official-content-editor-panels.png` | 公式画像: Pages / CMS / Assets / Settingsの入口 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/13-latest-content-editor-screen-guide.md` | Webflow公式Help CenterのContent editor role説明画像を利用。各panelの入口と位置関係が分かる画像にする。 |
| B-14 | P0 | `b-14-official-text-editing.png` | 公式画像: 文字編集のアウトラインまたはPencilアイコン | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/03-edit-text.md` | 編集対象テキスト、青いアウトライン、Pencilなどの編集アイコンが分かる公式画像。 |
| B-15 | P0 | `b-15-official-image-replace.png` | 公式画像: 画像差し替えの入口 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/06-replace-image.md` | 対象画像、画像編集アイコン、AssetsまたはUploadに進める入口が分かる公式画像。 |
| B-16 | P0 | `b-16-official-link-editing.png` | 公式画像: リンク編集の入口 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/07-edit-link-url.md`, `02-editor/10-external-link-new-tab.md` | Link設定、URL入力欄、新しいタブ設定などが分かる公式画像。 |
| B-17 | P0 | `b-17-official-publish-flow.png` | 公式画像: Publish前の確認画面 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/08-save-and-publish.md`, `02-editor/12-before-publish-checklist.md` | Publishボタン、公開対象、公開前確認の文脈が分かる公式画像。 |
| B-18 | P1 | `b-18-official-update-shortcut.png` | 公式画像: `?update` で直接編集画面を開く導線 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/02-open-content-editor.md` | 公式Help Centerの `?update` shortcut説明と整合する画像。ブラウザURL欄を写す場合は実サイトURLを公開可能なものにする。 |
| B-19 | P1 | `b-19-official-legacy-vs-content-editor.png` | 公式画像: Legacy Editorと最新版Content Editorの違い | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/13-latest-content-editor-screen-guide.md` | 旧Legacy Editorと最新版Content Editorを混同しないように、比較説明に使える公式画像または公式ページの画像。 |
| B-20 | P1 | `b-20-official-cms-item-editing.png` | 公式画像: CMS itemを作成・編集する画面 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/00-blog-post-complete-guide.md` | CMS fields、preview、publishの流れが分かる公式画像。 |
| B-21 | P1 | `b-21-official-seo-ogp-controls.png` | 公式画像: SEO / Open Graphを確認する画面 | `02-editor/14-official-content-editor-image-reference.md`, `05-settings/01-seo-title.md` | Page title、Meta description、Open Graph設定などが分かる公式画像。 |
| B-22 | P1 | `b-22-official-content-role-permissions.png` | 公式画像: Content editor roleの権限・Publish権限 | `02-editor/14-official-content-editor-image-reference.md`, `01-getting-started/08-editor-only-recommendation.md` | Content editor role、Can publish、権限範囲の説明に使える公式画像。 |
| B-23 | P1 | `b-23-official-cms-overview.png` | 公式画像: CMS機能の概要 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/00-blog-post-complete-guide.md` | Webflow公式CMSページ画像。CMSで構造化コンテンツを管理する全体像が分かる画像にする。 |
| B-24 | P1 | `b-24-official-cms-draft-publishing.png` | 公式画像: CMS下書き・公開ワークフロー | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/18-edit-published.md` | Webflow公式Updates画像。Draft changes、個別公開、公開前確認の文脈が分かる画像にする。 |
| B-25 | P1 | `b-25-official-cms-auto-save.png` | 公式画像: CMS自動保存 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/16-save-as-draft.md` | Webflow公式Updates画像。CMS編集の保存・公開操作を説明できる画像にする。 |
| B-26 | P1 | `b-26-official-cms-bulk-publishing.png` | 公式画像: CMS一括公開・一括非公開 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/25-cms-before-publish-checklist.md` | Webflow公式Updates画像。複数CMS itemをまとめて扱う操作の注意喚起に使う。 |
| B-27 | P1 | `b-27-official-cms-item-creation.png` | 公式画像: CMS item作成改善 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/02-create-new-post.md` | Webflow公式Updates画像。CMS item作成や編集の流れを補助する画像にする。 |
| B-28 | P1 | `b-28-official-seo-overview.png` | 公式画像: SEO機能の概要 | `02-editor/14-official-content-editor-image-reference.md`, `05-settings/01-seo-title.md` | Webflow公式SEOページ画像。SEO title、meta description、Open Graphの説明に使う。 |
| B-29 | P1 | `b-29-official-localization-overview.png` | 公式画像: Localization機能の概要 | `02-editor/14-official-content-editor-image-reference.md`, `07-localization/00-localization-overview.md` | Webflow公式Localizationページ画像。Localeや翻訳作業の全体像に使う。 |
| B-30 | P1 | `b-30-official-collaboration-overview.png` | 公式画像: チーム編集・コメント・権限 | `02-editor/14-official-content-editor-image-reference.md`, `01-getting-started/08-editor-only-recommendation.md` | Webflow公式Collaborationページ画像。Content editor role、コメント、権限の説明に使う。 |
| B-31 | P1 | `b-31-official-single-page-publishing.png` | 公式画像: 1ページだけPublishする考え方 | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/08-save-and-publish.md` | Webflow公式Single page publishing画像。Publish対象ページと公開先を確認する説明に使う。 |
| B-32 | P1 | `b-32-official-single-page-publishing-access.png` | 公式画像: 1ページ公開権限 | `02-editor/14-official-content-editor-image-reference.md`, `01-getting-started/08-editor-only-recommendation.md` | Webflow公式Single page publishing access画像。Role、Can publish、公開権限の説明に使う。 |
| B-33 | P1 | `b-33-official-next-gen-cms.png` | 公式画像: Next-gen CMSの概要 | `02-editor/14-official-content-editor-image-reference.md`, `03-cms/02-create-new-post.md` | Webflow公式Next-gen CMS画像。CMS item作成フォームや主要Fieldの説明に使う。 |
| B-34 | P1 | `b-34-official-publishing-permission-toggle.png` | 公式画像: Publish権限のON/OFF | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/08-save-and-publish.md` | Webflow公式Publishing permission toggle画像。Publish権限がない場合の説明に使う。 |
| B-35 | P1 | `b-35-official-preview-roles.png` | 公式画像: Preview role | `02-editor/14-official-content-editor-image-reference.md`, `02-editor/12-before-publish-checklist.md` | Webflow公式Preview roles画像。公開前レビューや確認担当者の説明に使う。 |
| B-36 | P1 | `b-36-official-hosting-domain.png` | 公式画像: Hosting / Domain / SSLの概要 | `02-editor/14-official-content-editor-image-reference.md`, `05-settings/09-domain-status.md` | Webflow公式Hosting画像。Domain、SSL、Publishing設定の説明に使う。 |
| B-37 | P1 | `b-37-official-security-permissions.png` | 公式画像: Securityと権限管理 | `02-editor/14-official-content-editor-image-reference.md`, `06-troubleshooting/00-common-checklist.md` | Webflow公式Security画像。権限不足や安全確認の説明に使う。 |
| B-38 | P1 | `b-38-official-analyze-seo-settings.png` | 公式画像: Analyze / 計測の概要 | `02-editor/14-official-content-editor-image-reference.md`, `05-settings/10-search-engine-control.md` | Webflow公式Analyze画像。検索表示、計測、反映タイミングの説明に使う。 |
| B-39 | P1 | `b-39-official-designer-overview.png` | 公式画像: Designerの概要 | `02-editor/14-official-content-editor-image-reference.md`, `04-designer/01-designer-warning.md` | Webflow公式Design画像。Designerが高機能で慎重に扱う画面だと伝える説明に使う。 |
| B-40 | P0 | `work-00-dashboard-workspace-site-check.png` | 作業前のWorkspace / Site確認 | `work/06-before-start.md` | DashboardでWorkspace名と対象Site cardが同時に見える構図。他社Site名、通知、メールは隠す。 |
| B-41 | P0 | `work-00-content-editor-entry-check.png` | 作業前のContent editor入口確認 | `work/06-before-start.md` | 対象Site card、Content editor入口、DesignerやSettingsとの位置関係。通常更新の入口を説明できる状態にする。 |
| B-42 | P0 | `work-00-before-publish-target-check.png` | 作業前ページのPublish前確認 | `work/06-before-start.md` | Publishボタン、公開対象、公開先ドメイン、Cancelできる状態。実行前で止める。 |
| B-09 | P0 | `work-01-edit-text-open-site.png` | テキスト修正作業の開始画面 | `work/00-edit-text.md` | 対象サイトカードからContent editor roleを開く直前。Workspace名、対象サイトカード、編集入口が分かる構図。 |
| B-10 | P0 | `work-02-replace-image-edit-icon.png` | 画像差し替えアイコン | `work/01-replace-image.md` | 対象画像と編集アイコンが同時に見える状態。未公開画像や個人情報は写さない。 |
| B-43 | P0 | `work-01-editable-text-indicator.png` | テキスト編集可能表示 | `work/00-edit-text.md` | Content editorで修正対象テキスト、青枠、鉛筆アイコンが見える状態。未公開情報は隠す。 |
| B-44 | P0 | `work-01-text-before-publish-review.png` | テキスト修正後のPublish前確認 | `work/00-edit-text.md` | 修正後テキスト、Publishボタン、対象ページが分かる周辺UI。実行前で止める。 |
| B-45 | P0 | `work-01-site-access-role-check.png` | テキスト編集できない時の権限確認 | `work/00-edit-text.md` | Site access / Members、Role、Can publish、Content editorなど。氏名・メールは隠す。 |

## C. CMS更新

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| C-01 | P0 | `c-01-cms-collections-entry.png` | CMS / Collections入口 | `03-cms/00-blog-post-complete-guide.md`, `01-where-is-cms.md` | 左メニュー、Collections、Blog / News / お知らせなど対象Collectionが分かる状態。 |
| C-02 | P0 | `c-02-collection-items-list.png` | 記事一覧画面 | `03-cms/02-create-new-post.md` | 既存記事一覧、検索欄、New itemボタンが見える状態。未公開記事名は必要なら隠す。 |
| C-03 | P0 | `c-03-new-cms-item-form.png` | 新規CMS item入力フォーム | `03-cms/02-create-new-post.md`, `03-post-title.md` | Name / Title、Slug、Save、Publishなど入力フォーム全体が分かる状態。 |
| C-04 | P0 | `c-04-thumbnail-and-category.png` | サムネイル・カテゴリー設定 | `03-cms/04-thumbnail-image.md`, `05-post-category.md`, `22-image-alt.md` | Thumbnail / Main image、Upload、Category、Alt textの場所が分かる状態。 |
| C-05 | P0 | `c-05-rich-text-body.png` | Rich Text本文欄 | `03-cms/06-write-body.md`, `07-bold-italic-body.md`, `08-headings.md`, `09-bullet-list.md`, `13-body-link.md` | 本文入力欄、ツールバー、見出し、リスト、リンク設定が分かる状態。 |
| C-06 | P0 | `c-06-rich-text-media.png` | 本文中の画像・YouTube挿入 | `03-cms/10-insert-image.md`, `11-resize-image.md`, `12-embed-youtube.md` | `+`ボタン、Image、Embed、画像サイズ変更メニューが分かる構図。 |
| C-07 | P0 | `c-07-save-draft-and-publish.png` | 下書き保存・公開操作 | `03-cms/16-save-as-draft.md`, `17-publish-draft.md`, `25-cms-before-publish-checklist.md` | Save as Draft、Publish、公開前プレビューの流れが分かる状態。 |
| C-08 | P1 | `c-08-schedule-and-date.png` | 公開日・予約公開設定 | `03-cms/14-publish-date.md`, `15-schedule-publish.md` | Date / Published on、Schedule、日時指定が見える状態。 |
| C-09 | P1 | `c-09-unpublish-archive-delete.png` | 非公開・アーカイブ・削除の確認画面 | `03-cms/19-unpublish.md`, `20-archive-post.md`, `21-delete-post.md` | Unpublish、Archive、Deleteの確認画面。削除は実行しない。 |
| C-10 | P1 | `c-10-asset-file-upload.png` | PDFなどファイルのAssetアップロード | `03-cms/24-attach-file.md` | Asset Panel、Upload、ファイル名、Copy linkが分かる状態。実資料名は公開OKのものにする。 |
| C-11 | P0 | `c-11-category-dropdown-open.png` | Categoryフィールドのドロップダウン | `03-cms/05-post-category.md` | `Category`、`Pick a Category...`、選択肢が見える状態。未公開記事名や本文は隠す。 |
| C-12 | P0 | `c-12-rich-text-list-icons.png` | Rich Textのリストアイコン | `03-cms/09-bullet-list.md` | 選択中の本文、番号なしリスト、番号付きリストのアイコンが見える状態。 |
| C-13 | P0 | `c-13-archive-button-visible.png` | CMS一覧のArchiveボタン | `03-cms/20-archive-post.md` | 記事選択後、上部のArchiveボタンが見える状態。実行前に止める。 |
| C-14 | P0 | `work-03-update-post-cms-list.png` | CMS記事一覧から投稿を始める画面 | `work/02-update-post.md` | CMS/Collection名、記事一覧、Newボタン。未公開記事名は必要に応じて隠す。 |
| C-15 | P0 | `c-15-booost-cms-fields-overview.png` | Booost記事入力フィールド全体 | `03-cms/26-booost-cms-field-guide.md` | Title、Slug、Summary、Thumbnail、Bodyなど主要Fieldと、Save/Create/Publish周辺の操作ボタンが分かる状態。未公開本文や個人情報は隠す。 |
| C-16 | P0 | `c-16-cms-entry-with-sidebar.png` | CMS / Collections入口 | `03-cms/01-where-is-cms.md` | Content editorまたは編集画面でCMS / Collections入口、左メニュー、対象Site名が分かる状態。 |
| C-17 | P0 | `c-17-collection-list-select-target.png` | Collection一覧から対象を選ぶ画面 | `03-cms/01-where-is-cms.md` | Blog、News、お知らせなどのCollection名とCMS見出し。未公開記事名は写さない。 |
| C-18 | P0 | `c-18-cms-items-status-list.png` | CMS item一覧のstatus確認 | `03-cms/01-where-is-cms.md` | item一覧、Status列、Draft / Published表示、Newボタン、検索欄。社外秘タイトルは隠す。 |
| C-19 | P0 | `c-19-new-item-from-collection-list.png` | Collection一覧からNew itemを押す直前 | `03-cms/02-create-new-post.md` | Collection名、Newボタン、検索欄、既存itemのstatus表示。 |
| C-20 | P0 | `c-20-new-cms-item-fields-overview.png` | 新規CMS itemのField全体 | `03-cms/02-create-new-post.md` | Title / Name、Slug、主要Field、Save as Draft、Publish / Create周辺。未公開本文は隠す。 |
| C-21 | P0 | `c-21-cms-save-publish-options.png` | CMS itemの保存・公開ボタン | `03-cms/02-create-new-post.md` | Save as Draft、Publish、ScheduleまたはPublish options、現在のCMS item名。実行前で止める。 |
| C-22 | P0 | `c-22-save-as-draft-button-closeup.png` | Save as Draftボタン | `03-cms/16-save-as-draft.md` | Save as Draft、Publish / Create、item名、Draft対象だと分かる見出し。 |
| C-23 | P0 | `c-23-draft-status-in-item-list.png` | Draft statusの一覧表示 | `03-cms/16-save-as-draft.md` | 対象item名、Draft status、Collection名、一覧UI。未公開本文や個人情報は隠す。 |
| C-24 | P0 | `c-24-published-item-draft-changes.png` | 公開済みitemの未公開変更 | `03-cms/16-save-as-draft.md` | PublishedまたはDraft changesのstatus、Publish options、item名。未公開本文は隠す。 |
| C-25 | P0 | `c-25-draft-item-before-publish.png` | Draft itemを公開前に探す画面 | `03-cms/17-publish-draft.md` | Draft status、対象item、Collection名、検索欄または一覧UI。 |
| C-26 | P0 | `c-26-draft-item-publish-options.png` | Draft itemのPublish入口 | `03-cms/17-publish-draft.md` | Publish、Publish options、item名、Draft status。実行前で止める。 |
| C-27 | P0 | `c-27-publish-now-queue-options.png` | Publish now / Queue選択肢 | `03-cms/17-publish-draft.md` | Publish now、Queue for next site publish、Scheduleがあればその選択肢、Cancelできる状態。 |
| C-28 | P0 | `c-28-published-item-status-list.png` | Published itemの一覧表示 | `03-cms/18-edit-published.md` | Published status、対象item、Collection名、検索欄または一覧UI。 |
| C-29 | P0 | `c-29-published-item-update-options.png` | 公開済みitem編集後のPublish options | `03-cms/18-edit-published.md` | item名、Published / Draft changesのstatus、Publish now、Queue for next site publish。 |

## D. Designer

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| D-01 | P0 | `d-01-designer-opened.png` | Designerを開いた状態 | `04-designer/01-designer-warning.md` | 左パネル、キャンバス、右パネル、上部バーが見える状態。初心者が「ここは慎重に触る画面」と分かる構図。 |
| D-02 | P0 | `d-02-edit-page-text.png` | Designerでテキストを選択 | `04-designer/02-edit-homepage-text.md`, `03-edit-address.md` | 変更対象テキスト、選択枠、右パネルが見える状態。誤って別要素を選んでいないことが分かるようにする。 |
| D-03 | P1 | `d-03-assets-and-logo.png` | Asset Panelまたはロゴ画像選択 | `04-designer/04-replace-logo.md`, `05-asset-panel.md`, `06-delete-asset.md` | Asset Panel、Upload、ロゴ選択、削除前確認のどれかが分かる状態。削除は実行しない。 |
| D-04 | P0 | `d-04-designer-publish-modal.png` | DesignerのPublishモーダル | `04-designer/07-publish-button.md` | 公開対象ドメイン、Publish to selected domains、公開ボタンが見える状態。 |
| D-05 | P1 | `d-05-undo-and-unsaved-warning.png` | Undoまたは未保存変更の確認 | `04-designer/08-undo-ctrl-z.md`, `09-discard-designer-changes.md` | Undo / Redo、または保存せず終了する確認画面が見える状態。 |

## E. Locale翻訳

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| E-01 | P0 | `e-01-locale-selector.png` | Designer上部のLocale selector | `07-localization/00-localization-overview.md`, `01-locale-translation-workflow.md` | Primary / Secondary localeの切り替え場所が分かる状態。現在選択中のLocaleも見えるようにする。 |
| E-02 | P0 | `e-02-localization-settings.png` | Localization設定画面 | `07-localization/06-add-new-locale.md` | Primary locale、Secondary locale、Add locale、Subdirectory、Publishing statusが分かる状態。 |
| E-03 | P0 | `e-03-static-page-translation.png` | 固定ページの翻訳操作 | `07-localization/02-static-page-translation.md` | 翻訳対象テキストを選択し、Translateボタンや翻訳結果が分かる状態。 |
| E-04 | P0 | `e-04-cms-locale-translation.png` | CMS itemのLocale翻訳 | `07-localization/03-cms-locale-translation.md` | CMS item、対象Locale、Title / Body / SEOなど翻訳対象フィールドが分かる状態。 |
| E-05 | P0 | `e-05-localized-seo-ogp.png` | LocaleごとのSEO / OGP設定 | `07-localization/04-localized-seo-ogp.md` | Page title、Meta description、OGP imageが対象Localeごとに設定されることが分かる状態。 |
| E-06 | P0 | `e-06-locale-publish-and-url.png` | Locale公開と公開URL確認 | `07-localization/05-locale-publish-checklist.md`, `07-publish-and-reflect-locale.md` | Publishモーダル、公開対象Locale、公開後の `/en` などのURLが分かる状態。 |
| E-07 | P0 | `work-06-edit-locale-selector.png` | Locale selectorで対象言語を確認する画面 | `work/05-edit-locale.md` | Locale selector、現在のLocale、対象ページの見出しが分かる状態。 |

## F. 設定・フォーム

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| F-01 | P0 | `f-01-seo-and-ogp-settings.png` | SEO / OGP設定 | `05-settings/01-seo-title.md`, `02-seo-description.md`, `03-ogp-image.md`, `10-search-engine-control.md` | Title tag、Meta description、Open Graph imageが分かる状態。コードや機密設定は隠す。 |
| F-02 | P0 | `f-02-forms-list-and-submissions.png` | Forms一覧・Submissions | `05-settings/04-form-submissions.md`, `06-form-csv-download.md` | フォーム名、Submissions、Export CSVボタンが分かる状態。問い合わせ本文や個人情報は隠す。 |
| F-03 | P0 | `f-03-email-notification-settings.png` | Form通知メール設定 | `05-settings/05-form-notification-email.md`, `06-troubleshooting/06-email-not-arriving.md` | 通知先メール欄、フォーム名、保存ボタンが分かる状態。実メールアドレスは隠す。 |
| F-04 | P1 | `f-04-members-and-roles.png` | Site access / メンバー権限 | `05-settings/08-invite-collaborator.md` | Role、Can publish、招待・権限設定が分かる状態。氏名・メールは隠す。 |
| F-05 | P0 | `f-05-domain-and-publishing-status.png` | Publishing / Domain状態 | `05-settings/09-domain-status.md`, `06-troubleshooting/01-cache-not-reflecting.md` | Production domain、SSL、Connected、Publish状態が分かる状態。 |
| F-06 | P0 | `work-04-edit-seo-settings.png` | 作業ベースSEO設定画面 | `work/03-edit-seo.md` | Title tag、Meta description、対象ページ名。APIキーや請求情報は写さない。 |
| F-07 | P0 | `work-05-check-forms-submissions.png` | 作業ベースForms送信内容確認画面 | `work/04-check-forms.md` | フォーム名、Submissions、CSVダウンロード入口。氏名、メール、問い合わせ本文は隠す。 |
| F-08 | P0 | `f-08-site-access-overview.png` | Site access全体 | `05-settings/08-invite-collaborator.md` | Site access見出し、Members一覧、Role、Can publish、Invite member / Invite client。氏名・メールは隠す。 |
| F-09 | P0 | `f-09-site-settings-site-access-menu.png` | Site settingsからSite accessへ入る画面 | `05-settings/08-invite-collaborator.md` | 対象Site名、Site settings、Site accessメニュー、左メニューの位置関係。 |
| F-10 | P0 | `f-10-invite-member-button.png` | Invite memberボタン | `05-settings/08-invite-collaborator.md` | Invite member / Invite client、Members一覧見出し、Role列。既存メンバー情報は隠す。 |
| F-11 | P0 | `f-11-role-can-publish-setting.png` | RoleとCan publishの設定 | `05-settings/08-invite-collaborator.md` | Site role、Content editor、Can publish、保存または招待前のボタン。実メールは写さない。 |
| F-12 | P0 | `f-12-existing-member-role-edit.png` | 既存メンバーの権限編集 | `05-settings/08-invite-collaborator.md` | Role変更メニュー、Can publish、Removeまたは権限変更入口。氏名・メールは隠す。 |

## G. トラブル解決・保守

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| G-01 | P0 | `g-01-backups-list.png` | Backups一覧 | `06-troubleshooting/05-backup-restore.md` | Backup日時、Preview、Restoreが見える状態。実行はしない。 |
| G-02 | P0 | `g-02-backup-restore-warning.png` | Restore確認画面 | `06-troubleshooting/05-backup-restore.md` | 復元前の警告と戻る選択肢が分かる状態。Restoreは押さない。 |
| G-03 | P1 | `g-03-error-examples.png` | 画像アップロードエラー、404などの例 | `06-troubleshooting/02-image-upload-failed.md`, `04-404-not-found.md` | エラー内容、URL、発生箇所が分かる状態。公開してよいPC画面のテストページで撮る。 |
| G-04 | P0 | `g-04-publishing-domain-status-check.png` | Publishing / Domain状態の確認 | `06-troubleshooting/00-common-checklist.md` | Publishing、Production domain、Connected / Published状態、対象Site名。DNS機密値は隠す。 |
| G-05 | P0 | `g-05-cms-item-status-troubleshooting.png` | CMS item statusの確認 | `06-troubleshooting/00-common-checklist.md` | 対象item、Draft / Published / Queuedなどのstatus、Collection名。未公開本文は隠す。 |
| G-06 | P0 | `g-06-editable-indicator-troubleshooting.png` | 編集できる要素の表示確認 | `06-troubleshooting/00-common-checklist.md` | 編集対象、青枠または鉛筆アイコン、ページ上の周辺文脈。 |
| G-07 | P0 | `g-07-role-permission-troubleshooting.png` | Role / Can publish権限確認 | `06-troubleshooting/00-common-checklist.md` | Site access、Role、Content editor、Can publish。氏名・メールは隠す。 |
| G-08 | P0 | `g-08-can-publish-permission-check.png` | Publishできない時の権限確認 | `06-troubleshooting/00-common-checklist.md` | Publishボタン、権限不足メッセージがあればその表示、対象画面。 |
| G-04 | P0 | `g-04-maintenance-request-example.png` | 保守依頼時に送るキャプチャ例 | `06-troubleshooting/07-maintenance-request.md`, `00-common-checklist.md` | URL、困っている箇所、画面全体、発生日時を説明できる構図。 |

## 最低限の撮影順

時間が限られる場合は、次の順で撮影してください。

1. A-01〜A-03: DashboardとSite settingsの入口
2. B-01〜B-06、B-08: Content Editorの基本操作
3. C-01〜C-07: CMS投稿の基本操作
4. F-02〜F-03: フォーム確認、CSV、通知メール
5. E-01〜E-06: Locale翻訳の基本操作
6. G-01〜G-04: トラブル時の確認・保守依頼

## 差し替え方針

撮影が必要な画像はこの一覧で管理します。未撮影のページには、本文内にも `:::note[キャプチャー指示]` を入れ、撮影する画面、保存ファイル名、撮影直前の状態、必ず写すもの、写さないものを明記します。撮影後に画像を本文へ差し込む時は、該当するキャプチャー指示を削除してください。

## 2026-05-22 反映状況

2026-05-18に取得した37枚のPNGは、対応する本文ページへ反映済みです。画像は `src/assets/captures/manual/` に保存しています。

次回の撮影依頼用に、未撮影分だけを抜き出した依頼書を `docs/booost-capture-request-2026-05-22.md` に作成しました。撮影担当者へ渡す場合は、まずそちらを使ってください。

今回未取得のキャプチャーは以下です。

- A-04: `a-04-invitation-and-login.png`
- A-06: `a-06-booost-workspace-overview.png`
- A-07: `a-07-workspace-plan-members.png`
- A-08: `a-08-site-plan-settings.png`
- A-09: `a-09-members-and-permissions.png`
- A-10: `a-10-open-site-from-dashboard.png`
- B-07: `b-07-discard-changes-confirm.png`
- B-08: `b-08-content-editor-latest-canvas.png`
- B-11: `b-09-latest-content-editor-screen-guide.png`
- B-12: `b-12-official-content-editor-canvas.png`
- B-13: `b-13-official-content-editor-panels.png`
- B-14: `b-14-official-text-editing.png`
- B-15: `b-15-official-image-replace.png`
- B-16: `b-16-official-link-editing.png`
- B-17: `b-17-official-publish-flow.png`
- B-18: `b-18-official-update-shortcut.png`
- B-19: `b-19-official-legacy-vs-content-editor.png`
- B-20: `b-20-official-cms-item-editing.png`
- B-21: `b-21-official-seo-ogp-controls.png`
- B-22: `b-22-official-content-role-permissions.png`
- B-23: `b-23-official-cms-overview.png`
- B-24: `b-24-official-cms-draft-publishing.png`
- B-25: `b-25-official-cms-auto-save.png`
- B-26: `b-26-official-cms-bulk-publishing.png`
- B-27: `b-27-official-cms-item-creation.png`
- B-28: `b-28-official-seo-overview.png`
- B-29: `b-29-official-localization-overview.png`
- B-30: `b-30-official-collaboration-overview.png`
- B-31: `b-31-official-single-page-publishing.png`
- B-32: `b-32-official-single-page-publishing-access.png`
- B-33: `b-33-official-next-gen-cms.png`
- B-34: `b-34-official-publishing-permission-toggle.png`
- B-35: `b-35-official-preview-roles.png`
- B-36: `b-36-official-hosting-domain.png`
- B-37: `b-37-official-security-permissions.png`
- B-38: `b-38-official-analyze-seo-settings.png`
- B-39: `b-39-official-designer-overview.png`
- B-09: `work-01-edit-text-open-site.png`
- B-10: `work-02-replace-image-edit-icon.png`
- C-11: `c-11-category-dropdown-open.png`
- C-12: `c-12-rich-text-list-icons.png`
- C-13: `c-13-archive-button-visible.png`
- C-14: `work-03-update-post-cms-list.png`
- C-15: `c-15-booost-cms-fields-overview.png`
- D-05: `d-05-undo-and-unsaved-warning.png`
- E-06: `e-06-locale-publish-and-url.png`
- E-07: `work-06-edit-locale-selector.png`
- F-06: `work-04-edit-seo-settings.png`
- F-07: `work-05-check-forms-submissions.png`
- G-04: `g-04-maintenance-request-example.png`
