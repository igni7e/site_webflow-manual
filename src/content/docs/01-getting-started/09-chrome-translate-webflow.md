---
title: "Webflowの英語画面を日本語で確認する"
description: "Webflowの管理画面が英語で分かりにくい時に、IGNITEのChrome拡張機能とChrome翻訳を使って画面を読みやすくする方法を説明します。"
sidebar:
  order: 9
  label: "英語画面を日本語で読む"
---

> 旧マニュアル番号: なし

Webflowの管理画面は英語で表示されることがあります。英語のままでも作業できますが、初めての方はボタン名や説明文で迷いやすいため、IGNITEでは **Webflow 日本語化 Chrome拡張機能** の利用をおすすめします。

このページでは、IGNITEが提供しているChrome拡張機能と、Chrome標準の翻訳機能の使い分けを説明します。

## まずおすすめ: Webflow 日本語化 Chrome拡張機能

Webflowを継続的に使う担当者には、IGNITE提供のChrome拡張機能 **Webflow 日本語化** の利用がおすすめです。

- [Webflow 日本語化 - Chrome Web Store](https://chromewebstore.google.com/detail/webflow-%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%8C%96/efenpjcceehojemnphkinocffloghhon)

この拡張機能は、Webflowの管理画面UIを日本語に近づけるためのChrome拡張機能です。Chrome Web Store上では、発行元は **IGNITE Co., Ltd.** と表示されています。

主に次の画面で使えます。

- Dashboard
- Designer
- Site Settings
- Site access
- その他のWebflow管理画面

> **ヒント**: Chromeのページ翻訳は画面全体を機械翻訳します。一方、Webflow 日本語化拡張機能はWebflow管理画面向けの翻訳辞書を使うため、日常的にWebflowを操作する場合はこちらの方が使いやすいです。

## インストール手順

1. Google Chromeで [Webflow 日本語化 - Chrome Web Store](https://chromewebstore.google.com/detail/webflow-%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%8C%96/efenpjcceehojemnphkinocffloghhon) を開きます。
2. 「Add to Desktop」またはChromeに追加するボタンをクリックします。
3. 確認画面で拡張機能の追加を許可します。
4. WebflowのDashboardやDesignerを開き直します。
5. Webflowの管理画面が日本語化されているか確認します。

## 拡張機能を使う時の注意点

- Webflowの公開サイト、つまり `webflow.io` や独自ドメインで表示される一般向けサイトには影響しません。
- CMS、Bodyなど、一部の技術用語は英語のまま残る場合があります。
- Webflowの画面変更により、一部の表示が英語のまま残る場合があります。
- 重要な操作では、翻訳後の日本語だけでなく、元の英語名も確認してください。

## Chrome翻訳も補助的に使う

たとえば、次のような英語が日本語で読みやすくなります。

| 英語表示 | 意味 |
| --- | --- |
| Dashboard | サイト一覧の管理画面 |
| Editor | 文章・画像・リンクなどを更新する画面 |
| Designer | サイトの構造やデザインを編集する画面 |
| Publish | 変更を公開する |
| Save as Draft | 下書きとして保存する |
| Collection | ブログやお知らせなどをまとめる箱 |

## ページ全体を日本語に翻訳する

1. Google ChromeでWebflowを開きます。
2. アドレスバー右側に表示される翻訳アイコンをクリックします。
3. 翻訳先の言語で「日本語」を選びます。
4. 画面全体の英語表示が日本語に変わったことを確認します。

翻訳アイコンが出ない場合は、ページ内の何もない場所を右クリックし、表示されるメニューから「日本語に翻訳」を選びます。

## 翻訳アイコンが出ない時

Chromeの設定で翻訳機能がオフになっている可能性があります。

1. Chrome右上のメニューを開きます。
2. 「設定」を開きます。
3. 「言語」を開きます。
4. 「Google 翻訳を使用する」をオンにします。
5. 必要に応じて、翻訳先の言語を日本語にします。

## 翻訳したまま作業する時の注意点

Chrome翻訳は便利ですが、Webflowのボタン名や項目名が実際と少し違う日本語になることがあります。

特に次の言葉は、英語名も一緒に覚えておくと安全です。

| 翻訳後に見える言葉 | 実際に覚える英語 | 注意点 |
| --- | --- | --- |
| 公開、発行 | Publish | 押すと公開サイトに反映されます |
| デザイナー | Designer | 通常更新では基本的に開きません |
| コレクション | Collection | ブログ・お知らせなどの投稿管理です |
| 下書き | Draft | まだ公開されていない状態です |
| スラッグ | Slug | URLの末尾です。公開前に確認します |

## IGNITE推奨の使い方

- 日常的にWebflowを使う場合は、まずWebflow 日本語化拡張機能を入れる。
- 拡張機能で翻訳されない説明文やヘルプ文は、Chrome翻訳で補助的に読む。
- 実際に押すボタンは、日本語表示だけでなく英語名も確認する。
- `Publish`、`Designer`、`Delete`、`Archive` など影響が大きいボタンは、押す前に一度止まる。
- 迷った時はスクリーンショットを撮って、IGNITEの制作担当者へ確認する。

## 参考

- [ページを翻訳する、Chrome の言語を変更する - Google Chrome ヘルプ](https://support.google.com/chrome/answer/173424?co=GENIE.Platform%3DDesktop&hl=ja-JP)
- [Webflow 日本語化 - Chrome Web Store](https://chromewebstore.google.com/detail/webflow-%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%8C%96/efenpjcceehojemnphkinocffloghhon)

## 次に進む

Webflowの英語UIでよく出る単語は [Webflow基本用語の早見表](/01-getting-started/10-webflow-ui-glossary/) で確認できます。
