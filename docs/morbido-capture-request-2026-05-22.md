---
title: "Morbido Webflowマニュアル 追加キャプチャー撮影依頼 2026-05-22"
description: "Morbido向けWebflow更新マニュアルで追加撮影が必要な未撮影キャプチャーの依頼リスト。"
sidebar:
  order: 2
---

# Morbido Webflowマニュアル 追加キャプチャー撮影依頼 2026-05-22

## 目的

Morbido向けWebflow更新マニュアルに差し込む追加キャプチャーを撮影します。既に撮影済みの37枚は対象外です。この依頼では、未撮影の20枚だけを撮影してください。

## 保存先

撮影した画像は、以下のフォルダに保存してください。

`src/assets/captures/manual/`

ファイル名はこの依頼書の `保存ファイル名` と完全一致させてください。

## 共通ルール

- Webflow画面を開いたら、すぐ撮らずに3〜5秒待ってください。
- `Loading...`、スピナー、白紙、画像未読込、スケルトンUIが残っている状態は撮らないでください。
- 個人名、メールアドレス、問い合わせ本文、未公開記事、顧客情報、請求情報、カード情報は写さないでください。
- 他社サイト名や不要なサイトカードが写る場合は、撮影前に画面を調整するか、撮影後にマスクしてください。
- 保存、公開、削除、復元、招待、アーカイブなどは実行せず、実行前の確認画面またはボタンが見える状態で止めてください。
- ボタンだけを拡大しすぎず、押す場所と周辺の文脈が同時に分かる構図にしてください。
- 画像サイズは横1280px前後を目安にしてください。

## 最優先で撮るもの

まずは以下のP0を撮影してください。時間が限られる場合は、この表だけで問題ありません。

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- | --- | --- |
| A-06 | P0 | `a-06-morbido-workspace-overview.png` | MorbidoのWorkspace全体 | Webflow Dashboardで `morbido's Workspace` と対象サイトカードが見えている状態 | Workspace名、対象サイト名、サイトカード、Dashboardであることが分かる左メニューまたは上部UI | 個人メールアドレス、他社サイト名、請求情報、不要な通知 |
| A-07 | P0 | `a-07-workspace-plan-members.png` | Workspace plan / Members | WebflowのWorkspace planまたはMembers付近で、現在のプランとメンバー数が分かる状態 | Workspace plan、メンバー数、UpgradeやPlan関連の表示 | 請求先、カード情報、個人メールアドレス、料金明細の詳細 |
| A-08 | P0 | `a-08-site-plan-settings.png` | Site plan / Publishing設定 | Site settings内のPlansまたはPublishing周辺で、Site planやCMS Hosting / Business planが分かる状態 | 対象サイト名、Site settingsであること、Site plan名または公開設定 | 請求情報、カード情報、他サイトの情報 |
| A-09 | P0 | `a-09-members-and-permissions.png` | Membersと権限 | WorkspaceまたはSite settingsのMembers画面 | Invite/Add memberボタン、Role、Can publishなど権限判断に必要な列 | 氏名、メールアドレス、個人アイコン、他社メンバー情報 |
| A-10 | P0 | `a-10-open-site-from-dashboard.png` | Dashboardからサイト修正画面に入る入口 | Dashboardで対象サイトカードにカーソルを合わせ、Open in Webflowまたは編集入口が見えている状態 | 対象サイトカード、Open in Webflow、SettingsまたはDesignerへの入口 | 他サイト名、個人情報、通知、請求情報 |
| B-08 | P0 | `b-08-content-editor-latest-canvas.png` | Content Editor（最新版）でサイトを開いた直後 | 最新版のContent editor roleでサイトを開いた直後のcanvas画面 | 最新UIであることが分かる上部または周辺UI、編集可能なページ、対象サイト名 | 未公開ページ、個人情報、通知、他社サイト情報 |
| B-09 | P0 | `work-01-edit-text-open-site.png` | テキスト修正作業の開始画面 | 対象サイトカードからContent editor roleを開く直前のDashboard | 対象サイトカード、編集入口、Workspace名 | 他サイト名、メールアドレス、通知 |
| B-10 | P0 | `work-02-replace-image-edit-icon.png` | 画像差し替えアイコン | 画像にカーソルを合わせ、画像編集アイコンが出ている状態 | 差し替え対象画像、画像編集アイコン、周辺の見出し | 未公開画像、個人情報、不要な管理画面通知 |
| C-11 | P0 | `c-11-category-dropdown-open.png` | Categoryフィールドのドロップダウン | CMS記事編集画面で `Category` フィールドのドロップダウンを開いた状態 | `Category` フィールド、`Pick a Category...`、選択肢、記事編集画面であることが分かる周辺UI | 未公開記事名、個人情報、不要な本文、他社情報 |
| C-12 | P0 | `c-12-rich-text-list-icons.png` | Rich Textのリストアイコン | Rich Text本文欄でテキストを選択し、番号なしリストと番号付きリストのアイコンが見えている状態 | 選択中の本文、番号なしリストアイコン、番号付きリストアイコン、Rich Text欄 | 未公開本文、個人情報、不要な管理画面通知 |
| C-13 | P0 | `c-13-archive-button-visible.png` | CMS一覧のArchiveボタン | CMS記事一覧で記事にチェックを入れ、上部に `Archive` ボタンが表示された状態 | 選択済みチェックボックス、上部の `Archive` ボタン、記事一覧であることが分かるUI | 未公開記事名、個人情報、不要な本文、他社情報 |
| C-14 | P0 | `work-03-update-post-cms-list.png` | CMS記事一覧から投稿を始める画面 | CMS記事一覧で `New` ボタンと記事一覧が見えている状態 | CMS/Collection名、記事一覧、Newボタン | 未公開記事名、個人名、機密情報 |
| E-06 | P0 | `e-06-locale-publish-and-url.png` | Locale公開と公開URL確認 | Publishモーダル、または公開後のLocale URLが分かる画面を開いた状態 | 公開対象Locale、Publishモーダル、公開後の `/en` などのURL | 未公開ページ、個人情報、他社サイト情報 |
| E-07 | P0 | `work-06-edit-locale-selector.png` | Locale selectorで対象言語を確認する画面 | Locale selectorでPrimary / Secondary localeが見えている状態 | Locale selector、現在のLocale、対象ページの見出し | 未公開ページ、個人情報、他社サイト情報 |
| F-06 | P0 | `work-04-edit-seo-settings.png` | 作業ベースSEO設定画面 | SEO titleとmeta descriptionの入力欄が見えている設定画面 | Title tag、Meta description、対象ページ名 | 非公開ページ名、個人情報、APIキー、請求情報 |
| F-07 | P0 | `work-05-check-forms-submissions.png` | 作業ベースForms送信内容確認画面 | Forms一覧またはSubmissions画面 | フォーム名、Submissions、CSVダウンロード入口 | 氏名、メールアドレス、電話番号、問い合わせ本文 |
| G-04 | P0 | `g-04-maintenance-request-example.png` | 保守依頼時に送るキャプチャ例 | 問題箇所が分かる公開サイトまたはWebflow画面を開いた状態 | URL、困っている箇所、画面全体、発生日時を説明できる構図 | 個人情報、問い合わせ本文、不要な通知、他社情報 |

## 余力があれば撮るもの

以下はP1です。P0を撮り終えた後、時間があれば撮影してください。

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- | --- | --- |
| A-04 | P1 | `a-04-invitation-and-login.png` | 招待メールまたはログイン画面 | 招待メールならAccept Invitation、ログイン画面ならEmail、Password、Forgot passwordが分かる状態 | Accept Invitation、Email、Password、Forgot passwordなどログイン導線 | 実メールアドレス、個人名、受信箱の他メール |
| B-07 | P1 | `b-07-discard-changes-confirm.png` | 変更破棄の確認画面 | Content Editorで未公開変更を作り、Discard確認画面を出した状態 | Discard、Cancelなどの判断ボタン | 実際に破棄して困る変更、個人情報、通知 |
| D-05 | P1 | `d-05-undo-and-unsaved-warning.png` | Undoまたは未保存変更の確認 | DesignerでUndo / Redo、または保存せず終了する確認画面が見える状態 | Undo / Redo、未保存変更の警告、戻る選択肢 | 実行して困る変更、個人情報、他社情報 |

## 撮影後の確認

撮影後は、各画像について以下を確認してください。

- ファイル名が依頼書と一致している
- `src/assets/captures/manual/` に保存されている
- ロード中の表示が写っていない
- 個人情報、メールアドレス、請求情報、未公開情報が写っていない
- ボタンや入力欄だけでなく、どの画面なのか分かる周辺UIも入っている

## この依頼の元リスト

元の管理リストは `docs/human-capture-shot-list.md` です。本文内のキャプチャー指示は、主に以下のページに残っています。

- `src/content/docs/01-getting-started/00-workspace-intro.md`
- `src/content/docs/01-getting-started/00-workspace-plan.md`
- `src/content/docs/01-getting-started/00-site-plan.md`
- `src/content/docs/01-getting-started/00-add-member.md`
- `src/content/docs/01-getting-started/00-open-site.md`
- `src/content/docs/02-editor/02-open-content-editor.md`
- `src/content/docs/03-cms/05-post-category.md`
- `src/content/docs/03-cms/09-bullet-list.md`
- `src/content/docs/03-cms/20-archive-post.md`
- `src/content/docs/work/00-edit-text.md`
- `src/content/docs/work/01-replace-image.md`
- `src/content/docs/work/02-update-post.md`
- `src/content/docs/work/03-edit-seo.md`
- `src/content/docs/work/04-check-forms.md`
- `src/content/docs/work/05-edit-locale.md`
