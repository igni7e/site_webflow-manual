---
title: "Final remaining capture merge plan"
description: "残っているキャプチャー差し込み位置を確認し、反映可能な画像をmainへマージする計画"
sidebar:
  order: 0
---

# Final remaining capture merge plan

## Goal

残っているキャプチャー指示を確認し、利用できる画像を本文へ反映して `main` へマージ・プッシュする。

## Checklist

- [x] 残っているキャプチャー指示と画像ファイルの所在を照合する
- [x] 反映可能な画像を本文へ差し込む
- [x] 見つからない画像がある場合は反映不可として記録する
- [x] `npm run build` で検証する
- [ ] コミットして `main` へプッシュする

## Current findings

- 旧Legacy Editor用の `b-02-editor-canvas-opened.png` は既に `src/assets/captures/manual/` に存在する。
- `d-05-clean-up-assets-menu.png` と `f-09-invite-member-role-modal.png` は、現時点で `/Users/das/Downloads/マニュアルv3` と `マニュアルv3.zip` には含まれていない。
- `/Users/das/Downloads` 内の近い名前のPNGと直近スクリーンショットを確認したが、`Clean up assets` メニューまたは `Invite member` モーダルに該当する画像は見つからなかった。

## Verification

- `src/content/docs/02-editor/01-open-legacy-editor.md` の2箇所を `b-02-editor-canvas-opened.png` に差し替えた。
- `npm run build` は成功した。
- 残る本文内キャプチャー指示は `d-05-clean-up-assets-menu.png` と `f-09-invite-member-role-modal.png` の2箇所のみ。
