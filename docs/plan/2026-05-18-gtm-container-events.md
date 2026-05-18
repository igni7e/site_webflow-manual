---
title: "GTMイベント設定追加計画"
description: "GTM-PGPXHQBZ export JSONにGA4イベント、トリガー、変数を追加する作業計画"
sidebar:
  order: 999
---

# GTMイベント設定追加計画

- [x] `GTM-PGPXHQBZ_v2.json` の既存タグ、変数、GA4 Measurement IDを確認する
- [x] 既存GA4タグを全ページ配信用に維持する
- [x] 主要行動イベント用のGA4イベント計測タグを追加する
- [x] JSONとして再読み込みできることを検証する
- [x] 変更後のタグ、トリガー、変数の一覧を確認する
- [x] IGNITEサイト遷移と問い合わせ導線を個別イベントとして追加する
- [x] Custom HTML一括計測を削除し、GTM標準の変数・トリガー・GA4 Eventタグ構成へ作り直す
- [x] 完成したGTM export JSONを `docs/gtm/GTM-PGPXHQBZ_v2.json` に保存する

## 追加イベント

- `manual_outbound_click`
- `manual_file_download`
- `manual_form_submit`
- `manual_search_open`
- `manual_engaged_30s`
- `manual_ignite_site_click`
- `manual_contact_click`

## GA4側でキーイベント候補

- `manual_form_submit`
- `manual_contact_click`
- `manual_ignite_site_click`
- `manual_file_download`
