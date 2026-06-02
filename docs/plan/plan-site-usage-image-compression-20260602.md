---
title: "Site Usage と画像容量注意の追加計画"
description: "WebflowのSite usage確認ページ追加と、画像圧縮・Bandwidth注意の追記計画"
sidebar:
  order: 0
---

# Site Usage と画像容量注意の追加計画

## 目的

Webflowの `Usage / Site usage` を確認するページを追加し、画像が重い場合はアップロード失敗だけでなくBandwidth使用量にも影響することを明記する。

## 作業項目

- [x] 添付画像を `src/assets/captures/manual/f-10-site-usage-bandwidth.png` として取り込む。
- [x] `05-settings/11-site-usage-bandwidth.md` を新規作成する。
- [x] `06-troubleshooting/02-image-upload-failed.md` にSite usage、Bandwidth、画像圧縮の注意を追記する。
- [x] `02-editor/06-replace-image.md` にBandwidth注意を追記する。
- [x] `03-cms/10-insert-image.md` にBandwidth注意を追記する。
- [x] `05-settings/00-site-settings-complete-guide.md` から新ページへリンクする。
- [x] `npm run build` で確認する。

## 参照

- Webflow公式: Bandwidth overview
- Webflow公式: Assets panel
- Webflow公式: Responsive images
