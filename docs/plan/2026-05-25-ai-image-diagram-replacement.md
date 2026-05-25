---
title: "Python図解のAI生成画像差し替え計画 2026-05-25"
description: "見づらいPython生成図解のうち、初心者の理解に直結する図解をAI生成画像へ差し替えるための実装TODO。"
---

# Python図解のAI生成画像差し替え計画 2026-05-25

## 方針

- Python生成SVGを全削除せず、分かりにくさが強い図解から段階的に差し替える。
- Webflowの実UIを正確に見せる必要がある箇所は実キャプチャーを優先し、概念説明だけAI生成画像にする。
- AI生成画像内の細かい文字は信用しない。本文側の見出し・説明・キャプションで意味を補う。
- 生成画像は `src/assets/ai-diagrams/manual/` に保存する。

## TODO

- [x] 置き換え対象のPython図解を確認する
- [x] 「編集アイコンが出る条件」のAI生成画像を作成する
- [x] 「テキスト修正の安全手順」のAI生成画像を作成する
- [x] 「画像差し替えの判断」のAI生成画像を作成する
- [x] Workspace / Site / Plan系のAI生成画像を作成する
- [x] Editor / Designer / Content Editor / Publish系のAI生成画像を作成する
- [x] CMS / Slug / 公開状態系のAI生成画像を作成する
- [x] Domain / cacheトラブル系のAI生成画像を作成する
- [x] 対象ページの画像参照をAI生成画像に差し替える
- [x] `docs/diagram-inventory-2026-05-22.md` に差し替え方針を追記する
- [x] `npm run build` で検証する

## 対象ページ

- `src/content/docs/02-editor/13-latest-content-editor-screen-guide.md`
- `src/content/docs/02-editor/03-edit-text.md`
- `src/content/docs/02-editor/06-replace-image.md`
- `src/content/docs/01-getting-started/00-workspace-intro.md`
- `src/content/docs/01-getting-started/00-plan-role-decision.md`
- `src/content/docs/01-getting-started/00-workspace-plan.md`
- `src/content/docs/01-getting-started/00-site-plan.md`
- `src/content/docs/01-getting-started/00-open-site.md`
- `src/content/docs/01-getting-started/07-editor-vs-designer.md`
- `src/content/docs/01-getting-started/08-editor-only-recommendation.md`
- `src/content/docs/02-editor/02-open-content-editor.md`
- `src/content/docs/02-editor/08-save-and-publish.md`
- `src/content/docs/02-editor/12-before-publish-checklist.md`
- `src/content/docs/03-cms/00-blog-post-complete-guide.md`
- `src/content/docs/03-cms/02-create-new-post.md`
- `src/content/docs/03-cms/03-post-title.md`
- `src/content/docs/03-cms/16-save-as-draft.md`
- `src/content/docs/03-cms/18-edit-published.md`
- `src/content/docs/03-cms/25-cms-before-publish-checklist.md`
- `src/content/docs/05-settings/09-domain-status.md`
- `src/content/docs/06-troubleshooting/01-cache-not-reflecting.md`
