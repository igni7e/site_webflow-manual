---
title: "Python図解のAI生成画像差し替え計画 round2 2026-05-25"
description: "残っているPython生成図解のうち、操作判断に関わる主要図解をAI生成画像へ追加差し替えする実装TODO。"
---

# Python図解のAI生成画像差し替え計画 round2 2026-05-25

## 方針

- 残りのPython生成SVGを一括削除せず、操作判断に影響する主要図解から差し替える。
- 実画面キャプチャーが必要なものはキャプチャー指示を優先し、概念説明はAI生成PNGにする。
- 生成画像は `src/assets/ai-diagrams/manual/` に保存する。

## TODO

- [x] 残っているPython図解参照を確認する
- [x] メンバー追加・権限のAI生成画像を作成する
- [x] リンク変更・変更破棄のAI生成画像を作成する
- [x] CMS画像・カテゴリー・Rich Text・本文リンク・非公開操作のAI生成画像を作成する
- [x] Designer / Asset / UndoのAI生成画像を作成する
- [x] SEO / Forms / CSVのAI生成画像を作成する
- [x] LocalizationのAI生成画像を作成する
- [x] 対象ページの画像参照をAI生成画像に差し替える
- [x] `docs/diagram-inventory-2026-05-22.md` に差し替えメモを追記する
- [x] `npm run build` で検証する
