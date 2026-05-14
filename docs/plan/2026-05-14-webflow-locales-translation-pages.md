---
title: Webflow Locale翻訳ページ追加
date: 2026-05-14
---

# Webflow Locale翻訳ページ追加

- [x] 既存の多言語ページと公式情報を確認する
- [x] Locale機能と翻訳手順の新規ページを追加する
- [x] 既存の多言語ガイドから新規ページへリンクする
- [x] ビルドと表記チェックを実行する

## 確認結果

- Webflow公式Help Center / Webflow Wayを確認して反映。
- `04-designer/12-locale-translation-workflow.md` を新規追加。
- 既存の `04-designer/00-localization-designer-guide.md` から新規ページへリンク。
- `npm run build` 成功。新規ページを含め84ページ生成。
- 内部リンクチェックは83ファイルすべてOK。
- ブラウザで新規ページの表示を確認。
- `git diff --check` 問題なし。
