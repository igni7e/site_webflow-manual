---
title: Designer mode wording adjustment plan
description: Designerモードを開いた場合の注意文言を、自己責任と通常更新はEditor推奨の表現に調整する計画
created: 2026-06-02
---

# Designer mode wording adjustment plan

## 目的

`01-getting-started/07-editor-vs-designer.md` の「誤ってデザイナーを開いてしまったら」周辺を、Designerを開くこと自体を禁止する表現ではなく、変更を加えた場合の影響と通常更新はContent editor role推奨であることが伝わる文面に修正する。

## 進捗

- [x] 対象文言の確認
- [x] Markdown修正
- [x] ビルド確認

## 検証メモ

- `npm run build` 成功。
- 既存の Starlight duplicate id 警告は継続して出るが、今回の変更によるビルド失敗はなし。
