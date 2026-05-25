---
title: "Booost Webflowマニュアル 追加キャプチャー撮影依頼 2026-05-22"
description: "Booost向けWebflow更新マニュアルで追加撮影が必要な未撮影キャプチャーの依頼リスト。"
sidebar:
  order: 2
---

# Booost Webflowマニュアル 追加キャプチャー撮影依頼 2026-05-22

## 目的

Booost向けWebflow更新マニュアルに差し込む追加キャプチャーと公式画像を整理します。既に撮影済みの37枚は対象外です。この依頼では、未撮影の22枚に加えて、Webflow公式画像候補28枚を確認してください。

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
- Webflow公式画像を使う場合は、公式Help Centerまたは公式サイトの最新版Content Editor画像を優先してください。
- 公式画像を保存する場合も、ファイル名はこの依頼書の `保存ファイル名` と完全一致させてください。

## 最優先で撮るもの

まずは以下のP0を撮影してください。時間が限られる場合は、この表だけで問題ありません。

| ID | 優先 | 保存ファイル名 | 撮影する画面 | 撮影直前の状態 | 必ず写すもの | 写さないもの |
| --- | --- | --- | --- | --- | --- | --- |
| A-06 | P0 | `a-06-booost-workspace-overview.png` | BooostのWorkspace全体 | Webflow Dashboardで `Booost Workspace` と対象サイトカードが見えている状態 | Workspace名、対象サイト名、サイトカード、Dashboardであることが分かる左メニューまたは上部UI | 個人メールアドレス、他社サイト名、請求情報、不要な通知 |
| A-07 | P0 | `a-07-workspace-plan-members.png` | Workspace plan / Members | WebflowのWorkspace planまたはMembers付近で、現在のプランとメンバー数が分かる状態 | Workspace plan、メンバー数、UpgradeやPlan関連の表示 | 請求先、カード情報、個人メールアドレス、料金明細の詳細 |
| A-08 | P0 | `a-08-site-plan-settings.png` | Site plan / Publishing設定 | Site settings内のPlansまたはPublishing周辺で、Site planやCMS Hosting / Business planが分かる状態 | 対象サイト名、Site settingsであること、Site plan名または公開設定 | 請求情報、カード情報、他サイトの情報 |
| A-09 | P0 | `a-09-members-and-permissions.png` | Membersと権限 | WorkspaceまたはSite settingsのMembers画面 | Invite/Add memberボタン、Role、Can publishなど権限判断に必要な列 | 氏名、メールアドレス、個人アイコン、他社メンバー情報 |
| A-10 | P0 | `a-10-open-site-from-dashboard.png` | Dashboardからサイト修正画面に入る入口 | Dashboardで対象サイトカードにカーソルを合わせ、Open in Webflowまたは編集入口が見えている状態 | 対象サイトカード、Open in Webflow、SettingsまたはDesignerへの入口 | 他サイト名、個人情報、通知、請求情報 |
| B-08 | P0 | `b-08-content-editor-latest-canvas.png` | Content Editor（最新版）でサイトを開いた直後 | 最新版のContent editor roleでサイトを開いた直後のcanvas画面 | 最新UIであることが分かる上部または周辺UI、編集可能なページ、対象サイト名 | 未公開ページ、個人情報、通知、他社サイト情報 |
| B-11 | P0 | `b-09-latest-content-editor-screen-guide.png` | 最新Content Editorの画面構成 | Webflow公式Help CenterのContent editor role説明画像、またはBooostサイトを最新版Content editor roleで開いたcanvas画面 | canvas、上部バー、Pages/CMS/Assetsなどの入口、編集可能な要素の青いアウトラインまたは編集アイコン | 未公開ページ、個人情報、通知、他社サイト情報 |
| B-12 | P0 | `b-12-official-content-editor-canvas.png` | 公式画像: Content editor roleのcanvas全体 | Webflow公式Help Centerまたは公式サイトのContent Editor説明画像を確認した状態 | canvas、編集対象ページ、Content editor roleであることが分かるUI | Legacy Editorの古い下部バーだけの画像、個人情報、未公開ページ |
| B-13 | P0 | `b-13-official-content-editor-panels.png` | 公式画像: Pages / CMS / Assets / Settingsの入口 | Webflow公式Help CenterのContent editor role説明画像を確認した状態 | Pages、CMS、Assets、Settingsなどの入口と画面全体の位置関係 | 入口だけの極端な拡大、ロード中のUI、通知 |
| B-14 | P0 | `b-14-official-text-editing.png` | 公式画像: 文字編集のアウトラインまたはPencilアイコン | 公式画像またはBooost画面でテキストにカーソルを合わせた状態 | 編集対象テキスト、青いアウトライン、Pencilなどの編集アイコン | デザイン編集パネル中心の画面、未公開本文、個人情報 |
| B-15 | P0 | `b-15-official-image-replace.png` | 公式画像: 画像差し替えの入口 | 公式画像またはBooost画面で画像編集入口が見えている状態 | 対象画像、画像編集アイコン、AssetsまたはUploadに進める入口 | 著作権不明の画像、個人情報、未公開素材 |
| B-16 | P0 | `b-16-official-link-editing.png` | 公式画像: リンク編集の入口 | 公式画像またはBooost画面でリンク設定入口が見えている状態 | Link設定、URL入力欄、新しいタブ設定 | 実在する非公開URL、ログイン情報、外部サービス管理画面 |
| B-17 | P0 | `b-17-official-publish-flow.png` | 公式画像: Publish前の確認画面 | 公式画像またはBooost画面でPublish前確認が見えている状態 | Publishボタン、公開対象、公開前確認の文脈 | 実際にPublish完了してしまった後だけの画面、公開してはいけないドメイン |
| B-09 | P0 | `work-01-edit-text-open-site.png` | テキスト修正作業の開始画面 | 対象サイトカードからContent editor roleを開く直前のDashboard | 対象サイトカード、編集入口、Workspace名 | 他サイト名、メールアドレス、通知 |
| B-10 | P0 | `work-02-replace-image-edit-icon.png` | 画像差し替えアイコン | 画像にカーソルを合わせ、画像編集アイコンが出ている状態 | 差し替え対象画像、画像編集アイコン、周辺の見出し | 未公開画像、個人情報、不要な管理画面通知 |
| C-11 | P0 | `c-11-category-dropdown-open.png` | Categoryフィールドのドロップダウン | CMS記事編集画面で `Category` フィールドのドロップダウンを開いた状態 | `Category` フィールド、`Pick a Category...`、選択肢、記事編集画面であることが分かる周辺UI | 未公開記事名、個人情報、不要な本文、他社情報 |
| C-12 | P0 | `c-12-rich-text-list-icons.png` | Rich Textのリストアイコン | Rich Text本文欄でテキストを選択し、番号なしリストと番号付きリストのアイコンが見えている状態 | 選択中の本文、番号なしリストアイコン、番号付きリストアイコン、Rich Text欄 | 未公開本文、個人情報、不要な管理画面通知 |
| C-13 | P0 | `c-13-archive-button-visible.png` | CMS一覧のArchiveボタン | CMS記事一覧で記事にチェックを入れ、上部に `Archive` ボタンが表示された状態 | 選択済みチェックボックス、上部の `Archive` ボタン、記事一覧であることが分かるUI | 未公開記事名、個人情報、不要な本文、他社情報 |
| C-14 | P0 | `work-03-update-post-cms-list.png` | CMS記事一覧から投稿を始める画面 | CMS記事一覧で `New` ボタンと記事一覧が見えている状態 | CMS/Collection名、記事一覧、Newボタン | 未公開記事名、個人名、機密情報 |
| C-15 | P0 | `c-15-booost-cms-fields-overview.png` | Booost記事入力フィールド全体 | BooostのCMS記事編集画面で、個人情報や未公開本文が見えないようにした状態 | Title、Slug、Summary、Thumbnail、Bodyなど主要Field、Save/Create/Publish周辺の操作ボタン | 未公開記事本文、個人情報、社外秘の画像、他社情報 |
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
| B-18 | P1 | `b-18-official-update-shortcut.png` | 公式画像: `?update` で直接編集画面を開く導線 | 公式Help CenterのShortcut説明、または公開サイトURL末尾に `?update` を付けた状態 | URL末尾の `?update`、編集画面への導線 | 非公開URL、個人情報、他社サイト情報 |
| B-19 | P1 | `b-19-official-legacy-vs-content-editor.png` | 公式画像: Legacy Editorと最新版Content Editorの違い | 公式Help Centerの比較説明を確認した状態 | Legacy Editorと最新版Content Editorの違いが説明できる画像 | 旧画面だけで最新版UIと誤解される画像 |
| B-20 | P1 | `b-20-official-cms-item-editing.png` | 公式画像: CMS itemを作成・編集する画面 | 公式画像またはBooost CMSで、CMS fieldsが見えている状態 | CMS fields、preview、publishの流れ | 未公開記事本文、個人情報、社外秘画像 |
| B-21 | P1 | `b-21-official-seo-ogp-controls.png` | 公式画像: SEO / Open Graphを確認する画面 | 公式画像またはBooost設定画面でSEO / OGPが見えている状態 | Page title、Meta description、Open Graph設定 | APIキー、非公開ページ名、請求情報 |
| B-22 | P1 | `b-22-official-content-role-permissions.png` | 公式画像: Content editor roleの権限・Publish権限 | 公式Help Centerのrole説明、または権限画面を開いた状態 | Content editor role、Can publish、権限範囲 | 氏名、メールアドレス、請求情報 |
| B-23 | P1 | `b-23-official-cms-overview.png` | 公式画像: CMS機能の概要 | Webflow公式CMSページの画像を確認した状態 | CMSで構造化コンテンツを管理する全体像 | Webflow製品外のCMS画像、古いUIだけの画像 |
| B-24 | P1 | `b-24-official-cms-draft-publishing.png` | 公式画像: CMS下書き・公開ワークフロー | Webflow公式UpdatesのCMS Drafting and Publishing画像を確認した状態 | Draft changes、個別公開、公開前確認の文脈 | 公開してはいけないドメイン、未公開記事本文 |
| B-25 | P1 | `b-25-official-cms-auto-save.png` | 公式画像: CMS自動保存 | Webflow公式UpdatesのCMS auto-save画像を確認した状態 | CMS編集の保存・公開操作を説明できる画面 | 未公開本文、個人情報 |
| B-26 | P1 | `b-26-official-cms-bulk-publishing.png` | 公式画像: CMS一括公開・一括非公開 | Webflow公式UpdatesのBulk publishing画像を確認した状態 | 複数CMS itemをまとめて扱う操作の文脈 | 誤って本番itemを公開する操作 |
| B-27 | P1 | `b-27-official-cms-item-creation.png` | 公式画像: CMS item作成改善 | Webflow公式UpdatesのCMS item creation画像を確認した状態 | CMS item作成や編集の流れ | 未公開記事本文、個人情報 |
| B-28 | P1 | `b-28-official-seo-overview.png` | 公式画像: SEO機能の概要 | Webflow公式SEOページの画像を確認した状態 | SEO title、meta description、Open Graphの文脈 | 外部SEOツール管理画面、実在する未公開検索結果 |
| B-29 | P1 | `b-29-official-localization-overview.png` | 公式画像: Localization機能の概要 | Webflow公式Localizationページの画像を確認した状態 | Locale、翻訳、地域別コンテンツの文脈 | Booost以外の顧客名が主役になる画像 |
| B-30 | P1 | `b-30-official-collaboration-overview.png` | 公式画像: チーム編集・コメント・権限 | Webflow公式Collaborationページの画像を確認した状態 | コメント、権限、チームで安全に作業する文脈 | 氏名、メールアドレス、請求情報 |
| B-31 | P1 | `b-31-official-single-page-publishing.png` | 公式画像: 1ページだけPublishする考え方 | Webflow公式Single page publishing画像、またはPublish確認画面を開いた状態 | Publish対象ページ、公開先、実行前で止めていること | 他社ドメイン、未公開ページ名、個人情報、通知 |
| B-32 | P1 | `b-32-official-single-page-publishing-access.png` | 公式画像: 1ページ公開権限 | Webflow公式Single page publishing access画像、またはRole/permissions画面を開いた状態 | Role、Can publish、公開権限のON/OFF | 氏名、メールアドレス、請求情報、他社メンバー |
| B-33 | P1 | `b-33-official-next-gen-cms.png` | 公式画像: Next-gen CMSの概要 | Webflow公式Next-gen CMS画像、または新規CMS itemフォームを開いた状態 | New item、Title/Name、Slug、主要Field、Save/Create/Publish周辺 | 未公開本文、個人情報、社外秘画像、他社情報 |
| B-34 | P1 | `b-34-official-publishing-permission-toggle.png` | 公式画像: Publish権限のON/OFF | Webflow公式Publishing permission toggle画像、またはPublish権限設定画面 | Publish権限のON/OFF、Role、対象サイトまたはWorkspace | 氏名、メールアドレス、請求情報 |
| B-35 | P1 | `b-35-official-preview-roles.png` | 公式画像: Preview role | Webflow公式Preview roles画像、またはPreview/review用権限が分かる画面 | Preview role、レビュー担当者が確認する文脈 | 氏名、メールアドレス、未公開情報 |
| B-36 | P1 | `b-36-official-hosting-domain.png` | 公式画像: Hosting / Domain / SSLの概要 | Webflow公式Hosting画像、またはSite settingsのPublishing / Domain設定 | Production domain、Connected、SSL Active、Publishing画面 | DNS設定値の詳細、請求情報、カード情報、他社ドメイン |
| B-37 | P1 | `b-37-official-security-permissions.png` | 公式画像: Securityと権限管理 | Webflow公式Security画像、または権限不足・エラー表示のWebflow画面 | エラーメッセージ、対象画面、どの操作で止まったか分かる周辺UI | メールアドレス、問い合わせ本文、請求情報、APIキー、他社情報 |
| B-38 | P1 | `b-38-official-analyze-seo-settings.png` | 公式画像: Analyze / 計測の概要 | Webflow公式Analyze画像、またはSite settingsのSEO / sitemap / indexing設定 | SEO、sitemap、indexing、Publishが必要な設定であること | APIキー、Googleアカウント情報、外部計測タグの詳細、個人情報 |
| B-39 | P1 | `b-39-official-designer-overview.png` | 公式画像: Designerの概要 | Webflow公式Design画像、またはDesignerを開いた直後の画面 | 左パネル、canvas、右パネル、上部バー、Designerであること | 未公開ページ、個人情報、他社サイト情報、通知 |
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
- `src/content/docs/02-editor/14-official-content-editor-image-reference.md`
- `src/content/docs/03-cms/05-post-category.md`
- `src/content/docs/03-cms/09-bullet-list.md`
- `src/content/docs/03-cms/20-archive-post.md`
- `src/content/docs/work/00-edit-text.md`
- `src/content/docs/work/01-replace-image.md`
- `src/content/docs/work/02-update-post.md`
- `src/content/docs/work/03-edit-seo.md`
- `src/content/docs/work/04-check-forms.md`
- `src/content/docs/work/05-edit-locale.md`
