# AGENTS.md - site_webflow-manual

## プロジェクト概要

クライアント向け Webflow 更新マニュアル。Astro Starlight 採用。日本語デフォルト。

## 編集規則

- 全 `.md` ファイルは **frontmatter 必須**：`title` / `description` / `sidebar.order`
- ファイル名は `NN-スラッグ.md`（NN は2桁数字、カテゴリ内連番）
- 本文に `#1` `#超重要` 等のタグ記法は使わない（Obsidian側ルールに準拠）
- 見出しは H1=タイトル、H2=主要セクション、H3=サブセクション
- Webflow 用語は英語表記を維持（Editor, Designer, Publish, CMS, Asset Panel 等）

## カテゴリ

- `01-getting-started/` はじめの一歩（招待〜ログイン〜ダッシュボード）
- `02-editor/` Editor モード操作
- `03-cms/` CMS（ブログ・お知らせ）
- `04-designer/` Designer モード（注意付き）
- `05-settings/` SEO・フォーム・ドメイン等
- `06-troubleshooting/` Q&A・トラブル解決

## ターゲット読者

非エンジニアのクライアント担当者。専門用語は初出時に必ず日本語で説明する。

## コミットメッセージ

`feat:` `fix:` `docs:` `chore:` プレフィックス。日本語OK。
