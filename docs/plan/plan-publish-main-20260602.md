---
title: "GitHub main公開計画"
description: "Webflow更新マニュアルのローカル変更をGitHub mainへ公開する計画"
sidebar:
  order: 0
---

# GitHub main公開計画

## 目的

ローカルで反映したWebflow更新マニュアルの修正を、GitHubの `main` ブランチへコミットしてpushする。

## 作業項目

- [x] 現在のブランチが `main` であることを確認する。
- [x] リモートが `origin` / `https://github.com/igni7e/site_webflow-manual.git` であることを確認する。
- [x] 一時ファイルを除外し、マニュアル本文・画像・計画ファイルだけをステージ対象にする。
- [x] `npm run build` が成功していることを確認する。
- [ ] コミットを作成する。
- [ ] `origin/main` へpushする。
