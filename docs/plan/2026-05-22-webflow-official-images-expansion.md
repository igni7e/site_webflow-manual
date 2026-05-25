---
title: Webflow公式画像追加TODO 2026-05-22
description: Webflow公式Help Centerの画像をマニュアル内に追加するための作業計画。
---

# Webflow公式画像追加TODO 2026-05-22

## 目的

Webflow公式Help Centerで公開されている画像を活用し、最新版Content EditorやWebflow画面の説明ページに視覚情報を増やす。

## TODO

- [x] Webflow公式Help Centerから利用できる画像URLを確認する
- [x] 公式画像を保存または参照する方針を決める
- [x] 画像を置く専用ページまたは既存ページの差し込み位置を決める
- [x] 公式画像をマニュアル本文へ追加する
- [x] frontmatter、内部リンク、ビルドを確認する
- [ ] commitしてmainへpushする

## 方針

- Webflow Help Center本文はCloudflareで直接画像URL取得が制限されるため、Help Center画像は公式ページURLを明記した `公式画像差し込み位置` として管理する。
- Webflow公式サイト `Create and edit website content with edit mode` から取得できるOG画像は本文に直接埋め込む。
- 実際のBooost画面でしか判断できない箇所は、従来どおり `src/assets/captures/manual/` に保存するキャプチャー指示として残す。
