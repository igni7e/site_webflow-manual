---
title: "画像使用状況確認 2026-05-18"
description: "Webflow更新マニュアルで使用中のキャプチャ、未使用画像、追加撮影候補の確認結果"
sidebar:
  order: 999
---

# 画像使用状況確認 2026-05-18

## 結論

- `src/assets/captures/manual/` にあるPNGは37枚です。
- 37枚すべてが `src/content/docs/` の本文内で使用されています。
- そのため、今回追加済み画像の中に未使用画像はありません。
- `docs/human-capture-shot-list.md` の欲しい画像一覧と照合すると、未取得・未反映の画像は6枚あります。

## 本文で使用中の画像

| 画像 | 使用回数 | 主な用途 |
| --- | ---: | --- |
| `a-01-dashboard-site-list.png` | 3 | Dashboard概要、トップページ |
| `a-02-site-card-actions.png` | 4 | サイトカード操作、Content Editor入口 |
| `a-03-site-settings-left-menu.png` | 1 | Site settings概要 |
| `a-05-chrome-translate-extension.png` | 1 | Chrome翻訳・日本語化 |
| `b-01-open-content-editor.png` | 1 | B-1 Content Editor旧バージョン |
| `b-02-editor-canvas-opened.png` | 1 | B-1 Content Editor旧バージョンで開いた状態 |
| `b-03-editable-text-active.png` | 2 | テキスト編集、太字 |
| `b-04-link-settings-panel.png` | 3 | リンク追加、URL変更、外部リンク |
| `b-05-image-replace.png` | 1 | 画像差し替え |
| `b-06-publish-button-editor.png` | 2 | Publish、公開前チェック |
| `c-01-cms-collections-entry.png` | 2 | CMS入口、CMS完全ガイド |
| `c-02-collection-items-list.png` | 1 | 記事一覧 |
| `c-03-new-cms-item-form.png` | 2 | 新規CMS item、タイトル |
| `c-04-thumbnail-and-category.png` | 2 | サムネイル、カテゴリー |
| `c-05-rich-text-body.png` | 4 | Rich Text本文、文字装飾、見出し、リスト |
| `c-06-rich-text-media.png` | 2 | 画像挿入、YouTube埋め込み |
| `c-07-save-draft-and-publish.png` | 3 | 下書き保存、公開、CMS公開前チェック |
| `c-08-schedule-and-date.png` | 2 | 公開日・予約公開 |
| `c-09-unpublish-archive-delete.png` | 3 | 非公開・アーカイブ・削除 |
| `c-10-asset-file-upload.png` | 1 | PDFなどのファイル添付 |
| `d-01-designer-opened.png` | 2 | Designer概要、Designer注意 |
| `d-02-edit-page-text.png` | 2 | Designerでのテキスト編集 |
| `d-03-assets-and-logo.png` | 3 | ロゴ差し替え、Asset Panel、Asset削除 |
| `d-04-designer-publish-modal.png` | 1 | Designer Publish |
| `e-01-locale-selector.png` | 2 | Locale概要、翻訳フロー |
| `e-02-localization-settings.png` | 1 | Locale追加 |
| `e-03-static-page-translation.png` | 1 | 固定ページ翻訳 |
| `e-04-cms-locale-translation.png` | 1 | CMS Locale翻訳 |
| `e-05-localized-seo-ogp.png` | 1 | LocaleごとのSEO / OGP |
| `f-01-seo-and-ogp-settings.png` | 2 | SEO title、SEO description |
| `f-02-forms-list-and-submissions.png` | 2 | Form submissions、CSV |
| `f-03-email-notification-settings.png` | 2 | 通知メール、メール未着 |
| `f-04-members-and-roles.png` | 1 | Collaborator招待 |
| `f-05-domain-and-publishing-status.png` | 2 | Domain / Publishing状態、反映されない時の確認 |
| `g-01-backups-list.png` | 1 | Backups一覧 |
| `g-02-backup-restore-warning.png` | 1 | Restore確認 |
| `g-03-error-examples.png` | 1 | 画像アップロードエラー例 |

## 未使用画像

なし。

`src/assets/captures/manual/` に存在する37枚は、すべて本文で参照されています。

## 欲しい画像一覧に残っている未取得画像

| 優先 | 画像 | 使いたいページ | 追加した方がよい理由 |
| --- | --- | --- | --- |
| P1 | `a-04-invitation-and-login.png` | `01-invitation-email.md`, `02-create-account.md`, `03-first-login.md`, `05-reset-password.md` | 招待、初回登録、ログイン、パスワード再設定は初心者がつまずきやすいため。 |
| P1 | `b-07-discard-changes-confirm.png` | `02-editor/09-discard-changes.md` | 変更破棄は不安が出やすい操作なので、確認画面があると安心材料になる。 |
| P0 | `b-08-content-editor-latest-canvas.png` | `02-editor/02-open-content-editor.md`, `02-editor/00-editor-complete-guide.md` | 現在の `b-02` は旧Editor寄りの画面なので、最新版Content Editorのcanvas画像を別途撮る必要がある。 |
| P1 | `d-05-undo-and-unsaved-warning.png` | `04-designer/08-undo-ctrl-z.md`, `09-discard-designer-changes.md` | DesignerでのUndoや未保存警告は、誤操作防止の説明に有効。 |
| P0 | `e-06-locale-publish-and-url.png` | `07-localization/05-locale-publish-checklist.md`, `07-publish-and-reflect-locale.md` | Locale公開とURL確認は影響範囲が大きく、手順理解に画像が必要。 |
| P0 | `g-04-maintenance-request-example.png` | `06-troubleshooting/07-maintenance-request.md`, `00-common-checklist.md` | 問い合わせ時に何を写せばよいかを具体化できる。 |

## 追加撮影の優先順

1. `e-06-locale-publish-and-url.png`
2. `g-04-maintenance-request-example.png`
3. `b-08-content-editor-latest-canvas.png`
4. `b-07-discard-changes-confirm.png`
5. `a-04-invitation-and-login.png`
6. `d-05-undo-and-unsaved-warning.png`

## 余裕があれば追加したい補足画像

現在の画像は統合キャプチャーを複数ページで使い回しているため、最低限は成立しています。ただし、より分かりやすくするなら以下を個別画像として追加するとよいです。

| 追加候補 | 対象ページ | 理由 |
| --- | --- | --- |
| 見出しメニュー専用のRich Text画像 | `03-cms/08-headings.md` | 現在はRich Text本文欄の画像で代用しているため、見出し選択の場所が弱い。 |
| リスト作成メニュー専用のRich Text画像 | `03-cms/09-bullet-list.md` | 現在は本文欄中心で、箇条書き操作の位置が伝わりにくい。 |
| Rich Text内リンク設定専用画像 | `03-cms/13-body-link.md` | Editor側リンク画像とは別に、CMS本文内リンクの画面があると混乱が減る。 |
| 画像サイズ変更メニュー専用画像 | `03-cms/11-resize-image.md` | 現在はメディア挿入画像で代用しており、リサイズ操作の説明には弱い。 |
| OGP画像設定専用画像 | `05-settings/03-ogp-image.md` | 現在はSEO / OGP全体画像で代用しているため、OGP image欄を強調した画像があるとよい。 |
| 404エラー専用画像 | `06-troubleshooting/04-404-not-found.md` | 現在の `g-03` はエラー例の統合画像なので、404だけを示す画像があると説明が明確になる。 |

## 注意

`docs/capture-checklist.md` は旧SVGベースのチェックリストが残っており、現在の `src/assets/captures/manual/` PNG運用とはずれがあります。今後の撮影管理は `docs/human-capture-shot-list.md` を正とするのが安全です。
