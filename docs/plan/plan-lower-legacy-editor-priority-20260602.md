---
title: Legacy Editor priority reduction plan
description: Content EditorのLegacyモードを補足扱いへ下げるための作業計画
created: 2026-06-02
---

# Legacy Editor priority reduction plan

## 目的

ブラウザコメントの「画像を削除」と、全体方針としてContent EditorのLegacyモードの優先度を下げる依頼に対応する。

## 方針

- `work/06-before-start` からLegacy Editor入口を強調する画像を削除する。
- Legacy Editorページは削除せず、例外時の補足ページとしてサイドバー下部へ移動する。
- Content Editor入門・最新版ページでは、通常導線を最新版Content editor roleに一本化し、Legacyは必要時だけ参照する表現にする。
- 撮影リスト上のLegacy関連キャプチャ優先度を下げる。

## 対象

- `src/content/docs/work/06-before-start.md`
- `src/content/docs/02-editor/00-editor-complete-guide.md`
- `src/content/docs/02-editor/01-open-legacy-editor.md`
- `src/content/docs/02-editor/02-open-content-editor.md`
- `docs/human-capture-shot-list.md`
- `docs/capture-checklist.md`

## 進捗

- [x] 対象箇所の確認
- [x] 本文・サイドバー・画像参照の修正
- [x] ビルド確認
- [x] ブラウザ確認

## 検証メモ

- `npm run build` 成功。
- 既存の Starlight duplicate id 警告は継続して出るが、今回の変更によるビルド失敗はなし。
- ブラウザで `/work/06-before-start/` を再読み込みし、Legacy入口画像 `work-00-content-editor-entry-check.png` が本文から消えていることを確認。
- ブラウザでB章のサイドバー順を確認し、`B-補足. Content Editor（旧バージョン）` が `B-1`、`B-2`、`B-13`、`B-14` の後ろに出ることを確認。
