---
title: "F-8. お問い合わせフォームに項目を追加・削除する"
description: "クライアント向けWebflow更新マニュアル：問い合わせフォームの入力項目を変更する方法"
sidebar:
  order: 7
  label: "F-8. お問い合わせフォームに項目を追加・削除する"
---


<!-- body-callout:start -->
:::caution[作業前に止まるポイント]
削除、復元、非公開、公開設定、Designer操作は影響が大きい作業です。実行ボタンを押す前に、対象ページ名、対象アイテム、公開先をもう一度確認してください。迷う場合は作業を止めて担当者へ共有します。
:::
<!-- body-callout:end -->


> 新規追加（標準スコープ補完）

「お問い合わせフォームに『業種』を追加したい」「『FAX番号』はもう不要なので削除したい」といった、フォーム自体の編集について解説します。
*実画面例: フォーム項目の変更前に、Forms画面で現在のフォーム構成と送信履歴を確認します。*

---

## 1. 重要な前提

フォーム項目（フィールド）の追加・削除・並び替えは <strong>Designer モードでの作業</strong> です。エディターからはできません。

> <strong>注意</strong>: <strong>フォーム編集はサイト構造に影響します</strong>。誤った操作で <strong>既存の問い合わせ受信が止まる</strong> リスクがあるため、必ず <strong>作業前にバックアップを取る</strong> または [IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) から依頼することをおすすめします。

## 2. フォーム編集の基本フロー

1. Designer モードを開く
2. 対象ページのフォーム要素をクリックして選択
3. <strong>新規フィールドの追加 / 削除 / ラベル変更</strong>
4. <strong>Form Settings</strong> で送信後の挙動・通知先を確認
5. <strong>Publish</strong> して公開
6. <strong>テスト送信</strong> して問い合わせが正常に届くか確認

## 3. 項目を追加する手順

1. Designer でフォーム要素をクリック
2. 左サイドバーの <strong>「Add（+）」</strong> から、追加したい入力タイプを選ぶ
   - <strong>Text Input</strong>（一行テキスト：会社名、業種など）
   - <strong>Text Area</strong>（複数行テキスト：詳細欄）
   - <strong>Email Input</strong>（メールアドレス専用）
   - <strong>Phone Input</strong>（電話番号専用）
   - <strong>Select Dropdown</strong>（プルダウン選択）
   - <strong>Radio Button</strong>（単一選択）
   - <strong>Checkbox</strong>（複数選択 / 同意チェック）
3. 追加した要素をフォーム内の希望位置にドラッグ
4. 要素を選択し、Settings パネルで <strong>Name（フィールド名）</strong> と <strong>Label（表示ラベル）</strong> を設定
5. 必要に応じて <strong>Required（必須）</strong> をONに
6. <strong>Publish</strong> して公開

## 4. 項目を削除する手順

1. Designer でフォーム内の削除したい入力欄をクリック
2. キーボードの <strong>Delete</strong> キーを押す（または右クリック → Delete）
3. <strong>Publish</strong> して公開

> <strong>注意</strong>: 削除前に「過去の問い合わせデータでこのフィールドを使っていないか」を確認してください。

## 5. 項目の並び順を変える

1. Designer でフォーム要素を <strong>ドラッグ & ドロップ</strong> で並び替え
2. <strong>Publish</strong> して公開

## 6. 必須項目（Required）の設定

ユーザーが入力しないと送信できないように設定する機能です。

1. 対象フィールドを選択
2. Settings パネルの <strong>「Required」</strong> をON
3. Publish

## 7. テスト送信は必ず実施

フォーム編集後は <strong>必ずテスト送信</strong> をしましょう：

1. 公開サイトで実際にフォームを開く
2. 全項目を入力して送信
3. <strong>指定の通知メールアドレスに届くか</strong> を確認
4. Webflow 管理画面の Form Submissions にも記録されているか確認

## 8. よくある質問 (Q&A)

#### Q. フォーム項目を追加したら、過去のデータはどうなりますか？

過去の問い合わせデータは変わりません。<strong>新規追加項目は今後の送信から記録</strong> されます。


#### Q. 削除した項目を元に戻したいです。

直後なら <strong>Ctrl+Z（Cmd+Z）</strong> で取り消せます。Publish 後の場合は <strong>バックアップから復元</strong> か、再度同じ項目を追加する必要があります。


#### Q. 自分でやるのが不安です。

[IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) から依頼することを強くおすすめします。フォーム関連は問い合わせ受信に直結するため、慎重な対応が必要です。


---

<strong>次のステップ:</strong>
複数人で Webflow を編集したい場合の方法を学びましょう → 「Webflow の共同編集者を招待する」
