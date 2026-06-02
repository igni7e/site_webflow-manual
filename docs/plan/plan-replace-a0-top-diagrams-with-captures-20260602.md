---
title: A0 top diagrams replacement plan
description: A-0-4/A-0-5の冒頭AI図解を実画面キャプチャへ差し替える作業計画
created: 2026-06-02
---

# A0 top diagrams replacement plan

## 目的

ブラウザコメントに基づき、`A-0-4. メンバー追加と権限` と `A-0-5. サイトの修正画面に入る方法` の冒頭画像をAI図解ではなく実際のWebflow画面キャプチャへ変更する。

## 方針

- `00-add-member.md` 冒頭の `member-permissions.png` を `a-09-members-and-permissions.png` に差し替える。
- `00-open-site.md` 冒頭の `content-editor-open-flow.png` を `a-10-open-site-from-dashboard.png` に差し替える。
- 既に本文中にある同一実キャプチャは重複するため削除する。
- コールアウトの文言を `図解の見方` から `画面の見方` へ変更する。

## 進捗

- [x] 対象ページと実キャプチャ候補の確認
- [x] Markdown差し替え
- [x] ビルド確認
- [x] ブラウザ確認

## 検証メモ

- `npm run build` 成功。
- ブラウザで `/01-getting-started/00-add-member/` の冒頭画像が `a-09-members-and-permissions.png` になっていることを確認。
- ブラウザで `/01-getting-started/00-open-site/` の冒頭画像が `a-10-open-site-from-dashboard.png` になっていることを確認。
- 両ページとも本文内の重複画像は削除済み。
