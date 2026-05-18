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
| A-01 | P0 | `a-01-dashboard-site-list.png` | Webflow Dashboardのサイト一覧 | `01-getting-started/00-site-update-overview.md`, `06-dashboard-overview.md` | BOOSTのサイトカード、Workspace名、Dashboard画面であることが分かる構図。不要なサイトや個人情報は隠す。 |
| A-02 | P0 | `a-02-site-card-actions.png` | 対象サイトカードの操作メニュー | `01-getting-started/06-dashboard-overview.md`, `07-editor-vs-designer.md`, `08-editor-only-recommendation.md` | Content editor入口とDesigner入口の違いが分かる状態。普段押す場所と触らない場所を説明できるようにする。 |
| A-03 | P0 | `a-03-site-settings-left-menu.png` | Site settingsの左メニュー | `01-getting-started/06-dashboard-overview.md`, `05-settings/00-site-settings-complete-guide.md` | General、Publishing、SEO、Forms、Backupsが見える状態。請求情報は写さない。 |
| A-04 | P1 | `a-04-invitation-and-login.png` | 招待メールまたはログイン画面 | `01-getting-started/01-invitation-email.md`, `02-create-account.md`, `03-first-login.md`, `05-reset-password.md` | 招待メールならAccept Invitation、ログイン画面ならEmail、Password、Forgot passwordが分かる状態。実メールは隠す。 |
| A-05 | P1 | `a-05-chrome-translate-extension.png` | Chrome翻訳またはIGNITE日本語化拡張機能 | `01-getting-started/09-chrome-translate-webflow.md` | Webflow画面とChrome拡張機能メニューが同時に見える構図。日本語化が便利だと分かる状態にする。 |

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

## F. 設定・フォーム

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| F-01 | P0 | `f-01-seo-and-ogp-settings.png` | SEO / OGP設定 | `05-settings/01-seo-title.md`, `02-seo-description.md`, `03-ogp-image.md`, `10-search-engine-control.md` | Title tag、Meta description、Open Graph imageが分かる状態。コードや機密設定は隠す。 |
| F-02 | P0 | `f-02-forms-list-and-submissions.png` | Forms一覧・Submissions | `05-settings/04-form-submissions.md`, `06-form-csv-download.md` | フォーム名、Submissions、Export CSVボタンが分かる状態。問い合わせ本文や個人情報は隠す。 |
| F-03 | P0 | `f-03-email-notification-settings.png` | Form通知メール設定 | `05-settings/05-form-notification-email.md`, `06-troubleshooting/06-email-not-arriving.md` | 通知先メール欄、フォーム名、保存ボタンが分かる状態。実メールアドレスは隠す。 |
| F-04 | P1 | `f-04-members-and-roles.png` | Site access / メンバー権限 | `05-settings/08-invite-collaborator.md` | Role、Can publish、招待・権限設定が分かる状態。氏名・メールは隠す。 |
| F-05 | P0 | `f-05-domain-and-publishing-status.png` | Publishing / Domain状態 | `05-settings/09-domain-status.md`, `06-troubleshooting/01-cache-not-reflecting.md` | Production domain、SSL、Connected、Publish状態が分かる状態。 |

## G. トラブル解決・保守

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| G-01 | P0 | `g-01-backups-list.png` | Backups一覧 | `06-troubleshooting/05-backup-restore.md` | Backup日時、Preview、Restoreが見える状態。実行はしない。 |
| G-02 | P0 | `g-02-backup-restore-warning.png` | Restore確認画面 | `06-troubleshooting/05-backup-restore.md` | 復元前の警告と戻る選択肢が分かる状態。Restoreは押さない。 |
| G-03 | P1 | `g-03-error-examples.png` | 画像アップロードエラー、404などの例 | `06-troubleshooting/02-image-upload-failed.md`, `04-404-not-found.md` | エラー内容、URL、発生箇所が分かる状態。公開してよいPC画面のテストページで撮る。 |
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

本文には撮影指示コールアウトを表示しません。撮影が必要な画像はこの一覧で管理し、撮影後に必要な画像だけを本文へ追加してください。

## 2026-05-18 反映状況

今回取得した37枚のPNGは、対応する本文ページへ反映済みです。画像は `src/assets/captures/manual/` に保存しています。現時点で、保存済みPNGの未使用画像はありません。

今回未取得の統合版キャプチャーは以下です。

- A-04: `a-04-invitation-and-login.png`
- B-07: `b-07-discard-changes-confirm.png`
- B-08: `b-08-content-editor-latest-canvas.png`
- D-05: `d-05-undo-and-unsaved-warning.png`
- E-06: `e-06-locale-publish-and-url.png`
- G-04: `g-04-maintenance-request-example.png`
