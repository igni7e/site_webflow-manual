---
title: "追加キャプチャー撮影指示書 2026-06-02"
description: "Webflow更新マニュアルに追加で差し込むキャプチャーの撮影指示一覧"
sidebar:
  order: 0
---

# 追加キャプチャー撮影指示書 2026-06-02

## 目的

Webflow更新マニュアル内に残っている「キャプチャー差し込み位置」を、実画面キャプチャーへ置き換えるための追加撮影指示です。

既存の全体リストは `docs/human-capture-shot-list.md` にあります。この指示書では、現時点で本文内に明示的な差し込み位置が残っているものと、今後よく必要になる補足パターンを優先してまとめます。

:::note[IDの見方]
この指示書のIDは、原則としてマニュアルの章番号に対応させます。たとえば `F-6` は「お問い合わせがあった時の通知メールアドレスを変更する方法」、`F-7` は「お問い合わせデータをCSVでダウンロードする方法」です。撮影内容で迷った場合は、IDよりも「差し込み先」のページ内容を優先してください。
:::

## 共通撮影ルール

- Webflow画面を開いたら、すぐ撮らずに3〜5秒待つ。
- `Loading...`、スピナー、白紙、画像未読込、スケルトンUIが残っている状態は使わない。
- 個人名、メールアドレス、問い合わせ本文、未公開記事名、未公開本文、請求情報、カード情報、APIキーは写さない。
- Legacy Editorを主役にした画像は撮らない。通常更新は最新版Content editor roleの画面を優先する。
- Designer画面を撮る場合は、実行前の状態で止め、Publish、Delete、Restore、Clean upなどは押さない。
- 保存先はすべて `src/assets/captures/manual/`。
- 撮影後は、ファイル名、ロード完了、個人情報マスク、画面の文脈が分かるかを確認する。

## P0: 最優先で撮る

| ID | 保存ファイル名 | 差し込み先 | 撮影する画面 | 撮影ポイント |
|---|---|---|---|---|
| B-02A | `b-02-content-editor-first-check.png` | `02-editor/02-open-content-editor.md` | 最新版Content editor roleでサイトを開いた直後 | 正しいサイト名、編集可能要素の青いアウトラインまたは編集アイコン、左側のCMSまたはAssets入口が同時に見える。詳しくは `docs/content-editor-first-check-capture-request-2026-06-02.md` を参照。 |
| B-10 | `b-10-open-in-new-tab-setting.png` | `02-editor/10-external-link-new-tab.md` | リンク設定パネル | 対象テキストを選択し、URL入力欄と `Open in new tab` チェックボックスが見える状態。外部URLは公開してよいサンプルにする。 |
| B-11 | `b-11-anchor-link-url-field.png` | `02-editor/11-anchor-link.md` | アンカーリンクのURL入力欄 | リンク設定パネルで `#contact` のようなIDが入力中だと分かる状態。対象テキストとURL欄を同時に写す。 |
| C-22A | `c-22-body-image-alt-settings.png` | `03-cms/22-image-alt.md` | 本文画像のAlt text設定 | Rich Text本文内の画像を選択し、Alt text欄が表示されている状態。本文や未公開情報は写さない。 |
| C-22B | `c-22-thumbnail-alt-settings.png` | `03-cms/22-image-alt.md` | アイキャッチ画像のAlt text設定 | CMS itemのサムネイル画像フィールドを開き、Alt text欄が見える状態。記事本文や未公開タイトルは隠す。 |
| F-06 | `f-06-form-submissions-export-all.png` | `05-settings/05-form-notification-email.md` | Default form email notifications設定画面 | Formsで通知メール設定を開き、`Send form submissions to` の通知先メール欄が見える状態。実メールアドレスはマスクする。 |
| F-07 | `f-07-form-submissions-export-all.png` | `05-settings/06-form-csv-download.md` | FormsのSubmissions export画面 | `Export all`、`Report spam`、`Delete` の位置関係が分かる状態。送信者名、メール、問い合わせ本文は必ず隠す。 |
| F-08 | `f-08-form-field-settings.png` | `05-settings/07-form-fields.md` | フォーム項目の追加・削除設定 | Designerでフォーム要素またはForm Settingsを開き、入力項目、Required、Field nameなどが分かる状態。変更や削除は実行しない。 |
| F-09A | `f-09-invite-member-role-modal.png` | `05-settings/08-invite-collaborator.md` | Invite member / Invite client の招待モーダル | Seat、Site role、`Content editor`、`Can publish` の判断が分かる状態。メールアドレスは入力しないかマスクする。 |
| WORK-02 | `work-02-cms-items-full-list.png` | `work/02-update-post.md` | CMS CollectionsのBlog記事一覧 | Blog CollectionのItems一覧、テーブル見出し、記事行、左メニューが見える。未公開本文は写さない。 |

## P1: 操作理解を補強する

| ID | 保存ファイル名 | 差し込み先 | 撮影する画面 | 撮影ポイント |
|---|---|---|---|---|
| C-05A | `c-05-multi-reference-categories.png` | `03-cms/05-post-category.md` | 複数カテゴリー選択フィールド | `Categories` または関連カテゴリーの選択肢が開き、複数選択できることが分かる状態。 |
| C-11A | `c-11-rich-text-image-size-menu.png` | `03-cms/11-resize-image.md` | Rich Text画像サイズ変更メニュー | 本文画像を選択し、幅いっぱい、回り込み、元サイズなどの選択肢が分かる状態。 |
| F-03A | `f-03-open-graph-image-setting.png` | `05-settings/03-ogp-image.md` | Page SettingsのOpen Graph Image設定 | ページ名、Open Graph Settings、Open Graph Image欄、Uploadまたは画像選択入口が分かる状態。 |
| F-11A | `f-11-page-indexing-settings.png` | `05-settings/10-search-engine-control.md` | Page SettingsのIndexing / Search settings | `Disable indexing for this page` または `Exclude from sitemap.xml` が見える状態。設定変更は実行しない。 |
| G-00 | `g-00-settings-troubleshooting-check.png` | `06-troubleshooting/00-common-checklist.md` | トラブル時に見るSite settings関連画面 | Forms、Publishing、Backups、または権限確認画面のうち、原因切り分けに使う画面を1つ撮る。個人情報は写さない。 |

## P2: Designer / Asset補足

| ID | 保存ファイル名 | 差し込み先 | 撮影する画面 | 撮影ポイント |
|---|---|---|---|---|
| D-05A | `d-05-asset-panel-replace-image.png` | `04-designer/05-asset-panel.md` | DesignerのImage settingsでReplace Imageが見える画面 | Navigatorから画像を選び、左側Assets Panel、対象画像、Replace Image入口が分かる画角にする。 |
| D-05B | `d-05-asset-delete-used-on-pages.png` | `04-designer/05-asset-panel.md` | Asset削除前のUsed on確認 | 画像の設定アイコンから `Used on X pages` と赤い `Delete` が見える状態。削除は実行しない。 |
| D-05C | `d-05-clean-up-assets-menu.png` | `04-designer/05-asset-panel.md` | Clean up assetsメニュー | Expandメニュー内の `Clean up assets` が見える状態。実行ボタンを押す前に撮る。 |
| D-10 | `d-10-favicon-webclip-settings.png` | `04-designer/10-favicon.md` | Project Settings > GeneralのFavicon & Webclip | Favicon 32x32px、Webclip 256x256px、Uploadボタンが見える状態。 |
| D-11 | `d-11-page-duplicate-menu.png` | `04-designer/11-duplicate-page.md` | PagesパネルのDuplicateメニュー | 対象ページを右クリックし、`Duplicate` が表示されている状態。複製は実行しない。 |

## 今後追加しやすい写真パターン

マニュアルの実画面感を増やすなら、次のパターンもあると便利です。

| パターン | 使いどころ | 撮影ポイント |
|---|---|---|
| Publish前の確認画面 | Editor、CMS、Designer、Locale公開前 | Publishボタン、公開対象、公開先ドメイン、Cancelできる状態を写す。公開は実行しない。 |
| コメントで確認依頼する画面 | 公開前レビュー、修正確認依頼 | Webflow Commentsのコメント入力欄、対象箇所、コメントピンが分かる状態。個人名やメールは隠す。 |
| 権限不足の画面 | 編集できない、Publishできない、CMSが見えない時 | 権限不足メッセージ、Role確認画面、対象サイト名を写す。メールアドレスは隠す。 |
| スマホ表示確認 | 画像差し替え後、CMS公開前、表示崩れ相談 | DesktopとMobile previewの切り替え、スマホ幅での見え方を写す。 |
| 変更後の公開ページ確認 | 画像差し替え、テキスト修正、CMS公開後 | 公開URL、変更箇所、ページ全体の文脈を写す。社外秘情報は載せない。 |
| Site usage / Bandwidth確認 | 画像やPDFを多く追加した後 | `Usage > Site usage`、Bandwidth、対象期間が分かる状態。請求詳細は写さない。 |

## 撮影後の差し込み方針

撮影できた画像は `src/assets/captures/manual/` に保存し、本文内の `:::note[キャプチャー指示]` または `:::note[キャプチャー差し込み位置]` を画像に差し替えます。

差し替え後は、該当ページで次を確認してください。

- 画像が本文の流れに合っている。
- Alt textが画像内容を説明している。
- 同じ説明の画像が重複していない。
- Legacy Editorが通常導線のように見えない。
- `npm run build` が成功する。

## 2026-06-05 反映状況

`/Users/das/Downloads/マニュアルv3` で受領した以下の画像は、`src/assets/captures/manual/` に保存し、対応する本文へ反映済みです。

- `b-02-content-editor-first-check.png`
- `b-10-open-in-new-tab-setting.png`
- `b-11-anchor-link-url-field.png`
- `c-05-multi-reference-categories.png`
- `c-11-rich-text-image-size-menu.png`
- `c-22-body-image-alt-settings.png`
- `c-22-thumbnail-alt-settings.png`
- `d-05-asset-panel-replace-image.png`
- `d-05-asset-delete-used-on-pages.png`
- `d-10-favicon-webclip-settings.png`
- `d-11-page-duplicate-menu.png`
- `f-03-open-graph-image-setting.png`
- `f-06-form-submissions-export-all.png`
- `f-07-form-submissions-export-all.png`
- `f-08-form-field-settings.png`
- `f-10-page-indexing-settings.png`
- `f-11-page-indexing-settings.png`
- `g-00-settings-troubleshooting-check.png`
- `work-02-cms-items-full-list.png`

今回の反映後も、`d-05-clean-up-assets-menu.png` と `f-09-invite-member-role-modal.png` は未撮影のため本文内のキャプチャー指示を残しています。
