---
title: "検索エンジンの表示制御（sitemap・noindex）"
description: "クライアント向けWebflow更新マニュアル：Googleなどの検索結果への表示・非表示を制御する方法"
sidebar:
  order: 10
  label: "検索エンジンの表示制御"
---

> 新規追加（標準スコープ補完）

「特定のページは Google の検索結果に出したくない」「サイト全体のページ一覧を Google に正しく伝えたい」といった、検索エンジンとの付き合い方の基本設定です。

---

## 1. 知っておくべき2つの仕組み

| 用語 | 役割 | 設定場所 |
|---|---|---|
| **sitemap.xml** | サイト内の全ページ一覧を検索エンジンに伝える | 自動生成（基本は触らない） |
| **noindex** | 「このページは検索結果に出さないで」と指示 | ページごとの設定 |

## 2. sitemap.xml の確認

Webflow は **sitemap.xml を自動生成** します。確認するには：

1. 自社サイトの URL の末尾に `/sitemap.xml` を付けてアクセス
   - 例: `https://example.com/sitemap.xml`
2. XML 形式でサイトの全ページが一覧表示されればOK

### Google Search Console への登録

サイトを Google に効率的にインデックスしてもらうため、Search Console に sitemap を登録することが推奨されます。これは **制作担当者が初期セットアップ** していますが、確認したい場合：

1. Google Search Console にログイン
2. 左メニュー「Sitemap」を開く
3. `sitemap.xml` が登録されているか確認

## 3. ページごとに「検索結果に出さない」設定（noindex）

特定ページを検索結果に出したくない場合：

### 個別ページの場合（Designer）

1. Designer モードを開く
2. 対象ページの **Page Settings**（歯車アイコン）を開く
3. **「Indexing」** または **「Search settings」** セクションを確認
4. **「Disable indexing for this page」** または **「Exclude from sitemap.xml」** をON
5. **Publish** で反映

### サイト全体を一時的に非公開にする場合

サイトリニューアル中など、**サイト全体を検索結果から外したい時**：

1. Project Settings → **「SEO」** タブを開く
2. **「Disable Webflow subdomain indexing」** をON
3. **Publish**

> **注意**: サイト全体の noindex は **解除を忘れると検索結果に永遠に出ません**。リニューアル後の解除を必ず確認してください。

## 4. robots.txt について

`robots.txt` は検索エンジン（クローラー）への指示ファイルです。Webflow は **基本的なrobots.txt を自動生成** しています。

URLの末尾に `/robots.txt` を付けて確認できます：
- 例: `https://example.com/robots.txt`

カスタマイズが必要な場合は **制作担当者に依頼** してください。クライアント側での編集は推奨されません。

## 5. よくある「noindex」を使う場面

- **サンクスページ**（フォーム送信完了画面）
- **テスト用ページ**
- **会員限定ページ**
- **キャンペーン終了後のページ**

逆に、**通常の自社紹介ページや商品ページ・ブログ記事は noindex にしない** でください。SEO 的な機会損失になります。

## 6. よくある質問 (Q&A)

Q. noindex を設定したら、すぐに検索結果から消えますか？
A. いいえ、Google が再クロールして反映するまで **数日〜数週間** かかります。緊急性がある場合は Google Search Console の「URL の削除」機能も併用してください。

Q. sitemap.xml に新しい記事がすぐ載りません。
A. Webflow は通常 **公開時に sitemap.xml を自動更新** します。反映されない場合は Project Settings → SEO で sitemap の再生成を試してください。

Q. 「特定のページだけ Google に表示させたい」という設定はありますか？
A. それは Webflow 側ではなく **検索エンジン側の挙動** です。コンテンツの質と被リンクで決まるため、SEO 対策（記事の充実、内部リンクなど）が必要になります。

---

**次のステップ:**
これで便利な設定編は完了です。次はトラブル解決編へ進みましょう → 「変更を保存したのに、サイトに反映されません！」
