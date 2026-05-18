---
title: "公開SEOキーワード方針 2026-05-18"
description: "Webflow更新マニュアル公開に向けた検索流入キーワード、主要導線、計測設定の整理"
sidebar:
  order: 999
---

# 公開SEOキーワード方針 2026-05-18

## 狙う検索意図

このサイトは、Webflowを初めて触る担当者が「どう更新すればよいか」を調べる検索流入を狙います。制作会社向けの高度な実装記事ではなく、非エンジニアが作業前に確認する日本語マニュアルとして設計します。

## 主要キーワード

| 優先 | キーワード | 対応ページ |
| --- | --- | --- |
| P0 | Webflow 更新方法 | `/`, `/01-getting-started/00-site-update-overview/` |
| P0 | Webflow 使い方 日本語 | `/`, `/01-getting-started/10-webflow-ui-glossary/` |
| P0 | Webflow Content Editor 使い方 | `/02-editor/00-editor-complete-guide/`, `/02-editor/02-open-content-editor/` |
| P0 | Webflow CMS 更新 | `/03-cms/00-blog-post-complete-guide/`, `/03-cms/01-where-is-cms/` |
| P1 | Webflow SEO設定 | `/05-settings/00-site-settings-complete-guide/`, `/05-settings/01-seo-title/`, `/05-settings/02-seo-description/` |
| P1 | Webflow フォーム 確認 | `/05-settings/04-form-submissions/`, `/05-settings/06-form-csv-download/` |
| P1 | Webflow Localization 使い方 | `/07-localization/00-localization-overview/` |
| P1 | Webflow 反映されない | `/06-troubleshooting/01-cache-not-reflecting/` |

## 実装済みSEO対策

- サイト全体のtitle / descriptionを公開検索向けに変更
- トップページのtitle / description / tagline / 本文に主要キーワードを自然に追加
- `robots.txt` を追加し、公開クロールとsitemapを明示
- `WebSite` のJSON-LD構造化データを追加
- `robots` metaで `index,follow` と大きい画像プレビューを許可
- OGP / Twitter Cardの基本metaを追加
- GTMコンテナ `GTM-PGPXHQBZ` をhead scriptとnoscript iframeで追加
- GTMは `PUBLIC_GTM_ID` を設定すると別コンテナIDに差し替え可能
- Google Search Console verificationを `PUBLIC_GOOGLE_SITE_VERIFICATION` で差し込めるようにした

## GTM / Search Console設定

本番ビルド時に以下の環境変数を設定します。

```txt
PUBLIC_GTM_ID=GTM-PGPXHQBZ
PUBLIC_GOOGLE_SITE_VERIFICATION=xxxxxxxxxxxxxxxxxxxxxxxx
```

Google Tag Managerは、環境変数が未設定でも `GTM-PGPXHQBZ` が出力されます。別コンテナに差し替える場合だけ `PUBLIC_GTM_ID` を設定します。Search ConsoleのHTML meta verificationは、`PUBLIC_GOOGLE_SITE_VERIFICATION` が設定されている時だけ出力されます。

## 次に強化するとよいこと

- Search Console公開後に、実際の検索クエリを見てページtitleを調整する
- `Webflow CMS 更新`, `Webflow SEO設定`, `Webflow フォーム 確認` の各ページで、冒頭文に検索意図に近い一文を追加する
- 実際の質問が集まったら、`FAQPage` 構造化データを主要FAQページに追加する
- 公開後に `sitemap-index.xml` がSearch Consoleで正常取得されるか確認する
