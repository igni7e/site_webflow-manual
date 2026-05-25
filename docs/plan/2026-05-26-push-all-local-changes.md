---
title: "ローカル変更一括push計画 2026-05-26"
description: "現在のローカル変更を検証し、commitしてorigin/mainへpushするためのTODO。"
sidebar:
  order: 999
---

# ローカル変更一括push計画 2026-05-26

## 方針

- 既存の作業差分を勝手に巻き戻さず、現在の内容をそのままcommit対象にする。
- push前に `npm run build` で最低限の公開ビルドを確認する。
- commit後に `origin/main` へpushし、localとremoteの同期状態を確認する。

## TODO

- [x] 現在の変更範囲を確認する
- [x] 全変更をstageする
- [x] `npm run build` で検証する
- [ ] commitを作成する
- [ ] `origin/main` へpushする
- [ ] push後の状態を確認する
