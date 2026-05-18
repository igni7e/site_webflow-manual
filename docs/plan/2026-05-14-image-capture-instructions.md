---
title: "2026-05-14 画像撮影指示書作成計画"
description: "Webflow更新マニュアルに後から差し込むスクリーンショットの撮影指示を整理する計画"
sidebar:
  order: 8
---

# 2026-05-14 画像撮影指示書作成計画

- [x] 既存ページの画像配置と不足箇所を確認する
- [x] 章別の撮影方針を決める
- [x] ページ別に撮影すべき画面、強調箇所、保存名を整理する
- [x] 撮影時の共通ルールをまとめる
- [x] ビルドと差分を確認する

## 方針

- 公開マニュアル本文には未撮影の仮画像を大量に出さず、まず撮影指示書として整理する。
- 後から手動撮影またはブラウザキャプチャで差し替えやすいよう、ファイル名、撮影対象、強調箇所を明確にする。
- 個人情報、クライアント固有名、メールアドレス、フォーム送信内容は写さない。
- 絵文字は使わない。

## 共通ルール

- 画面サイズは原則としてデスクトップ幅 `1440px` で撮影する。スマートフォン確認が主題のページだけ、追加で `390px` 幅を撮る。
- キャプチャーは原則としてIGNITEが保有するBOOSTのWebflowサイトを使って撮影する。
- BOOST上のサイト名、ユーザー名、メールアドレス、請求情報、フォーム送信者情報、公開前コンテンツは必ずぼかす。
- ボタンや入力欄を説明する画像では、赤枠や番号などを後から載せやすいよう、対象の周囲に余白を残す。
- 画像ファイルは `src/assets/captures/` に置く。ファイル名は `カテゴリ番号-ページ番号-内容.svg` または実画面なら `.png` にする。
- 既存のイメージSVGを実画面キャプチャに差し替える場合も、同じファイル名を使うと本文側の修正が少なく済む。
- 1ページに入れる画像は、基本は2〜4枚。操作が短いページは1〜2枚、CMSやDesignerのように迷いやすいページは4〜6枚まで許容する。
- 画像直下の注釈は `※画面は撮影時点のものです。WebflowのUI変更により表示が異なる場合があります。` に統一する。

## AI撮影担当者への共通指示

AIがキャプチャーを撮る場合は、各ページで以下の順番を守る。

1. 対象ページの本文を読み、どの操作を説明しているページか確認する。
2. BOOSTのWebflowサイトを開く。実データが写る画面では、撮影前にぼかす対象を確認する。
3. 指示された画面状態まで操作する。途中で本番公開、削除、課金、招待送信は実行しない。
4. 撮影前に、個人名、メールアドレス、問い合わせ内容、請求情報、アクセス権限一覧、クライアント固有名が写っていないか確認する。
5. 撮影対象のボタン・入力欄・パネルが画面内で見切れていないことを確認する。
6. 可能なら撮影後に赤枠・番号・短いラベルを追加する。ラベル文言は本文内の用語に合わせる。
7. 保存名はこの指示書の保存名案に合わせる。
8. 画像を本文へ差し込む時は、該当手順の直後に置く。

## AI向けキャプチャー指示テンプレート

各キャプチャーは、最低限この粒度で指示する。

```md
<details>
<summary>キャプチャー指示: 画像の目的</summary>

- 保存名: `カテゴリ-ページ-内容.png`
- 差し込み位置: 「該当セクション名」の直後
- 撮影画面: Webflowのどの画面を開くか
- 事前状態: どのサイト、どのCollection、どのページ、どの入力状態にするか
- 強調箇所: 赤枠や番号で示すボタン・入力欄・メニュー
- 隠す情報: サイト名、メール、フォーム内容など
- 撮影後チェック: 何が写っていれば成功か

</details>
```

## 本文へ入れる撮影指示ブロックの書式

公開ページ内に撮影指示を残す場合は、読者の邪魔にならないよう折りたたみ式にする。

```md
<details>
<summary>キャプチャー指示</summary>

- 保存名: `03-24-attach-file-asset-upload.png`
- 差し込み位置: `Step 1: アセットにファイルをアップロード` の直後
- 撮影画面: Asset ManagerでPDFをアップロードする直前の画面
- 強調箇所: `Upload` ボタン、アップロード対象ファイル名、Asset Managerの検索欄
- 隠す情報: 実在のクライアント名、社内資料名、メールアドレス
- 撮影後チェック: PDFがAsset一覧に表示され、リンクコピー前の状態が分かること

</details>
```

このブロックは、実キャプチャーを入れた後に削除してもよい。

## 章別の撮影方針

| 章 | 画像の役割 | 優先度 |
| --- | --- | --- |
| 01 はじめの一歩 | ログイン、Dashboard、押してよいボタンと避けるボタンを見分ける | 高 |
| 02 Editor | 実際に文章、画像、リンクを更新する画面を見せる | 高 |
| 03 CMS | Collection、CMS item、本文エディタ、公開状態を見せる | 高 |
| 04 Designer | 注意喚起が必要な画面、Locale selector、Publish操作を見せる | 中 |
| 05 Settings | Forms、SEO、OGP、CSV、通知先など設定画面を見せる | 高 |
| 06 Troubleshooting | エラー例、確認すべき状態、連絡時に必要な情報を見せる | 中 |

## 01 はじめの一歩

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-invitation-email.md` | Webflow招待メールのサンプル | 招待ボタン、送信元、期限表示 | `01-01-invitation-email.png` |
| `02-create-account.md` | アカウント作成画面 | 名前、メール、パスワード入力欄 | `01-02-create-account.png` |
| `03-first-login.md` | 初回ログイン後のWebflow Dashboard | 対象サイトカード | `01-03-first-login-dashboard.png` |
| `04-bookmark-login.md` | ブックマーク登録済みのChrome画面 | ブックマークバー、WebflowログインURL | `01-04-bookmark-login.png` |
| `05-reset-password.md` | パスワード再設定画面 | メールアドレス入力欄、送信ボタン | `01-05-reset-password.png` |
| `06-dashboard-overview.md` | Dashboardでサイトカードにカーソルを合わせた状態 | Open in Webflow、Site settings、Designerの違い | `01-06-dashboard-site-card.png` |
| `07-editor-vs-designer.md` | Dashboard上のOpen in WebflowとDesigner入口の比較 | 日常更新で使う入口、注意が必要な入口 | `01-07-editor-vs-designer.png` |
| `09-chrome-translate-webflow.md` | Chrome翻訳メニューとIGNITEのWebflow日本語化拡張機能ページ | 翻訳アイコン、拡張機能名、追加ボタン | `01-09-chrome-translate-extension.png` |
| `10-webflow-ui-glossary.md` | Webflow画面上の主要UIに番号を振った説明画像 | Dashboard、Editor、Designer、Publish | `01-10-ui-glossary-overview.png` |
| `11-after-login-first-steps.md` | ログイン直後のDashboardで最初に見る場所 | 対象サイト、Open in Webflow、Site settings | `01-11-after-login-first-steps.png` |

## 02 Editor

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-open-legacy-editor.md` | Dashboardから旧Content Editorを開く流れ | Open Editor (Legacy)、旧版の入口 | `02-01-open-legacy-editor-flow.png` |
| `02-open-content-editor.md` | 最新版Content Editorでサイトを開く流れ | Open in Webflow、編集画面のツールバー | `02-02-open-content-editor-flow.png` |
| `03-edit-text.md` | 編集可能なテキストにカーソルを合わせた状態 | 青枠、編集アイコン、テキスト入力位置 | `02-03-edit-text-target.png` |
| `04-bold-text.md` | テキスト選択後の装飾メニュー | Bold、Italic、リンクメニュー | `02-04-bold-menu.png` |
| `05-add-link.md` | 文章リンクのURL入力欄 | URL欄、Open in new tab | `02-05-add-link-panel.png` |
| `06-replace-image.md` | 画像にカーソルを合わせて編集アイコンが出た状態 | 画像編集アイコン、アップロード入口 | `02-06-replace-image-icon.png` |
| `07-edit-link-url.md` | 既存リンクの設定パネル | 現在のURL、変更後URL、保存操作 | `02-07-edit-link-url.png` |
| `08-save-and-publish.md` | Publish前後の画面 | Publishボタン、公開先、完了メッセージ | `02-08-publish-flow.png` |
| `09-discard-changes.md` | 変更破棄や戻る操作の画面 | 破棄ボタン、戻る導線 | `02-09-discard-changes.png` |
| `10-external-link-new-tab.md` | 外部リンクの新規タブ設定 | Open in new tabのオン状態 | `02-10-open-new-tab.png` |
| `11-anchor-link.md` | アンカーリンク入力例 | `#contact` の入力欄、対象ボタン | `02-11-anchor-link.png` |
| `12-before-publish-checklist.md` | 公開前チェックを行う公開サイトのプレビュー | PC表示、スマートフォン表示、リンク確認 | `02-12-before-publish-check.png` |

## 03 CMS

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-where-is-cms.md` | Collectionsパネル | Collection一覧、対象Collection | `03-01-collections-panel.png` |
| `02-create-new-post.md` | New itemボタンを押す直前 | New item、対象Collection名 | `03-02-new-cms-item.png` |
| `03-post-title.md` | Name、Title、Slug入力欄 | Slugは半角英数字とハイフン | `03-03-title-slug-fields.png` |
| `04-thumbnail-image.md` | サムネイル画像フィールド | 画像アップロード欄、プレビュー | `03-04-thumbnail-field.png` |
| `05-post-category.md` | カテゴリー選択欄 | Dropdown、Multi-referenceの違い | `03-05-category-select.png` |
| `06-write-body.md` | Rich Text本文入力欄 | 本文エリア、ツールバー | `03-06-rich-text-body.png` |
| `07-bold-italic-body.md` | Rich Textの文字装飾メニュー | Bold、Italic | `03-07-rich-text-format.png` |
| `08-headings.md` | 見出しレベル選択メニュー | H2、H3の選択 | `03-08-heading-levels.png` |
| `09-bullet-list.md` | 箇条書きメニュー | Bullet list、Numbered list | `03-09-list-menu.png` |
| `10-insert-image.md` | Rich Text内の画像追加メニュー | 追加ボタン、Image | `03-10-insert-image.png` |
| `11-resize-image.md` | 挿入済み画像のサイズ調整状態 | 画像ハンドル、配置メニュー | `03-11-resize-image.png` |
| `12-embed-youtube.md` | YouTube共有URLとWebflow埋め込み欄 | Share URL、Embed追加欄 | `03-12-youtube-embed.png` |
| `13-body-link.md` | Rich Text内リンク設定 | URL欄、リンク解除アイコン | `03-13-body-link.png` |
| `14-publish-date.md` | 公開日フィールド | Date picker、時刻入力欄 | `03-14-publish-date.png` |
| `15-schedule-publish.md` | Schedule設定画面 | Scheduleボタン、日時確認 | `03-15-schedule-publish.png` |
| `16-save-as-draft.md` | Save as Draftボタン | 下書き保存の状態表示 | `03-16-save-as-draft.png` |
| `17-publish-draft.md` | DraftからPublishする画面 | Draft表示、Publishボタン | `03-17-publish-draft.png` |
| `18-edit-published.md` | Published itemの編集画面 | Save、公開済み状態 | `03-18-edit-published.png` |
| `19-unpublish.md` | Unpublish操作のメニュー | Unpublish、確認ダイアログ | `03-19-unpublish.png` |
| `20-archive-post.md` | Archive操作のメニュー | Archive、Archived状態 | `03-20-archive-post.png` |
| `21-delete-post.md` | Delete操作の確認画面 | Deleteは危険操作であること | `03-21-delete-post.png` |
| `22-image-alt.md` | 画像alt入力欄 | Alt text欄、入力例 | `03-22-image-alt.png` |
| `23-reorder-cms-items.md` | CMS一覧の並び替え画面 | 並び順、ドラッグ操作 | `03-23-reorder-cms-items.png` |
| `24-attach-file.md` | ファイル添付フィールド | File upload、Asset選択 | `03-24-attach-file.png` |
| `25-cms-before-publish-checklist.md` | CMS記事のPreviewと公開サイト | 一覧ページ、詳細ページ、SNS表示 | `03-25-cms-before-publish.png` |

### `03-cms/24-attach-file.md` 詳細キャプチャー指示

このページはPDFや資料ファイルの添付で迷いやすいため、最低3枚入れる。

#### 1枚目: Asset Managerでファイルをアップロードする画面

- 保存名: `03-24-attach-file-asset-upload.png`
- 差し込み位置: `Step 1: アセットにファイルをアップロード` の手順1の直後
- 撮影画面: WebflowのAsset Managerを開いた状態
- 事前状態: デモ用PDF `sample-company-profile.pdf` をアップロードする直前にする
- 強調箇所: `Upload` ボタン、Asset Managerのパネル名、アップロード対象ファイル
- 隠す情報: 実在の社内資料名、顧客名、ファイル一覧にある非公開資料名
- 撮影後チェック: 読者が「まずAsset ManagerでUploadする」と分かること

#### 2枚目: アップロード後にファイルURLをコピーする画面

- 保存名: `03-24-attach-file-copy-url.png`
- 差し込み位置: `Step 1` の手順3の直後
- 撮影画面: アップロード済みPDFの詳細またはメニューを開いた状態
- 事前状態: デモPDFがAsset Manager内に表示されている
- 強調箇所: `Copy URL`、ファイル名、URLを取得するボタン
- 隠す情報: 実URLのドメインに顧客名が入る場合はぼかす
- 撮影後チェック: 本文へ貼るURLをどこで取得するか分かること

#### 3枚目: CMS本文内でリンクを設定する画面

- 保存名: `03-24-attach-file-rich-text-link.png`
- 差し込み位置: `Step 2: 本文にダウンロードリンクを貼る` の手順2の直後
- 撮影画面: CMS Rich Textで「会社案内PDF（2.3MB）」を選択し、リンク設定パネルを開いた状態
- 事前状態: Rich Text本文にダウンロードリンク用テキストを入力しておく
- 強調箇所: 選択したリンクテキスト、リンクアイコン、URL入力欄、`Open in new tab`
- 隠す情報: 実在資料名、未公開記事本文
- 撮影後チェック: 「テキストを選択してURLを貼る」流れが1枚で分かること

#### 4枚目: 公開ページでPDFリンクを確認する画面

- 保存名: `03-24-attach-file-published-check.png`
- 差し込み位置: `Step 2` の後、または公開前チェックの補足として追加
- 撮影画面: 公開ページまたはPreviewでPDFリンクが表示されている状態
- 事前状態: ダウンロードリンクをクリックする直前にする
- 強調箇所: リンクテキスト、リンク先が別タブで開くことを示すブラウザ状態
- 隠す情報: 顧客サイトURL、非公開資料名
- 撮影後チェック: 読者が公開後にリンク確認する必要を理解できること

## 04 Designer

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-designer-warning.md` | Designer画面全体 | Navigator、Style panel、Publishの位置 | `04-01-designer-warning-overview.png` |
| `02-edit-homepage-text.md` | Designerでテキストを選択した状態 | 直接編集できるテキスト、周辺要素 | `04-02-edit-homepage-text.png` |
| `03-edit-address.md` | フッターや共通パーツのテキスト編集画面 | SymbolやComponentの注意箇所 | `04-03-edit-address-symbol.png` |
| `04-replace-logo.md` | ロゴ画像の選択状態 | Asset、Replace image、Style panel | `04-04-replace-logo.png` |
| `05-asset-panel.md` | Asset Panel | Upload、検索、既存Asset | `04-05-asset-panel.png` |
| `06-delete-asset.md` | Asset削除前の確認画面 | Delete、使用中Assetの注意 | `04-06-delete-asset.png` |
| `07-publish-button.md` | DesignerのPublishメニュー | Publish、公開先ドメイン | `04-07-designer-publish.png` |
| `08-undo-ctrl-z.md` | Undo操作または変更履歴の説明画面 | Undo、Redo、操作後確認 | `04-08-undo-redo.png` |
| `09-discard-designer-changes.md` | 変更破棄の確認画面 | Leave、Discard、保存されない変更 | `04-09-discard-designer-changes.png` |
| `10-favicon.md` | Site settingsのFavicon設定 | Favicon、Webclip、Save Changes | `04-10-favicon-settings.png` |
| `11-duplicate-page.md` | ページ複製メニュー | Duplicate、Slug、SEO設定 | `04-11-duplicate-page.png` |
| `00-localization-designer-guide.md` | Locale selectorと翻訳画面 | Locale selector、Translate、対象Locale | `04-00-localization-locale-selector.png` |

## 05 Settings

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-seo-title.md` | SEO SettingsのTitle Tag入力欄 | Title Tag、検索結果プレビュー | `05-01-seo-title.png` |
| `02-seo-description.md` | Meta Description入力欄 | Description、文字数の目安 | `05-02-seo-description.png` |
| `03-ogp-image.md` | Open Graph Settings | OGP画像、タイトル、説明文 | `05-03-ogp-image.png` |
| `04-form-submissions.md` | FormsのSubmissions一覧 | フォーム名、送信履歴、詳細 | `05-04-form-submissions.png` |
| `05-form-notification-email.md` | フォーム通知先設定 | Send form submissions to、Save Changes | `05-05-form-notification-email.png` |
| `06-form-csv-download.md` | Export to CSVボタン | 対象フォーム名、Export to CSV | `05-06-form-csv-download.png` |
| `07-form-fields.md` | Designer上のフォームフィールド | Field settings、Name、Required | `05-07-form-fields.png` |
| `08-invite-collaborator.md` | CollaboratorsまたはMembers招待画面 | Role選択、招待メール欄 | `05-08-invite-collaborator.png` |
| `09-domain-status.md` | Publishing設定のドメイン一覧 | Production domain、SSL、Connected | `05-09-domain-status.png` |
| `10-search-engine-control.md` | Indexingや検索エンジン設定 | サイト全体・ページ単位の公開設定 | `05-10-search-engine-control.png` |
| `00-site-settings-complete-guide.md` | Site settingsの左メニュー全体 | Forms、SEO、Publishing、Plans | `05-00-site-settings-overview.png` |

## 06 Troubleshooting

| ページ | 入れる画像 | 強調箇所 | 保存名案 |
| --- | --- | --- | --- |
| `01-cache-not-reflecting.md` | Chromeの強制再読み込み、シークレットモード | 更新確認の手順 | `06-01-cache-refresh.png` |
| `02-image-upload-failed.md` | 画像アップロードエラーまたはファイル情報 | ファイルサイズ、形式、エラー表示 | `06-02-image-upload-failed.png` |
| `03-mobile-display-broken.md` | PC表示とスマートフォン表示の比較 | 崩れている箇所、端末情報 | `06-03-mobile-display-broken.png` |
| `04-404-not-found.md` | 404画面例 | URLバー、404表示 | `06-04-404-not-found.png` |
| `05-backup-restore.md` | Backups画面 | Restore、日時、確認ダイアログ | `06-05-backup-restore.png` |
| `06-email-not-arriving.md` | Forms送信履歴と通知メール設定 | Webflow上の送信記録、通知先 | `06-06-email-not-arriving.png` |
| `00-common-checklist.md` | トラブル時チェック用の総合図 | Publish、キャッシュ、権限、URL確認 | `06-00-troubleshooting-checklist.png` |

## 優先撮影リスト

最初に撮るべき画像は以下です。ここを揃えるだけで、初心者向けマニュアルとしてかなり読みやすくなります。

1. `01-11-after-login-first-steps.png`
2. `01-06-dashboard-site-card.png`
3. `02-01-open-legacy-editor-flow.png`
4. `02-02-open-content-editor-flow.png`
5. `02-03-edit-text-target.png`
6. `02-06-replace-image-icon.png`
7. `02-08-publish-flow.png`
8. `03-01-collections-panel.png`
8. `03-03-title-slug-fields.png`
9. `03-06-rich-text-body.png`
10. `05-04-form-submissions.png`
11. `05-06-form-csv-download.png`
12. `01-09-chrome-translate-extension.png`

## 後で本文へ差し込む時の書式

```md
![画像の説明](../../../assets/captures/保存名.png)
*※画面は撮影時点のものです。WebflowのUI変更により表示が異なる場合があります。*
```

画像の説明は「何の画面か」が分かる短い日本語にします。例: `DashboardでOpen in Webflowを選ぶ画面`。
