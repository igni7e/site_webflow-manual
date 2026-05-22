---
title: A-1. Webflow更新作業の全体像
description: はじめてWebflowを触る担当者向けに、Content editor roleでのログインから公開前確認までの流れをまとめます。
sidebar:
  order: 0
  label: "A-1. 更新作業の全体像"
---


<!-- body-callout:start -->
:::tip[最初に見る場所]
迷った時は、まずDashboardで対象サイト名を確認します。似た名前のサイトやテスト環境がある場合は、編集前に正しいサイトか確認してから進めます。
:::
<!-- body-callout:end -->

![Webflow Dashboardのサイト一覧](../../../assets/captures/manual/a-01-dashboard-site-list.png)


# A-1. Webflow更新作業の全体像

このページは、Webflowで作られたWebサイトを更新する前に読む入口です。2026年現在、Webflowの日常更新は <strong>Content editor role</strong> を使い、Webflowのcanvas上で文章・画像・リンク・CMS記事を更新する流れが基本です。

従来の <strong>Legacy Editor</strong> は2026年8月4日から利用できなくなる予定です。公開版のこのマニュアルでは、古いEditor専用画面ではなく、Content editor roleを前提に説明します。
*実画面例: Webflowにログインすると、編集権限のあるサイトがDashboardに表示されます。まず対象サイトを間違えないことが重要です。*

## 作業の流れ

1. Webflowから届いた招待メールを確認します。
2. アカウントを作成し、ログインできる状態にします。
3. ダッシュボードで対象サイトを確認します。
4. 文章・画像・リンクなどの日常更新はContent editor roleで作業します。
5. ブログ・お知らせなどの投稿はCMSで作業します。
6. 作業後は必ずPreviewや公開サイトで見た目を確認します。
7. 問題がなければPublishします。

## 事前に用意するもの

- Webflowに招待されたメールアドレス
- Webflowのログイン情報
- Google Chrome
- 更新したい文章の原稿
- 差し替えたい画像ファイル
- 変更したいリンク先URL
- 公開前に確認する公開サイトのURL

## 英語画面が不安な場合

Webflowの画面は英語で表示されることがあります。初めての方は、Google Chromeの翻訳機能を使って画面全体の意味を確認すると進めやすくなります。

ただし、翻訳後の日本語だけを見ると、`Publish`、`Designer`、`Delete` などの重要なボタンを見間違える可能性があります。操作前に英語名もあわせて確認してください。

- [Chrome翻訳でWebflowの英語画面を日本語で確認する](/01-getting-started/09-chrome-translate-webflow/)
- [Webflow基本用語の早見表](/01-getting-started/10-webflow-ui-glossary/)

## どの章を読めばよいか

| やりたいこと | 読むページ |
| --- | --- |
| 招待メールから始めたい | [招待メールを確認する](/01-getting-started/01-invitation-email/) |
| アカウントを作成したい | [アカウントを作成する](/01-getting-started/02-create-account/) |
| ログイン直後に何を押すか知りたい | [ログイン直後に押すもの・押さないもの](/01-getting-started/11-after-login-first-steps/) |
| 英語画面を日本語で確認したい | [Chrome翻訳で英語画面を読む](/01-getting-started/09-chrome-translate-webflow/) |
| 文字・画像・リンクを更新したい | [Content Editor入門](/02-editor/00-editor-complete-guide/) |
| ブログやお知らせを投稿したい | [ブログ投稿ガイド](/03-cms/00-blog-post-complete-guide/) |
| フォーム回答を確認したい | [フォーム回答・CSVガイド](/05-settings/00-site-settings-complete-guide/) |
| 多言語サイトを修正したい | [多言語・自動翻訳ガイド](/04-designer/00-localization-designer-guide/) |

## Content editor roleとDesignerの違い

<strong>Content editor role</strong> は、完成済みのサイト上で文章・画像・リンク・CMS記事などを更新するための権限です。デザインやレイアウトを壊さずにコンテンツを更新できるよう、編集範囲が制限されています。

<strong>Designer</strong> は、レイアウト・スタイル・構造・多言語設定などを編集できる画面です。便利ですが、誤操作の影響が大きいため、必要な場合だけ使います。

## 公開前チェック

- 変更した文章に誤字脱字がない
- 画像が正しく表示されている
- リンク先が正しい
- スマートフォン表示で崩れていない
- CMS記事の場合、タイトル・Slug・概要・カテゴリーが入っている
- Publish前に、公開してよい内容か社内確認が済んでいる

## 理解度チェック

1. 日常的な文章・画像・リンクの更新で、まず使うべき役割はどれですか？
   - A. Designer
   - B. Content editor role
   - C. Billing

#### 答え

正解: B

Content editor roleは、完成済みのサイト上で安全にコンテンツを更新するための役割です。Designerはレイアウトや構造も変更できるため、必要な場合だけ使います。


2. Publish前に確認することとして正しいものはどれですか？
   - A. 変更したページだけでなく、スマートフォン表示やリンク先も確認する
   - B. 画像が表示されていれば、文章やリンクは確認しなくてよい
   - C. 社内確認前でも、作業者の判断で必ずPublishする

#### 答え

正解: A

公開後は一般の閲覧者に見えるため、文章、画像、リンク、スマートフォン表示を確認してからPublishします。


3. Webflowの英語画面が不安なときの考え方として正しいものはどれですか？
   - A. 翻訳された日本語だけを見て、英語名は確認しない
   - B. Chrome翻訳や日本語化拡張機能で意味を確認しつつ、PublishやDeleteなどの英語名も確認する
   - C. 英語画面が出たら、すぐDesignerで設定を変更する

#### 答え

正解: B

翻訳は補助として便利ですが、重要なボタンは英語名も見て誤操作を防ぎます。


## 次に進む

招待メールから始める場合は [招待メールを確認する](/01-getting-started/01-invitation-email/) に進んでください。すでにログインできる場合は [ログイン直後に押すもの・押さないもの](/01-getting-started/11-after-login-first-steps/) または [Content Editor入門](/02-editor/00-editor-complete-guide/) から始めて問題ありません。
