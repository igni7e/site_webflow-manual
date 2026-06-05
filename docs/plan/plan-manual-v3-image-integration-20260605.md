---
title: "Manual v3 image integration plan"
description: "マニュアルv3で追加されたWebflow管理画面キャプチャーを本文へ差し込む作業計画"
sidebar:
  order: 0
---

# Manual v3 image integration plan

## Goal

`/Users/das/Downloads/マニュアルv3` に追加されたPNG画像を `src/assets/captures/manual/` に取り込み、対応する本文内のキャプチャー指示を実画像へ置き換える。

## Checklist

- [x] 追加画像を確認し、番号ずれのある `f-06` / `f-10` の用途を判断する
- [x] PNG画像を `src/assets/captures/manual/` にコピーする
- [x] 対象Markdownの `キャプチャー指示` / `キャプチャー差し込み位置` を画像に差し替える
- [x] `docs/human-capture-shot-list.md` と `docs/additional-capture-request-2026-06-02.md` に反映済みステータスを追記する
- [x] 画像参照とビルドを検証する

## Decisions

- `f-06-form-submissions-export-all.png` はCSV出力画面ではなく通知先メール設定画面のため、`05-settings/05-form-notification-email.md` の画像として使う。
- `f-07-form-submissions-export-all.png` はCSV出力画面として `05-settings/06-form-csv-download.md` に使う。
- `f-10-page-indexing-settings.png` と `f-11-page-indexing-settings.png` は同じSitemap indexing設定のON/OFF違い。本文の主画像は `f-11`、補足画像として `f-10` も検索表示制御ページ内で使う。
- 画像圧縮やリサイズは、ビルドまたは表示上の問題が出た場合のみ行う。

## Verification

- `node` によるMarkdown画像参照チェックで、`src/content/docs` 内の `assets/captures/manual` 参照がすべて存在することを確認した。
- 今回対象ファイル名に紐づく本文内の `キャプチャー指示` / `キャプチャー差し込み位置` は残っていないことを確認した。
- `npm run build` は成功した。既存のStarlight duplicate id警告とPagefind警告は継続して出ているが、ビルドは完了した。
- ローカルサーバーで代表ページがHTTP 200を返すことを確認し、ビルドログで今回追加した画像が最適化対象に入っていることを確認した。
