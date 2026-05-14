---
title: Locale翻訳セクション分割
date: 2026-05-14
---

# Locale翻訳セクション分割

- [x] 既存のLocaleページと現在のナビゲーション構成を確認する
- [x] `G. Locale翻訳` セクションを追加する
- [x] Locale関連ページを複数ページに分割する
- [x] 既存リンクとトップページの導線を更新する
- [x] ビルド、内部リンク、表示確認を実行する

## 確認結果

- `astro.config.mjs` に `G. Locale翻訳` セクションを追加。
- `src/content/docs/07-localization/` を新設し、6ページ構成に分割。
- 旧 `04-designer/12-locale-translation-workflow.md` は削除し、D章からG章へ誘導する形に整理。
- トップページに `G. Locale翻訳` の導線を追加。
- `npm run build` 成功。89ページ生成。
- 内部リンクチェックは88ファイルすべてOK。
- 旧 `/04-designer/12-locale-translation-workflow/` 参照は残っていないことを確認。
- ブラウザで `/07-localization/00-localization-overview/` を表示確認。
- `git diff --check` 問題なし。
