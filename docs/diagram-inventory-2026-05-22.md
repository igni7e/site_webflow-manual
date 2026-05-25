---
title: "Python生成図解一覧 2026-05-22"
description: "Webflowマニュアルに追加したPython生成図解50枚のファイル名、差し込み先、用途の一覧。"
---

# Python生成図解一覧 2026-05-22

Pythonで生成したSVG図解を `src/assets/diagrams/manual/` に保存し、各本文ページへ差し込みました。

## AI生成画像への差し替えメモ

以下の図解は、Python生成SVGよりも初心者向けの視覚説明を優先し、AI生成のPNGへ差し替えました。元のSVGは削除せず、段階的な差し替え対象として残しています。

| 旧図解 | 新ファイル | 差し込み先 | 理由 |
| --- | --- | --- | --- |
| `diagram-12-diagram.svg` | `src/assets/ai-diagrams/manual/editor-icon-conditions.png` | `02-editor/13-latest-content-editor-screen-guide.md` | 編集できる要素と編集できない要素の違いを画面イメージで見せるため。 |
| `diagram-13-diagram.svg` | `src/assets/ai-diagrams/manual/text-edit-safe-steps.png` | `02-editor/03-edit-text.md` | テキスト修正の流れを、Publish前確認まで含めて見せるため。 |
| `diagram-14-diagram.svg` | `src/assets/ai-diagrams/manual/image-replace-safe-steps.png` | `02-editor/06-replace-image.md` | 画像差し替え後のデスクトップ・スマホ確認を強調するため。 |
| `diagram-01-workspace-site.svg` | `src/assets/ai-diagrams/manual/workspace-site-relationship.png` | `01-getting-started/00-workspace-intro.md` | WorkspaceとSite cardの関係を実務画面に近い構図で見せるため。 |
| `diagram-02-workspace-plan-site-plan.svg` | `src/assets/ai-diagrams/manual/workspace-plan-site-plan.png` | `01-getting-started/00-plan-role-decision.md`, `00-workspace-plan.md`, `00-site-plan.md` | Workspace planとSite planの違いをまとめて見せるため。 |
| `diagram-04-dashboard.svg` | `src/assets/ai-diagrams/manual/content-editor-open-flow.png` | `01-getting-started/00-open-site.md` | DashboardからContent Editorへ入る流れを具体的に見せるため。 |
| `diagram-07-diagram.svg` | `src/assets/ai-diagrams/manual/safe-update-route.png` | `01-getting-started/08-editor-only-recommendation.md` | 通常更新の安全ルートと相談が必要な操作を分けて見せるため。 |
| `diagram-08-editor-designer.svg` | `src/assets/ai-diagrams/manual/editor-designer-boundary.png` | `01-getting-started/07-editor-vs-designer.md` | EditorとDesignerの責任範囲を視覚的に分けるため。 |
| `diagram-11-content-editor.svg` | `src/assets/ai-diagrams/manual/content-editor-open-flow.png` | `02-editor/02-open-content-editor.md` | Content Editorを開いて編集対象を確認する流れを見せるため。 |
| `diagram-16-publish.svg`, `diagram-17-publish.svg` | `src/assets/ai-diagrams/manual/publish-flow.png` | `02-editor/12-before-publish-checklist.md`, `02-editor/08-save-and-publish.md` | Publish前確認、公開先選択、公開後確認を一連の流れで見せるため。 |
| `diagram-19-cms.svg` | `src/assets/ai-diagrams/manual/cms-overview.png` | `03-cms/00-blog-post-complete-guide.md` | Collection、CMS item、一覧・詳細ページの関係を見せるため。 |
| `diagram-20-cms-item.svg` | `src/assets/ai-diagrams/manual/cms-item-creation-flow.png` | `03-cms/02-create-new-post.md` | CMS item作成から下書き保存・公開までの流れを見せるため。 |
| `diagram-21-title-slug.svg` | `src/assets/ai-diagrams/manual/title-slug-relationship.png` | `03-cms/03-post-title.md` | TitleとSlug、公開URLの関係を具体的に見せるため。 |
| `diagram-25-diagram.svg`, `diagram-26-diagram.svg`, `diagram-28-cms.svg` | `src/assets/ai-diagrams/manual/cms-publish-status-options.png` | `03-cms/16-save-as-draft.md`, `03-cms/18-edit-published.md`, `03-cms/25-cms-before-publish-checklist.md` | Draft、Publish now、Queueの違いを明確に見せるため。 |
| `diagram-40-domain-ssl.svg` | `src/assets/ai-diagrams/manual/domain-ssl-status.png` | `05-settings/09-domain-status.md` | Domain、SSL、公開先を設定画面風に見せるため。 |
| `diagram-47-diagram.svg` | `src/assets/ai-diagrams/manual/publish-cache-troubleshooting.png` | `06-troubleshooting/01-cache-not-reflecting.md` | Publish、公開先、cache、CMS statusの切り分けを見せるため。 |
| `diagram-03-diagram.svg` | `src/assets/ai-diagrams/manual/member-permissions.png` | `01-getting-started/00-add-member.md` | 追加する人、招待元、Role、Can publishの確認点をまとめて見せるため。 |
| `diagram-15-diagram.svg` | `src/assets/ai-diagrams/manual/link-change-safe-check.png` | `02-editor/07-edit-link-url.md` | リンク変更前後に確認するURL、リンク先、別タブ設定を見せるため。 |
| `diagram-18-diagram.svg` | `src/assets/ai-diagrams/manual/discard-changes-warning.png` | `02-editor/09-discard-changes.md` | Discard時に戻る範囲とPublish済みとの差を視覚的に見せるため。 |
| `diagram-22-diagram.svg` | `src/assets/ai-diagrams/manual/cms-thumbnail-body-image.png` | `03-cms/04-thumbnail-image.md` | サムネイル画像と本文内画像の表示先の違いを見せるため。 |
| `diagram-23-diagram.svg` | `src/assets/ai-diagrams/manual/cms-category-selection.png` | `03-cms/05-post-category.md` | Categoryの選択が一覧、絞り込み、関連記事に影響することを見せるため。 |
| `diagram-24-rich-text.svg` | `src/assets/ai-diagrams/manual/cms-rich-text-structure.png` | `03-cms/06-write-body.md` | Rich Text内の見出し、本文、画像、リンクの並びを見せるため。 |
| `diagram-30-diagram.svg` | `src/assets/ai-diagrams/manual/cms-body-link-options.png` | `03-cms/13-body-link.md` | 内部リンク、外部リンク、別タブ設定の違いを見せるため。 |
| `diagram-27-diagram.svg` | `src/assets/ai-diagrams/manual/cms-unpublish-archive-delete.png` | `03-cms/19-unpublish.md` | Unpublish、Archive、Deleteの影響範囲を分けて見せるため。 |
| `diagram-31-designer.svg`, `diagram-32-designer.svg` | `src/assets/ai-diagrams/manual/designer-caution.png` | `04-designer/01-designer-warning.md`, `04-designer/02-edit-homepage-text.md` | Designerで触ってよい箇所と相談すべき箇所を見せるため。 |
| `diagram-33-asset-panel.svg` | `src/assets/ai-diagrams/manual/asset-panel-workflow.png` | `04-designer/05-asset-panel.md` | Asset Panelでアップロード、選択、差し替えを行う流れを見せるため。 |
| `diagram-34-undo.svg` | `src/assets/ai-diagrams/manual/undo-backup-restore.png` | `04-designer/08-undo-ctrl-z.md` | Undo、History、Backup restoreの戻せる範囲を分けて見せるため。 |
| `diagram-35-seo-title.svg`, `diagram-36-meta-description.svg`, `diagram-37-ogp.svg` | `src/assets/ai-diagrams/manual/seo-meta-ogp-settings.png` | `05-settings/01-seo-title.md`, `05-settings/02-seo-description.md`, `05-settings/03-ogp-image.md` | SEO title、Meta description、OGP画像の表示先をまとめて見せるため。 |
| `diagram-38-forms.svg`, `diagram-39-csv.svg` | `src/assets/ai-diagrams/manual/forms-csv-privacy.png` | `05-settings/04-form-submissions.md`, `05-settings/06-form-csv-download.md` | Form submissionsとCSV exportで個人情報を扱う注意点を見せるため。 |
| `diagram-42-locale.svg`, `diagram-43-primary-secondary-locale.svg`, `diagram-44-diagram.svg`, `diagram-45-cms-locale.svg`, `diagram-46-locale-seo-ogp.svg` | `src/assets/ai-diagrams/manual/localization-workflow.png` | `07-localization/*` | Primary Locale、Secondary Locale、静的ページ、CMS、SEO/OGPの翻訳範囲をまとめて見せるため。 |

| ID | ファイル | 差し込み先 | 用途 |
| --- | --- | --- | --- |
| diagram-01 | `diagram-01-workspace-site.svg` | `01-getting-started/00-workspace-intro.md` | Workspaceの基本構造 |
| diagram-02 | `diagram-02-workspace-plan-site-plan.svg` | `01-getting-started/00-plan-role-decision.md` | Plan判断 |
| diagram-03 | `diagram-03-diagram.svg` | `01-getting-started/00-add-member.md` | メンバー追加 |
| diagram-04 | `diagram-04-dashboard.svg` | `01-getting-started/00-open-site.md` | Dashboard入口 |
| diagram-05 | `diagram-05-workspace-plan.svg` | `01-getting-started/00-workspace-plan.md` | Workspace plan |
| diagram-06 | `diagram-06-site-plan.svg` | `01-getting-started/00-site-plan.md` | Site plan |
| diagram-07 | `diagram-07-diagram.svg` | `01-getting-started/08-editor-only-recommendation.md` | 安全な入口 |
| diagram-08 | `diagram-08-editor-designer.svg` | `01-getting-started/07-editor-vs-designer.md` | Editor vs Designer |
| diagram-09 | `diagram-09-diagram.svg` | `01-getting-started/11-after-login-first-steps.md` | 初回確認 |
| diagram-10 | `diagram-10-webflow.svg` | `01-getting-started/10-webflow-ui-glossary.md` | 用語整理 |
| diagram-11 | `diagram-11-content-editor.svg` | `02-editor/02-open-content-editor.md` | 開き方 |
| diagram-12 | `diagram-12-diagram.svg` | `02-editor/13-latest-content-editor-screen-guide.md` | 画面の見方 |
| diagram-13 | `diagram-13-diagram.svg` | `02-editor/03-edit-text.md` | テキスト編集 |
| diagram-14 | `diagram-14-diagram.svg` | `02-editor/06-replace-image.md` | 画像差し替え |
| diagram-15 | `diagram-15-diagram.svg` | `02-editor/07-edit-link-url.md` | リンク変更 |
| diagram-16 | `diagram-16-publish.svg` | `02-editor/12-before-publish-checklist.md` | 公開前確認 |
| diagram-17 | `diagram-17-publish.svg` | `02-editor/08-save-and-publish.md` | Publish |
| diagram-18 | `diagram-18-diagram.svg` | `02-editor/09-discard-changes.md` | 変更破棄 |
| diagram-19 | `diagram-19-cms.svg` | `03-cms/00-blog-post-complete-guide.md` | CMS概要 |
| diagram-20 | `diagram-20-cms-item.svg` | `03-cms/02-create-new-post.md` | 新規記事 |
| diagram-21 | `diagram-21-title-slug.svg` | `03-cms/03-post-title.md` | Title/Slug |
| diagram-22 | `diagram-22-diagram.svg` | `03-cms/04-thumbnail-image.md` | 画像Field |
| diagram-23 | `diagram-23-diagram.svg` | `03-cms/05-post-category.md` | カテゴリー |
| diagram-24 | `diagram-24-rich-text.svg` | `03-cms/06-write-body.md` | 本文 |
| diagram-25 | `diagram-25-diagram.svg` | `03-cms/16-save-as-draft.md` | 公開状態 |
| diagram-26 | `diagram-26-diagram.svg` | `03-cms/18-edit-published.md` | 公開済み修正 |
| diagram-27 | `diagram-27-diagram.svg` | `03-cms/19-unpublish.md` | 非公開 |
| diagram-28 | `diagram-28-cms.svg` | `03-cms/25-cms-before-publish-checklist.md` | 公開前 |
| diagram-29 | `diagram-29-morbido-field.svg` | `03-cms/26-morbido-cms-field-guide.md` | Morbido Fields |
| diagram-30 | `diagram-30-diagram.svg` | `03-cms/13-body-link.md` | 本文リンク |
| diagram-31 | `diagram-31-designer.svg` | `04-designer/01-designer-warning.md` | Designer注意 |
| diagram-32 | `diagram-32-designer.svg` | `04-designer/02-edit-homepage-text.md` | Designer画面 |
| diagram-33 | `diagram-33-asset-panel.svg` | `04-designer/05-asset-panel.md` | Assets |
| diagram-34 | `diagram-34-undo.svg` | `04-designer/08-undo-ctrl-z.md` | Undo |
| diagram-35 | `diagram-35-seo-title.svg` | `05-settings/01-seo-title.md` | SEO title |
| diagram-36 | `diagram-36-meta-description.svg` | `05-settings/02-seo-description.md` | Meta description |
| diagram-37 | `diagram-37-ogp.svg` | `05-settings/03-ogp-image.md` | OGP |
| diagram-38 | `diagram-38-forms.svg` | `05-settings/04-form-submissions.md` | Forms |
| diagram-39 | `diagram-39-csv.svg` | `05-settings/06-form-csv-download.md` | CSV |
| diagram-40 | `diagram-40-domain-ssl.svg` | `05-settings/09-domain-status.md` | Domain/SSL |
| diagram-41 | `diagram-41-sitemap-noindex.svg` | `05-settings/10-search-engine-control.md` | SEO制御 |
| diagram-42 | `diagram-42-locale.svg` | `07-localization/00-localization-overview.md` | Locale概要 |
| diagram-43 | `diagram-43-primary-secondary-locale.svg` | `07-localization/06-add-new-locale.md` | Locale追加 |
| diagram-44 | `diagram-44-diagram.svg` | `07-localization/02-static-page-translation.md` | 静的ページ |
| diagram-45 | `diagram-45-cms-locale.svg` | `07-localization/03-cms-locale-translation.md` | CMS翻訳 |
| diagram-46 | `diagram-46-locale-seo-ogp.svg` | `07-localization/04-localized-seo-ogp.md` | Locale SEO |
| diagram-47 | `diagram-47-diagram.svg` | `06-troubleshooting/01-cache-not-reflecting.md` | 反映されない |
| diagram-48 | `diagram-48-diagram.svg` | `06-troubleshooting/02-image-upload-failed.md` | 画像トラブル |
| diagram-49 | `diagram-49-404.svg` | `06-troubleshooting/04-404-not-found.md` | 404 |
| diagram-50 | `diagram-50-diagram.svg` | `06-troubleshooting/07-maintenance-request.md` | 保守依頼 |
