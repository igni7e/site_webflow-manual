---
title: "Python図解のAI生成画像差し替え計画 final7 2026-05-25"
description: "残っているPython生成図解7件をAI生成画像へ差し替える実装TODO。"
---

# Python図解のAI生成画像差し替え計画 final7 2026-05-25

## 方針

- 残っている `src/assets/diagrams/manual/diagram-*.svg` の本文参照7件を、AI生成PNGへ差し替える。
- 生成画像は `src/assets/ai-diagrams/manual/` に保存する。
- 元SVGは削除せず、本文参照だけを差し替える。

## TODO

- [x] 残り7件の参照先と用途を確認する
- [x] Webflow用語・初回ログイン確認のAI生成画像を作成する
- [x] Morbido CMS Field・検索表示制御のAI生成画像を作成する
- [x] 画像アップロード・404・保守依頼のAI生成画像を作成する
- [x] 対象ページの画像参照をAI生成画像に差し替える
- [x] `docs/diagram-inventory-2026-05-22.md` に差し替えメモを追記する
- [x] `npm run build` で検証する
- [ ] mainへマージしてpushする
