---
title: "D-12. 既存ページを複製して新しいページを作る"
description: "クライアント向けWebflow更新マニュアル：似たデザインの新規ページを作る時の効率的な方法"
sidebar:
  order: 11
  label: "D-12. 既存ページを複製して新しいページを作る"
---


<!-- body-callout:start -->
:::caution[Designer操作の注意]
Designerはサイト全体の見た目や構造を変更できる画面です。小さな変更でも他のページに影響することがあるため、変更前後の画面を見比べながら慎重に進めます。
:::
<!-- body-callout:end -->

「キャンペーンページの第2弾を作りたい」「サービスページに似た新しいページが欲しい」といった時、既存ページを <strong>複製</strong> することで、デザインを一から作らなくて済みます。

---

## 1. ページ複製のメリット

- <strong>デザインの統一感</strong> が保てる
- <strong>作業時間の大幅短縮</strong>（一からの設計が不要）
- <strong>既存ページのレイアウトをベース</strong> にできる

## 2. ページ複製の手順（Designer モード）

1. Designer モードで対象サイトを開く
2. 左サイドバーの <strong>「Pages」</strong> アイコン（紙のマーク）をクリック
3. 複製したいページを <strong>右クリック</strong>（または「・・・」メニューを開く）
4. <strong>「Duplicate（複製）」</strong> を選択
5. 新しいページが「ページ名 (1)」のような名前で作成される
6. 新ページを選択 → <strong>Settings</strong>（歯車アイコン）でページ名・URLスラッグを変更
7. 必要箇所をテキスト・画像差し替えで編集
8. <strong>Publish</strong> で公開

:::note[キャプチャー差し込み位置]
Pagesパネルで対象ページを右クリックし、`Duplicate` が表示されている画面をここに追加します。保存ファイル名は `src/assets/captures/manual/d-11-page-duplicate-menu.png`。複製を実行する前のメニュー表示状態で撮影してください。
:::

## 3. 複製後にやるべきこと

複製ページは <strong>元ページの設定を引き継ぐ</strong> ため、以下を必ず確認・修正してください：

| 項目 | チェック内容 |
|---|---|
| <strong>ページタイトル（SEO Title）</strong> | 元のままだと検索結果で重複扱い。必ず変更 |
| <strong>メタディスクリプション</strong> | 元のままだと SEO 上不利。新しいページ内容に合わせて書く |
| <strong>OGP画像</strong> | SNS シェア時の画像。新ページに合った画像に差し替え |
| <strong>URLスラッグ</strong> | 元と同じだと作成エラー。固有のスラッグに変更 |
| <strong>本文</strong> | 各セクションのテキスト・画像を新内容に差し替え |
| <strong>CTA リンク</strong> | フォームや問い合わせのリンク先が正しいか確認 |
| <strong>アンカーリンク</strong> | 内部の `#section` リンクが正しく動作するか確認 |

## 4. 注意事項

- <strong>CMS テンプレートページ（記事ページなど）は複製できません</strong>。CMS テンプレートは Designer の特殊な仕組みで動作するため、新規追加するには <strong>CMS Collection の構造を Designer 側で設計</strong> する必要があります（[IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) からご相談ください）
- <strong>複製後は必ず Publish が必要</strong> です。複製しただけでは公開サイトには反映されません

## 5. よくある質問 (Q&A)

#### Q. 複製したページが Designer 上では見えるのに、公開サイトに表示されません。

複製ページが <strong>Draft（下書き）</strong> 状態の可能性があります。Page Settings で「Draft」のチェックを外し、Publish を実行してください。


#### Q. 複製したページの URL を変えるにはどうすればいいですか？

Page Settings の <strong>「Slug」</strong> 欄を編集します。例: 元 `/campaign-spring` → 新 `/campaign-summer`


#### Q. 元ページに加えた変更を、複製ページにも反映させたいです。

残念ながら <strong>複製後は別ページとして独立</strong> するため、自動同期はされません。両方を手動で更新するか、共通部分を <strong>Components（コンポーネント）</strong> として [IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) から設計を依頼する方法があります。


---

<strong>次のステップ:</strong>
これで Designer モードの基本機能は完了です。次は便利な設定編へ進みましょう → 「Google検索結果に出るページのタイトルを変更する方法 (SEO)」
