# Webflowマニュアル 人間撮影用キャプチャー一覧

この一覧は、現在入っている汎用キャプチャーや仮画像を、実際に人間が撮影した分かりやすい画像へ差し替えるための撮影リストです。

## 撮影ルール

- Webflow画面を開いたら、すぐ撮らずに数秒待つ。
- `Loading...`、スピナー、白紙、画像未読込、スケルトンUIが残っている画像は使わない。
- 個人名、メールアドレス、問い合わせ本文、未公開記事、顧客情報、請求情報は写さない。
- 画面全体よりも、読者が押す場所・見る場所が分かる構図を優先する。
- 可能ならデスクトップ幅は1440px以上、スマホ確認は390px前後で撮る。
- 撮影後、画像を開いてロード中の状態や不要な情報が写っていないか確認する。
- ファイルは `src/assets/captures/manual/` に保存する想定。必要ならこのフォルダを作成する。

## 優先度

- P0: これがないと手順が分かりにくい。最優先で撮る。
- P1: あると理解しやすい。主要ページに入れる。
- P2: 余力があれば撮る。補足・FAQ・注意喚起用。

## A. はじめの一歩

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| A-01 | P0 | `a-01-dashboard-site-list.png` | Webflow Dashboardのサイト一覧 | `01-getting-started/00-site-update-overview.md`, `06-dashboard-overview.md` | 対象サイトカード、Workspace名、サイト名が分かる状態。個人名は写っても問題ない範囲に調整 |
| A-02 | P0 | `a-02-site-card-hover-actions.png` | 対象サイトカードにカーソルを合わせ、開くボタンが出た状態 | `01-getting-started/06-dashboard-overview.md`, `11-after-login-first-steps.md` | `Open in Webflow`、設定メニュー、Designerなどの違いが分かる状態 |
| A-03 | P0 | `a-03-site-settings-left-menu.png` | 対象サイトのSite settings左メニュー | `01-getting-started/06-dashboard-overview.md` | General、Publishing、SEO、Forms、Backupsなどが見える状態 |
| A-04 | P1 | `a-04-webflow-invitation-email.png` | Webflow招待メールの見本 | `01-getting-started/01-invitation-email.md` | `Accept Invitation` が分かること。実メールアドレスや個人名は隠す |
| A-05 | P1 | `a-05-create-account-screen.png` | 招待リンク後のアカウント作成画面 | `01-getting-started/02-create-account.md` | Full name、Password、Create accountが分かる状態。入力前の空欄で撮る |
| A-06 | P1 | `a-06-login-screen.png` | Webflowログイン画面 | `01-getting-started/03-first-login.md`, `05-reset-password.md` | Email、Password、Log in、Forgot passwordの位置が分かる状態 |
| A-07 | P1 | `a-07-bookmark-login-url.png` | ブラウザでログインURLをブックマークする画面 | `01-getting-started/04-bookmark-login.md` | アドレスバーとブックマーク追加の流れが分かる状態。公開サイトURLは問題なければ表示 |
| A-08 | P1 | `a-08-content-editor-vs-designer-entry.png` | サイトカード上でContent editor入口とDesigner入口が分かる状態 | `01-getting-started/07-editor-vs-designer.md`, `08-editor-only-recommendation.md` | 通常更新で押すもの、押さないものを比較できる構図 |
| A-09 | P1 | `a-09-chrome-translate-webflow.png` | Chrome翻訳またはIGNITE拡張機能でWebflow画面を日本語化している画面 | `01-getting-started/09-chrome-translate-webflow.md` | 拡張機能・翻訳メニュー・Webflow画面が同時に分かる状態 |
| A-10 | P2 | `a-10-webflow-ui-terms.png` | Dashboard上でDashboard、Designer、Publishなど英語UIが見える状態 | `01-getting-started/10-webflow-ui-glossary.md` | 用語表と対応しやすいよう、英語UIが読み取れる状態 |

## B. Content Editor

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| B-01 | P0 | `b-01-open-content-editor.png` | Content editor roleで対象サイトを開く入口 | `02-editor/00-editor-complete-guide.md`, `01-open-editor.md` | Dashboardから編集画面へ入るボタンが分かる状態 |
| B-02 | P0 | `b-02-editor-canvas-opened.png` | Content editorでサイトを開いた直後 | `02-editor/00-editor-complete-guide.md`, `01-open-editor.md` | 上部バー、ページ画面、編集可能な雰囲気が分かる状態 |
| B-03 | P0 | `b-03-editable-text-hover.png` | 編集可能なテキストにカーソルを合わせた状態 | `02-editor/02-edit-text.md` | 編集枠、編集アイコン、対象テキストが見える |
| B-04 | P0 | `b-04-text-editing-active.png` | テキストをクリックして入力できる状態 | `02-editor/02-edit-text.md` | 入力カーソル、変更対象の見出しまたは本文が分かる |
| B-05 | P1 | `b-05-bold-toolbar.png` | テキスト選択後に太字メニューが出た状態 | `02-editor/03-bold-text.md` | Boldボタン、選択範囲が分かる |
| B-06 | P0 | `b-06-link-settings-panel.png` | 文章やボタンのリンク設定画面 | `02-editor/04-add-link.md`, `06-edit-link-url.md` | URL入力欄、Open in new tab設定が見える |
| B-07 | P0 | `b-07-image-replace-hover.png` | 画像にカーソルを合わせて編集アイコンが出た状態 | `02-editor/05-replace-image.md` | 対象画像だけを選んでいることが分かる |
| B-08 | P1 | `b-08-image-upload-dialog.png` | 画像アップロード・Replace画面 | `02-editor/05-replace-image.md` | Upload、Replace、Choose imageが見える |
| B-09 | P0 | `b-09-publish-button-editor.png` | Editor / Content editorのPublishボタン | `02-editor/07-save-and-publish.md` | Publishボタン、保存状態、公開対象が分かる |
| B-10 | P1 | `b-10-discard-changes-confirm.png` | 変更破棄または閉じる確認画面 | `02-editor/08-discard-changes.md` | Discard、Cancelなど判断に必要なボタンが見える |
| B-11 | P1 | `b-11-external-link-new-tab.png` | 外部リンクを新規タブで開く設定 | `02-editor/09-external-link-new-tab.md` | 外部URLとNew tab設定が見える |
| B-12 | P1 | `b-12-anchor-link-target-section.png` | ページ内アンカーリンクの対象セクション | `02-editor/10-anchor-link.md` | セクションIDまたはリンク先見出しが分かる |
| B-13 | P0 | `b-13-before-publish-preview.png` | Publish前にページ全体を確認している状態 | `02-editor/11-before-publish-checklist.md` | 変更済みテキスト、画像、リンク導線が見える |

## C. CMS更新

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| C-01 | P0 | `c-01-cms-collections-entry.png` | Collections / CMS入口 | `03-cms/00-blog-post-complete-guide.md`, `01-where-is-cms.md` | 左メニューやCollectionsタブが分かる |
| C-02 | P0 | `c-02-collection-list.png` | CMS Collection一覧 | `03-cms/01-where-is-cms.md` | Blog、News、お知らせなど対象Collectionが見える |
| C-03 | P0 | `c-03-collection-items-list.png` | 対象Collectionの記事一覧 | `03-cms/02-create-new-post.md` | 既存記事一覧、検索欄、New itemが見える |
| C-04 | P0 | `c-04-new-item-button.png` | New itemを押す直前 | `03-cms/02-create-new-post.md` | 新規追加ボタンを明確にする |
| C-05 | P0 | `c-05-new-cms-item-form.png` | 新規CMS itemの入力フォーム | `03-cms/02-create-new-post.md` | Name、Slug、Save、Publishなど全体が分かる |
| C-06 | P0 | `c-06-title-field.png` | Title / Name欄を入力している状態 | `03-cms/03-post-title.md` | 必須項目であることが分かる |
| C-07 | P0 | `c-07-thumbnail-field.png` | サムネイル画像欄 | `03-cms/04-thumbnail-image.md` | Thumbnail / Main image、Uploadが見える |
| C-08 | P1 | `c-08-category-dropdown.png` | カテゴリー選択欄を開いた状態 | `03-cms/05-post-category.md` | Category候補、選択状態が分かる |
| C-09 | P0 | `c-09-rich-text-body.png` | Rich Text本文欄 | `03-cms/06-write-body.md` | 本文入力欄、ツールバー、見出しが見える |
| C-10 | P1 | `c-10-rich-text-formatting.png` | 太字・斜体メニュー | `03-cms/07-bold-italic-body.md` | Bold、Italic、選択テキストが分かる |
| C-11 | P1 | `c-11-heading-menu.png` | 見出し設定メニュー | `03-cms/08-headings.md` | Heading 2 / Heading 3などが分かる |
| C-12 | P1 | `c-12-list-menu.png` | 箇条書きメニュー | `03-cms/09-bullet-list.md` | Bullet list / Numbered listが分かる |
| C-13 | P0 | `c-13-insert-image-menu.png` | 本文中に画像を入れるメニュー | `03-cms/10-insert-image.md` | `+` ボタン、Image選択が見える |
| C-14 | P1 | `c-14-image-resize-menu.png` | 本文画像のサイズ変更メニュー | `03-cms/11-resize-image.md` | Small、Medium、Full widthなどが分かる |
| C-15 | P1 | `c-15-youtube-embed-url.png` | YouTube埋め込みURL入力 | `03-cms/12-embed-youtube.md` | YouTube URLを貼る場所が分かる。実動画URLは公開OKのもの |
| C-16 | P1 | `c-16-rich-text-link-settings.png` | 本文リンク設定画面 | `03-cms/13-body-link.md` | URL欄、Open in new tab設定が見える |
| C-17 | P1 | `c-17-publish-date-field.png` | 公開日フィールド | `03-cms/14-publish-date.md` | Published on、Date入力欄が見える |
| C-18 | P1 | `c-18-schedule-publish.png` | 予約公開設定 | `03-cms/15-schedule-publish.md` | Schedule、日時指定が分かる |
| C-19 | P0 | `c-19-save-as-draft.png` | Save as Draft操作 | `03-cms/16-save-as-draft.md` | 下書き保存ボタンと状態が見える |
| C-20 | P0 | `c-20-publish-cms-item.png` | CMS itemをPublishする操作 | `03-cms/17-publish-draft.md` | Publishボタンと公開状態が見える |
| C-21 | P1 | `c-21-edit-published-item.png` | 公開済み記事の再編集画面 | `03-cms/18-edit-published.md` | Published状態とSave changesが分かる |
| C-22 | P1 | `c-22-unpublish-item.png` | Unpublish操作 | `03-cms/19-unpublish.md` | Unpublish、Cancelが分かる |
| C-23 | P1 | `c-23-archive-item.png` | Archive操作 | `03-cms/20-archive-post.md` | Archive、確認画面が分かる |
| C-24 | P1 | `c-24-delete-item-warning.png` | Delete前の警告画面 | `03-cms/21-delete-post.md` | 削除が不可逆だと分かる。実削除はしない |
| C-25 | P1 | `c-25-image-alt-field.png` | 画像alt入力欄 | `03-cms/22-image-alt.md` | altテキスト欄と対象画像が分かる |
| C-26 | P1 | `c-26-cms-sort-settings.png` | CMS一覧の並び順設定または公開ページの並び | `03-cms/23-reorder-cms-items.md` | 並び順の根拠が分かる画面 |
| C-27 | P1 | `c-27-asset-file-upload.png` | PDFなどファイルをAssetへアップロード | `03-cms/24-attach-file.md` | Upload、ファイル名、Copy linkが分かる。実資料名は公開OKのもの |
| C-28 | P0 | `c-28-cms-before-publish-preview.png` | CMS記事の公開前プレビュー | `03-cms/25-cms-before-publish-checklist.md` | 詳細ページと一覧ページの確認に使える画面 |

## D. Designer

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| D-01 | P0 | `d-01-designer-opened.png` | DesignerでBooostトップページを開いた状態 | `04-designer/01-designer-warning.md` | 左右パネル、キャンバス、上部バーが見える |
| D-02 | P0 | `d-02-edit-homepage-text.png` | トップページ見出しテキストを選択している状態 | `04-designer/02-edit-homepage-text.md` | 変更対象テキストだけを選んでいる |
| D-03 | P1 | `d-03-footer-address-text.png` | フッターや会社情報の住所テキスト | `04-designer/03-edit-address.md` | 住所・電話番号など複数箇所確認が必要と分かる |
| D-04 | P1 | `d-04-logo-selected.png` | ロゴ画像を選択している状態 | `04-designer/04-replace-logo.md` | ロゴ、選択枠、右パネルが見える |
| D-05 | P1 | `d-05-asset-panel-open.png` | Asset Panelを開いた状態 | `04-designer/05-asset-panel.md` | Asset一覧、Upload、検索が見える |
| D-06 | P1 | `d-06-delete-asset-warning.png` | Asset削除前の確認画面 | `04-designer/06-delete-asset.md` | Delete前の警告が分かる。実削除はしない |
| D-07 | P0 | `d-07-designer-publish-modal.png` | DesignerのPublishモーダル | `04-designer/07-publish-button.md` | 公開対象ドメイン、Publish to selected domainsが見える |
| D-08 | P1 | `d-08-undo-redo-buttons.png` | Designer左上のUndo / Redo付近 | `04-designer/08-undo-ctrl-z.md` | Undo / Redo、またはショートカット説明に使える構図 |
| D-09 | P1 | `d-09-unsaved-changes-exit.png` | 保存せず終了・未公開変更の確認画面 | `04-designer/09-discard-designer-changes.md` | 破棄するか戻るか判断できるボタンが見える |
| D-10 | P1 | `d-10-favicon-settings.png` | Favicon設定画面 | `04-designer/10-favicon.md` | Favicon、Webclip、Uploadが分かる |
| D-11 | P1 | `d-11-duplicate-page-menu.png` | Pagesパネルでページ複製メニュー | `04-designer/11-duplicate-page.md` | Duplicate、ページ名、設定メニューが見える |

## E. Locale翻訳

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| E-01 | P0 | `e-01-locale-selector-topbar.png` | Designer上部のLocale selector | `07-localization/00-localization-overview.md`, `01-locale-translation-workflow.md` | 現在のLocaleが一目で分かる |
| E-02 | P0 | `e-02-localization-settings-panel.png` | Settings panel > Localization | `07-localization/00-localization-overview.md` | Primary locale、Secondary localeが分かる |
| E-03 | P0 | `e-03-locales-list.png` | Locale一覧 | `07-localization/06-add-new-locale.md` | Display name、Subdirectory、Publishing statusが見える |
| E-04 | P0 | `e-04-add-locale-entry.png` | Add localeの入口 | `07-localization/06-add-new-locale.md` | Add localeボタンまたは入力入口が見える |
| E-05 | P0 | `e-05-language-country-fields.png` | Language / Country入力 | `07-localization/06-add-new-locale.md` | 確定前の状態で撮る。実変更はしない |
| E-06 | P0 | `e-06-locale-subdirectory.png` | Subdirectory入力欄 | `07-localization/06-add-new-locale.md` | `/en` などURLに関わる項目が見える |
| E-07 | P0 | `e-07-locale-publishing-status.png` | Publishing status | `07-localization/06-add-new-locale.md` | 公開オン・オフが分かる |
| E-08 | P0 | `e-08-select-secondary-locale.png` | Secondary localeを選ぶ直前 | `07-localization/01-locale-translation-workflow.md` | Locale selectorを開いた状態 |
| E-09 | P0 | `e-09-secondary-locale-canvas.png` | Secondary localeのキャンバス | `07-localization/01-locale-translation-workflow.md` | 対象Locale選択後のページ表示 |
| E-10 | P0 | `e-10-static-text-selected.png` | 固定ページのテキスト要素選択 | `07-localization/02-static-page-translation.md` | 翻訳対象テキストと選択状態が分かる |
| E-11 | P0 | `e-11-machine-translate-action.png` | 機械翻訳操作 | `07-localization/02-static-page-translation.md` | Translateボタンや候補が分かる |
| E-12 | P1 | `e-12-translated-static-page-check.png` | 翻訳後の固定ページ表示確認 | `07-localization/02-static-page-translation.md` | ボタンや見出しがはみ出していない |
| E-13 | P0 | `e-13-cms-collection-locale.png` | CMS Collection一覧とLocale切り替え | `07-localization/03-cms-locale-translation.md` | Collectionと対象Localeが同時に分かる |
| E-14 | P0 | `e-14-cms-item-locale-fields.png` | CMS item内のLocaleフィールド | `07-localization/03-cms-locale-translation.md` | Title、Body、SEOなどが見える |
| E-15 | P0 | `e-15-translate-all-fields.png` | Translate all fields操作 | `07-localization/03-cms-locale-translation.md` | 複数フィールド翻訳の入口 |
| E-16 | P1 | `e-16-rich-text-locale-body.png` | Locale版Rich Text本文 | `07-localization/03-cms-locale-translation.md` | 翻訳済み本文、見出し、画像が分かる |
| E-17 | P0 | `e-17-page-seo-locale.png` | LocaleごとのPage title / Meta description | `07-localization/04-localized-seo-ogp.md` | 対象LocaleのSEO欄が分かる |
| E-18 | P0 | `e-18-ogp-locale-settings.png` | LocaleごとのOGP設定 | `07-localization/04-localized-seo-ogp.md` | OGP title、description、imageが見える |
| E-19 | P0 | `e-19-publish-modal-locale.png` | Publish modalでLocale / domain確認 | `07-localization/07-publish-and-reflect-locale.md`, `05-locale-publish-checklist.md` | 公開対象を間違えない構図 |
| E-20 | P0 | `e-20-published-locale-url.png` | 公開後の `/en` などLocale URL | `07-localization/07-publish-and-reflect-locale.md` | ブラウザURLと翻訳ページが見える |
| E-21 | P1 | `e-21-public-locale-switcher.png` | 公開サイト上の言語切り替えUI | `07-localization/05-locale-publish-checklist.md` | Japanese / Englishなど切替UIが見える |
| E-22 | P1 | `e-22-mobile-locale-check.png` | スマホ幅で翻訳ページを確認 | `07-localization/05-locale-publish-checklist.md` | 見出し、CTA、ナビゲーションが崩れていない |

## F. 便利な設定

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| F-01 | P0 | `f-01-site-settings-general.png` | Site settings > General | `05-settings/00-site-settings-complete-guide.md` | 左メニューと基本設定が見える。請求情報は写さない |
| F-02 | P0 | `f-02-seo-settings-overview.png` | Site settings > SEO | `05-settings/01-seo-title.md`, `02-seo-description.md`, `10-search-engine-control.md` | SEO設定の入口が分かる |
| F-03 | P1 | `f-03-page-seo-settings.png` | DesignerのPage settings > SEO | `05-settings/01-seo-title.md`, `02-seo-description.md` | Title tag、Meta description入力欄が見える |
| F-04 | P1 | `f-04-open-graph-settings.png` | Page settings / CMS itemのOpen Graph Settings | `05-settings/03-ogp-image.md` | OGP image、title、descriptionが見える |
| F-05 | P0 | `f-05-forms-list.png` | Site settings > Forms一覧 | `05-settings/04-form-submissions.md`, `05-form-notification-email.md` | フォーム名、Submissions入口が分かる |
| F-06 | P0 | `f-06-form-submissions-list.png` | Form submissions一覧 | `05-settings/04-form-submissions.md` | 個人情報は隠す。日時とフォーム名だけ分かればよい |
| F-07 | P0 | `f-07-email-notification-settings.png` | Email notifications欄 | `05-settings/05-form-notification-email.md`, `06-troubleshooting/06-email-not-arriving.md` | 通知先メール欄。実メールアドレスは隠す |
| F-08 | P0 | `f-08-export-csv-button.png` | Export to CSVボタン | `05-settings/06-form-csv-download.md` | 対象フォーム名、Exportボタンが分かる |
| F-09 | P1 | `f-09-form-fields-designer.png` | Designerでフォーム要素を選択 | `05-settings/07-form-fields.md` | 入力項目、フォーム設定、Submitボタンが見える |
| F-10 | P0 | `f-10-site-access-members.png` | Site access / メンバー権限画面 | `05-settings/08-invite-collaborator.md` | 氏名・メールは隠す。RoleとCan publishが分かる |
| F-11 | P0 | `f-11-publishing-domain-status.png` | PublishingのProduction domain / SSL状態 | `05-settings/09-domain-status.md` | Connected、SSL、Production domainが分かる |
| F-12 | P1 | `f-12-plans-current-plan.png` | Plans画面 | `05-settings/00-site-settings-complete-guide.md` | 現在プラン・アップグレード候補。料金や請求情報は隠す |
| F-13 | P1 | `f-13-custom-code-warning.png` | Custom code画面 | `05-settings/10-search-engine-control.md` | 触るべきでない専門設定として使う。コード内容は隠す |
| F-14 | P1 | `f-14-apps-integrations-overview.png` | Apps & Integrations画面 | `05-settings/00-site-settings-complete-guide.md` | 外部連携画面。実連携先で機密があれば隠す |

## G. トラブル解決・保守

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 差し込み先 | 撮影ポイント |
| --- | --- | --- | --- | --- | --- |
| G-01 | P0 | `g-01-publish-status-check.png` | Publishing画面で公開状態を確認 | `06-troubleshooting/01-cache-not-reflecting.md`, `00-common-checklist.md` | 反映されない時の確認用。対象ドメインが分かる |
| G-02 | P1 | `g-02-image-upload-error-example.png` | 画像アップロードエラーまたは失敗直後 | `06-troubleshooting/02-image-upload-failed.md` | エラー文が読める。実ファイル名は問題なければ表示 |
| G-03 | P1 | `g-03-mobile-broken-example.png` | スマホ幅で表示崩れが分かる例 | `06-troubleshooting/03-mobile-display-broken.md` | 端末幅と崩れ箇所が分かる。再現用のURLも控える |
| G-04 | P1 | `g-04-404-example.png` | 404 Not Found表示 | `06-troubleshooting/04-404-not-found.md` | 公開してよいテストURLで撮る |
| G-05 | P0 | `g-05-backups-list.png` | Backups一覧 | `06-troubleshooting/05-backup-restore.md` | 日時・Preview・Restoreが分かる。実ユーザー名は必要なら隠す |
| G-06 | P0 | `g-06-backup-restore-warning.png` | Restore確認画面 | `06-troubleshooting/05-backup-restore.md` | 復元前警告が見える。実行はしない |
| G-07 | P0 | `g-07-forms-email-troubleshooting.png` | Forms通知設定とSubmissions確認 | `06-troubleshooting/06-email-not-arriving.md` | 送信記録あり・通知先確認の流れが分かる |
| G-08 | P1 | `g-08-maintenance-request-screenshot-example.png` | 相談時に送る画面キャプチャー例 | `06-troubleshooting/07-maintenance-request.md` | URL、困っている箇所、画面全体が分かる |

## 差し替え方針

現在入っている次の汎用画像は、上記の専用キャプチャーに順次差し替えてください。

| 現在の仮画像 | 差し替え先の例 |
| --- | --- |
| `webflow-dashboard-sites.png` | A-01、A-02、A-08など用途別に分ける |
| `webflow-booost-designer.png` | B-02〜B-13、C-28、D-01〜D-11、E-01〜E-22へ専用画像で置き換える |
| `webflow-booost-general.png` | F-01、E-03〜E-07、G-08などへ専用画像で置き換える |
| `webflow-booost-forms.png` | F-05〜F-09、G-07へ専用画像で置き換える |
| `webflow-booost-seo.png` | F-02〜F-04、E-17〜E-18へ専用画像で置き換える |
| `webflow-booost-publishing.png` | E-19、F-11、G-01へ専用画像で置き換える |
| `webflow-booost-backups.png` | G-05、G-06へ専用画像で置き換える |

## 最低限の撮影順

まず全部を撮り切るのが難しい場合は、次の順で進めてください。

1. A-01〜A-03: DashboardとSite settingsの入口
2. B-01〜B-09: Content editorの基本操作
3. C-01〜C-10、C-19〜C-20: CMS新規投稿の基本
4. F-05〜F-08: Forms、通知、CSV
5. E-01〜E-09、E-19〜E-20: Localeの入口と公開
6. G-01、G-05〜G-07: トラブル時に使う確認画面

## 詳細撮影指示

上の一覧だけでは撮影場所が迷いやすいため、実際に撮る時は下の詳細指示を見てください。各キャプチャーは「画面への入り方」「撮影直前の状態」「必ず写すもの」を満たしていればOKです。

### 共通の撮り方

- まず対象ページを開き、3〜5秒待ってから撮影する。
- 画面左上や左メニューなど、今どの画面にいるか分かる情報をできるだけ入れる。
- ボタンだけを拡大しすぎず、押す場所と周辺の文脈が同時に分かる構図にする。
- クリック後に保存・公開・削除・復元が実行される画面では、実行前の確認画面で止める。
- 個人情報や未公開情報が出る場合は、撮影前に隠すか、公開してよいテストデータに差し替える。

### A. はじめの一歩

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| A-01 | Webflowにログインし、DashboardのSites一覧を開く。 | 対象のBOOSTサイトカードが見える位置までスクロールし、何もメニューを開かない状態で撮る。 | Workspace名、対象サイトカード、サイトサムネイル、サイト名、Dashboardであることが分かる左上または上部。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-02 | DashboardのSites一覧で対象サイトカードまで移動する。 | 対象サイトカードにマウスを乗せ、Open / Settings / Designerなどのアクションが表示された瞬間に撮る。 | サイトカード全体、表示されたボタン、カーソル位置、通常開く入口とDesigner入口の違い。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-03 | 対象サイトカードからSite settingsまたはSettingsを開く。 | Site settingsの左メニューが表示され、Generalなどのメニューが見える状態で撮る。 | 左メニュー、General、Publishing、SEO、Forms、Backups、現在見ているサイト名。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-04 | GmailなどでWebflowから届いた招待メールを開く。 | Accept Invitationボタンが見える位置にスクロールし、個人情報を隠して撮る。 | Webflowからの招待メールであること、Accept Invitationボタン、差出人、件名。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-05 | 招待メールのAccept Invitationを開き、アカウント作成画面を表示する。 | 入力前の空欄状態で止める。実名やメールを入力した後は撮らない。 | Full name、Email、Password、Create accountボタン。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-06 | Webflowのログイン画面を開く。 | メールアドレス・パスワード未入力の状態で撮る。パスワード再設定ページでも同じ構図で撮る。 | Email、Password、Log in、Forgot passwordの位置。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-07 | WebflowログインURLまたは対象サイトのログインURLをChromeで開く。 | アドレスバーのブックマーク操作が見える状態にする。 | アドレスバー、ブックマーク星アイコン、保存先フォルダ、ログインURLの一部。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-08 | Dashboardの対象サイトカードを表示する。 | Content editorで開く入口とDesignerで開く入口が同時に見える状態にする。 | Content editor側の入口、Designer側の入口、サイトカード、押し間違えない比較。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-09 | Webflow画面をChromeで開き、IGNITEのWebflow日本語化拡張機能またはChrome翻訳メニューを開く。 | 拡張機能が有効で、Webflow画面の英語UIと日本語化の関係が分かる状態で撮る。 | Chrome拡張機能メニュー、Webflow画面、翻訳・日本語化が有効な状態。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |
| A-10 | DashboardまたはDesignerを開く。 | Dashboard、Designer、Publishなど英語UIが読み取れる画面で止める。 | 英語UIの用語、上部バーまたは左メニュー、用語表と対応できる画面。 | 個人名、メールアドレス、Workspace内の不要なサイト、請求情報は写さない。 |

### B. Content Editor

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| B-01 | Dashboardで対象サイトカードを表示する。 | Content editor roleで開く入口が見える状態にする。 | 対象サイトカード、Content editor入口、Designerではないことが分かる周辺UI。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-02 | Content editor roleでBOOSTサイトを開く。 | ページが完全に読み込まれ、上部バーとキャンバスが見える状態で撮る。 | 上部バー、サイトキャンバス、編集可能なページの見た目、ロード完了状態。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-03 | Content editorで編集対象ページを開く。 | 編集できる見出しまたは本文にマウスを乗せる。 | 対象テキスト、編集可能な枠、編集アイコン、周辺の見出し。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-04 | Content editorで編集可能なテキストをクリックする。 | 入力カーソルが出て、テキストが編集状態になったところで撮る。 | 入力カーソル、選択中テキスト、変更対象の文脈。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-05 | Content editorで本文テキストをドラッグ選択する。 | テキスト装飾ツールバーが表示された状態で撮る。 | 選択範囲、Boldボタン、ツールバー全体。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-06 | Content editorでリンク付きテキストまたはボタンを選択する。 | リンク設定パネルまたはポップアップを開いた状態で撮る。 | URL入力欄、Open in new tab、保存ボタン、対象リンク。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-07 | Content editorで画像があるページを開く。 | 差し替えたい画像にマウスを乗せ、画像編集アイコンが出た状態で撮る。 | 画像全体、選択枠、画像編集アイコン、対象画像だけを選んでいる状態。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-08 | B-07の画像編集アイコンを押す。 | 画像アップロードまたはReplace画面が開いた状態で止める。 | Upload、Replace、Choose image、ファイル選択入口。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-09 | Content editorで軽微なテスト変更後、公開前状態にする。 | Publishボタンが押せる状態で、まだ押さずに撮る。 | Publishボタン、保存状態、公開対象、上部バー。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-10 | Content editorで未公開の変更がある状態にする。 | 閉じる、戻る、Discardなどの確認画面を表示して撮る。 | Discard、Cancel、Saveなど判断に必要なボタン。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-11 | Content editorで外部リンク付きテキストまたはボタンを選択する。 | リンク設定でOpen in new tabの項目が見える状態にする。 | 外部URL、Open in new tab設定、対象リンク。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-12 | ページ内リンクがあるページを開く。 | リンク元とリンク先セクションが分かる位置、またはアンカー設定が見える状態で撮る。 | リンク元、リンク先見出し、セクションIDまたはアンカー名。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |
| B-13 | Content editorで変更後のページを表示する。 | Publish前にページ全体を見直している状態で撮る。 | 変更済みテキスト、差し替え画像、リンク導線、上部バー。 | 未公開情報、顧客名、フォーム送信内容、編集不要な管理画面は写さない。 |

### C. CMS更新

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| C-01 | DesignerまたはContent editorの左メニューからCMS / Collectionsを開く。 | CMSの入口が左メニュー上で分かる状態で撮る。 | Collectionsタブ、CMSアイコン、対象サイト名。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-02 | CMS / Collectionsを開く。 | Collection一覧でBlog、News、お知らせなどが見える状態で撮る。 | Collection名、Item数、対象Collectionがどれか分かる周辺UI。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-03 | 対象Collectionをクリックする。 | 記事一覧が表示され、検索欄とNew itemが見える状態で撮る。 | 既存記事一覧、検索欄、New itemボタン、Collection名。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-04 | C-03の記事一覧画面を開く。 | New itemボタンが見える位置で止め、クリック直前の状態で撮る。 | New itemボタン、Collection名、記事一覧の一部。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-05 | New itemをクリックする。 | 新規CMS itemフォームが開いた直後、入力前の状態で撮る。 | Name、Slug、Save、Publish、主要フィールド。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-06 | 新規または既存CMS itemフォームを開く。 | Title / Name欄にカーソルを置き、入力欄が分かる状態で撮る。 | Title / Name欄、必須表示、入力例が必要ならテスト文言。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-07 | CMS itemフォームでサムネイルまたはMain image欄までスクロールする。 | Upload / Choose imageボタンが見える状態で撮る。 | Thumbnail / Main image欄、Uploadボタン、現在画像の有無。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-08 | CMS itemフォームでCategory欄を開く。 | ドロップダウン候補が表示された状態で撮る。 | Category欄、候補リスト、選択済み表示。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-09 | CMS itemフォームでRich Text本文欄までスクロールする。 | 本文欄とツールバーが見える状態で撮る。 | Rich Text欄、ツールバー、本文入力位置、見出し。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-10 | Rich Text本文の一部を選択する。 | 装飾ツールバーが出た状態で撮る。 | 選択テキスト、Bold、Italic、リンクなどのツールバー。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-11 | Rich Text本文で見出しにしたい行を選択する。 | Headingメニューを開いた状態で撮る。 | Heading 2、Heading 3などの候補、対象行。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-12 | Rich Text本文で箇条書きにしたい行を選択する。 | リストメニューを開いた状態で撮る。 | Bullet list、Numbered list、対象テキスト。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-13 | Rich Text本文の画像を入れたい位置にカーソルを置く。 | 追加メニューを開き、Image選択が見える状態で撮る。 | プラスボタン、Imageメニュー、挿入位置。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-14 | Rich Text本文内の画像を選択する。 | 画像サイズ変更メニューが表示された状態で撮る。 | Small、Medium、Full widthなどのサイズ選択、対象画像。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-15 | Rich Text本文でEmbed / Video挿入を開く。 | YouTube URL入力欄が見える状態で撮る。 | YouTube URL入力欄、Embedボタン、公開OKの動画URL。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-16 | Rich Text本文でリンクにしたいテキストを選択する。 | リンク設定ポップアップを開いた状態で撮る。 | URL欄、Open in new tab、選択テキスト。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-17 | CMS itemフォームで公開日フィールドまでスクロールする。 | Published onやDate欄が見える状態で撮る。 | 日付入力欄、カレンダー、公開日ラベル。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-18 | CMS itemのPublish / Schedule操作へ進む。 | Schedule日時指定画面を開き、実行前で止める。 | Scheduleボタン、日時入力、タイムゾーン表示。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-19 | CMS itemフォームを編集した状態にする。 | Save as DraftボタンまたはDraft状態が見える状態で撮る。 | Save as Draft、Draftラベル、保存ボタン。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-20 | 下書きCMS itemを開く。 | Publishボタンが見える状態で、クリック前に撮る。 | Publishボタン、公開状態、対象Item名。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-21 | 公開済みCMS itemを開く。 | Published状態とSave changesが見える状態で撮る。 | Publishedラベル、Save changes、変更対象フィールド。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-22 | 公開済みCMS itemの公開設定を開く。 | Unpublishボタンまたは確認画面が見える状態で撮る。 | Unpublish、Cancel、公開中ステータス。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-23 | CMS item一覧またはItem設定メニューを開く。 | Archive操作または確認画面を表示して撮る。 | Archive、確認メッセージ、Cancel。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-24 | CMS itemの削除メニューを開く。 | Delete確認画面で止め、絶対に実行せず撮る。 | Delete警告、Cancel、対象Item名。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-25 | CMS itemフォームで画像フィールドまたは画像設定を開く。 | altテキスト入力欄が見える状態で撮る。 | alt欄、対象画像、説明文の入力位置。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-26 | CMS一覧、Collection settings、または公開ページの並び順が分かる画面を開く。 | 並び順を決めている項目が見える状態で撮る。 | Sort項目、日付、Orderフィールド、公開ページの表示順。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-27 | DesignerまたはAsset Panelを開く。 | PDFなどファイルをアップロード済み、またはアップロード入口が見える状態で撮る。 | Upload、ファイル名、Copy link、公開OKの資料名。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |
| C-28 | CMS記事の詳細ページまたは一覧ページをプレビューする。 | 公開前チェックで見るべき画面全体が分かる状態で撮る。 | 記事タイトル、本文、画像、一覧への反映、スマホ確認が必要な導線。 | 実在の記事タイトル、未公開記事、顧客名、社内メモ、個人情報は写さない。 |

### D. Designer

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| D-01 | DashboardからDesignerでBOOSTサイトを開く。 | Designerが完全に読み込まれ、左右パネルとキャンバスが表示された状態で撮る。 | 左パネル、キャンバス、右パネル、上部バー、Designerであること。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-02 | Designerでトップページを開く。 | トップページ見出しテキストを選択し、テキスト編集対象が分かる状態で撮る。 | 選択枠、見出し、Navigatorまたは右パネルのテキスト設定。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-03 | Designerでフッターまたは会社情報セクションまで移動する。 | 住所テキストを選択し、周辺情報も見える状態で撮る。 | 住所、電話番号、会社情報ブロック、選択枠。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-04 | Designerでロゴがあるヘッダーを表示する。 | ロゴ画像を選択し、右パネルまたは画像設定が見える状態で撮る。 | ロゴ、選択枠、画像設定、Asset参照。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-05 | Designer左メニューからAsset Panelを開く。 | Asset一覧とUploadボタンが見える状態で撮る。 | Asset一覧、Upload、検索欄、サムネイル。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-06 | Asset Panelで不要なテスト画像の設定を開く。 | Delete確認画面または削除前メニューで止める。 | Delete警告、対象Asset、Cancel。実削除しない。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-07 | Designer右上のPublishをクリックする。 | Publish modalが開いた状態で、Publish実行前に撮る。 | 公開対象ドメイン、Publish to selected domains、ステージングと本番の違い。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-08 | Designer画面左上または上部バーを表示する。 | Undo / Redoアイコンが見える状態で撮る。 | Undo、Redo、上部バー、ショートカット説明に使える位置。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-09 | Designerで未保存または未公開の変更がある状態にする。 | 閉じる、戻る、Discard確認画面で止める。 | Discard、Cancel、未保存変更の警告。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-10 | Site settingsまたはDesignerのFavicon設定を開く。 | Favicon / Webclipアップロード欄が見える状態で撮る。 | Favicon、Webclip、Upload、現在設定画像。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |
| D-11 | DesignerのPages panelを開く。 | ページの設定メニューからDuplicateが見える状態で撮る。 | Pages panel、対象ページ名、Duplicateメニュー。 | 本番サイトを壊す操作、削除確定、Publish実行、Custom codeの中身は写さない。 |

### E. Locale翻訳

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| E-01 | DesignerでBOOSTサイトを開く。 | 上部バーのLocale selectorが見える状態で撮る。 | Locale selector、現在のLocale、ページキャンバス。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-02 | DesignerまたはSite settingsでLocalization設定を開く。 | Primary localeとSecondary localeが見える状態で撮る。 | Localization見出し、Primary locale、Secondary locale、言語名。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-03 | Localization設定でLocales一覧を開く。 | Locale一覧全体が見える位置で撮る。 | Display name、Subdirectory、Publishing status、既存Locale。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-04 | Localization設定のLocales一覧を開く。 | Add localeボタンまたは追加入口が見える状態で撮る。 | Add locale、Locales一覧、設定画面の場所。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-05 | Add localeを開く。 | Language / Country入力画面で、確定前に止める。 | Language、Country、追加ボタン、Cancel。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-06 | Add localeまたはLocale settingsを開く。 | Subdirectory入力欄が見える状態で撮る。 | Subdirectory、URL例、保存前状態。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-07 | Locale settingsを開く。 | Publishing statusのオン・オフが見える状態で撮る。 | Publishing status、Enable publishing、対象Locale名。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-08 | Designer上部のLocale selectorをクリックする。 | Secondary localeを選ぶ直前、候補リストが開いた状態で撮る。 | Locale selector、Primary / Secondary候補、現在選択中のLocale。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-09 | Locale selectorでSecondary localeを選択する。 | Secondary localeのキャンバスが完全に読み込まれた状態で撮る。 | 対象Locale名、ページ表示、上部バー。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-10 | Secondary localeで固定ページを開く。 | 翻訳対象の見出しまたは本文テキストを選択する。 | 選択テキスト、対象ページ、翻訳前後が分かる文脈。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-11 | 翻訳対象テキストを選択する。 | Translate操作または翻訳候補が見える状態で撮る。 | Translateボタン、候補、対象テキスト。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-12 | 翻訳後の固定ページを表示する。 | 見出し、本文、ボタンが収まっているか分かる構図で撮る。 | 翻訳後見出し、CTA、余白、文字のはみ出し有無。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-13 | Locale選択後にCMS / Collectionsを開く。 | CMS Collection一覧とLocaleが同時に分かる状態で撮る。 | Collection名、Locale selector、記事一覧入口。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-14 | 対象CMS itemをSecondary localeで開く。 | Title、Body、SEOなどLocaleごとのフィールドが見える状態で撮る。 | Locale名、Title、Body、SEOフィールド。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-15 | CMS itemのLocale版編集画面を開く。 | Translate all fieldsボタンまたは一括翻訳入口が見える状態で撮る。 | Translate all fields、対象フィールド、Locale名。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-16 | Locale版CMS itemのRich Text本文を開く。 | 翻訳済み本文と画像が見える位置で撮る。 | 見出し、本文、画像、リンク、Locale表示。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-17 | Page settingsまたはCMS itemのSEO欄を開く。 | 対象LocaleのPage title / Meta descriptionが見える状態で撮る。 | Locale名、Page title、Meta description、Slug。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-18 | Page settingsまたはCMS itemのOpen Graph欄を開く。 | OGP title、description、imageが見える状態で撮る。 | OGP title、description、OGP image、Locale名。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-19 | Designer右上のPublishを開く。 | Localeや公開対象ドメインを確認できるPublish modalで止める。 | 公開対象ドメイン、Locale、Publishボタン、実行前状態。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-20 | 公開後のLocale URLをブラウザで開く。 | /enなどのURLと翻訳済みページが見える状態で撮る。 | アドレスバー、Locale URL、翻訳済み見出し、ページ本文。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-21 | 公開サイトを開く。 | 言語切り替えUIを開いた状態で撮る。 | 言語切り替えメニュー、日本語/英語などの選択肢、現在言語。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |
| E-22 | 公開サイトの翻訳ページをスマホ幅で開く。 | ヘッダー、見出し、CTAが収まっている状態で撮る。 | スマホ幅、ナビ、見出し、CTA、表示崩れがないこと。 | 未確定のLocale追加、非公開URL、顧客名、社内コメント、分析数値は写さない。 |

### F. 便利な設定

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| F-01 | 対象サイトのSite settingsを開く。 | General画面の左メニューと基本設定が見える状態で撮る。 | General、サイト名、左メニュー、基本設定。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-02 | Site settingsを開き、SEOをクリックする。 | SEO設定の入口や主要項目が見える状態で撮る。 | SEOメニュー、Indexing関連、設定見出し。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-03 | DesignerのPages panelからPage settingsを開く。 | SEO settings内のTitle tagとMeta descriptionが見える状態で撮る。 | Title tag、Meta description、ページ名。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-04 | Page settingsまたはCMS itemのOpen Graph settingsを開く。 | OGP imageやtitle欄が見える状態で撮る。 | OGP title、description、image、Uploadまたは画像選択。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-05 | Site settingsを開き、Formsをクリックする。 | Forms一覧でフォーム名とSubmissions入口が見える状態で撮る。 | Formsメニュー、フォーム名、Submissions入口。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-06 | 対象フォームのSubmissionsを開く。 | 個人情報を隠し、一覧の構造が分かる状態で撮る。 | 送信日時、フォーム名、一覧テーブル、個人情報を隠した状態。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-07 | 対象フォームの設定を開く。 | Email notifications欄が見える位置までスクロールして撮る。 | Email notifications、通知先欄、Add email address、メールはマスク。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-08 | Form submissions画面を開く。 | Export to CSVボタンが見える状態で撮る。 | 対象フォーム名、Export to CSV、送信一覧の一部。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-09 | Designerでフォームがあるページを開く。 | フォーム要素を選択し、設定パネルが見える状態で撮る。 | 入力項目、Submitボタン、フォーム設定、選択枠。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-10 | Site settingsでSite accessまたはMembersを開く。 | メンバー一覧とRoleが見える状態で、個人情報を隠して撮る。 | Role、Can publish、招待ボタン、メールはマスク。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-11 | Site settingsでPublishingを開く。 | Production domainとSSL状態が見える状態で撮る。 | Production domain、Connected、SSL、Publish先。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-12 | Site settingsでPlansを開く。 | 現在プランとアップグレード候補が分かる状態で、請求情報を隠して撮る。 | Current plan、CMS plan、Upgrade導線、料金やカード情報は隠す。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-13 | Site settingsでCustom codeを開く。 | Custom code欄があることだけ分かる状態で、コード内容は隠して撮る。 | Custom code見出し、Head / Footer code欄、触らない注意に使う構図。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |
| F-14 | Site settingsでApps & Integrationsを開く。 | 連携一覧が見える状態で、機密連携情報を隠して撮る。 | Apps & Integrations見出し、連携カード、設定入口。 | メールアドレス、フォーム送信本文、請求情報、API key、外部連携の機密情報は写さない。 |

### G. トラブル解決・保守

| ID | 画面への入り方 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- |
| G-01 | Site settingsでPublishingを開く。 | 公開状態や対象ドメインが分かる状態で撮る。 | Publish状態、対象ドメイン、Production / Stagingの違い。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-02 | 画像アップロード時のエラーを再現できるテスト画像を用意する。 | エラー表示が出た直後、メッセージが読める状態で撮る。 | エラー文、対象ファイル名、アップロード場所。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-03 | 公開サイトまたはPreviewをスマホ幅で開く。 | 表示崩れ箇所が画面内に入る状態で撮る。 | スマホ幅、崩れ箇所、URL、比較しやすい周辺要素。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-04 | 公開してよい存在しないテストURLを開く。 | 404 Not Found画面が表示された状態で撮る。 | アドレスバー、404表示、サイト側のエラーページ。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-05 | Site settingsでBackupsを開く。 | Backups一覧が表示され、日時とPreview / Restoreが見える状態で撮る。 | Backup日時、Preview、Restore、作成者名は必要なら隠す。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-06 | Backups一覧でRestoreを押す直前または確認画面を開く。 | Restore確認画面で止め、実行せず撮る。 | Restore警告、Cancel、対象バックアップ日時。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-07 | Site settingsのFormsとEmail notificationsを確認する。 | 送信記録あり、通知先確認の流れが分かる画面で撮る。 | Submissions一覧、Email notifications、通知先はマスク。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |
| G-08 | 相談用の例として、公開してよいページまたはテスト画面を開く。 | 困っている箇所が分かるよう、URLと問題箇所を同時に入れて撮る。 | アドレスバー、問題箇所、ページ全体の文脈、問い合わせで送るべき情報。 | 個人情報、問い合わせ本文、実ユーザー名、機密URL、削除・復元の実行完了画面は写さない。 |

