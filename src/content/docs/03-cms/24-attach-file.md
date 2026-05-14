---
title: "本文にPDFなどのファイルを添付する方法"
description: "クライアント向けWebflow更新マニュアル：ブログ本文からPDF・資料ファイルをダウンロードできるようにする方法"
sidebar:
  order: 24
  label: "本文にファイルを添付"
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に `src/assets/captures/manual/c-27-asset-file-upload.png` を入れてください。
撮影対象: C-27「PDFなどファイルをAssetへアップロード」。Upload、ファイル名、Copy linkが分かる。実資料名は公開OKのもの

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::tip[下書きで確認]
CMS記事は、いきなり公開せず下書き状態でタイトル、本文、画像、リンク、公開日を確認します。特に一覧ページと詳細ページの両方で見え方を確認すると安心です。
:::
<!-- body-callout:end -->


> 新規追加（標準スコープ補完）

「会社案内のPDFをダウンロードできるようにしたい」「セミナー資料を本文からリンクしたい」といった時に使うのが <strong>ファイル添付（リンク）</strong> です。
*実画面例: 資料リンクを入れる場合は、公開ページでリンク導線が自然に見えるか確認します。*

---

## 1. ファイル添付の基本方針

Webflow では、<strong>ファイルを直接埋め込む</strong> のではなく、<strong>「アセットにアップロード → リンクとして本文に貼る」</strong> という流れが基本です。

対応形式の例（一般的なもの）:
- PDF（最も多い）
- Word（.docx）
- Excel（.xlsx）
- PowerPoint（.pptx）
- ZIP

> <strong>注意</strong>: <strong>アップロード可能な最大サイズは 10MB</strong> が目安です。それ以上は分割するか圧縮してください。

## 2. アップロードと添付の手順

### Step 1: アセットにファイルをアップロード

1. Designer モードまたは CMS の編集画面で、画像挿入と同じ要領で <strong>「Asset Manager（アセットマネージャー）」</strong> を開く
2. <strong>「Upload」</strong> をクリックしてファイルを選択
3. アップロード完了後、ファイルの <strong>URL をコピー</strong>

<details>
<summary>キャプチャー指示: Asset ManagerでPDFをアップロードする画面</summary>

- 保存名: `03-24-attach-file-asset-upload.png`
- 差し込み位置: この `Step 1` の手順1の直後
- 撮影画面: WebflowのAsset Managerを開き、PDFファイルをアップロードする直前の画面
- 事前状態: デモ用PDF `sample-company-profile.pdf` を用意し、実在の顧客資料は表示しない
- 強調箇所: `Upload` ボタン、Asset Managerのパネル名、アップロード対象ファイル名
- 隠す情報: 顧客名、社内資料名、未公開ファイル名、ユーザー名
- 撮影後チェック: 読者が「まずAsset ManagerからUploadする」と分かる画面になっていること

</details>

<details>
<summary>キャプチャー指示: アップロード済みファイルのURLをコピーする画面</summary>

- 保存名: `03-24-attach-file-copy-url.png`
- 差し込み位置: この `Step 1` の手順3の直後
- 撮影画面: アップロード済みPDFの詳細メニュー、またはURLコピー操作ができる画面
- 事前状態: デモPDFがAsset Manager内に表示されている状態にする
- 強調箇所: `Copy URL`、ファイル名、URLコピー用のボタンまたはメニュー
- 隠す情報: 実URLに含まれる顧客名、非公開ファイル名
- 撮影後チェック: 本文に貼るURLをどこで取得するか分かること

</details>

### Step 2: 本文にダウンロードリンクを貼る

1. CMS の本文エディタで、リンクにしたいテキスト（例:「会社案内PDF（2.3MB）」）を選択
2. ツールバーの <strong>リンク（鎖アイコン）</strong> をクリック
3. <strong>コピーした URL</strong> を貼り付け
4. <strong>「Open in new tab」をON</strong>（PDF は別タブで開くのが安全）
5. Save

<details>
<summary>キャプチャー指示: CMS本文内でPDFリンクを設定する画面</summary>

- 保存名: `03-24-attach-file-rich-text-link.png`
- 差し込み位置: この `Step 2` の手順2の直後
- 撮影画面: CMS Rich Text本文で「会社案内PDF（2.3MB）」を選択し、リンク設定パネルを開いた状態
- 事前状態: 本文にデモテキストを入力し、リンクにしたい文字列だけを選択しておく
- 強調箇所: 選択中のリンクテキスト、リンクアイコン、URL入力欄、`Open in new tab`
- 隠す情報: 未公開記事本文、実在資料名、顧客サイトURL
- 撮影後チェック: 「テキストを選択してURLを貼る」流れが1枚で分かること

</details>

<details>
<summary>キャプチャー指示: 公開ページでPDFリンクを確認する画面</summary>

- 保存名: `03-24-attach-file-published-check.png`
- 差し込み位置: `Step 2` の手順5の直後
- 撮影画面: Previewまたは公開ページでPDFリンクが表示されている状態
- 事前状態: リンクテキストが本文内に表示され、クリック直前の状態にする
- 強調箇所: PDFリンクのテキスト、ブラウザのURL欄、別タブで開くことが分かる状態
- 隠す情報: 顧客サイトURL、資料の実ファイル名、非公開記事URL
- 撮影後チェック: 読者が「設定後に必ず公開画面でリンク確認する」と分かること

</details>

## 3. リンクテキストの書き方（おすすめ）

ユーザーが安心してクリックできるよう、<strong>ファイルの種類とサイズ</strong> を明記しましょう：

- 良い例: 「会社案内をダウンロード（PDF / 2.3MB）」
- 良い例: 「料金表（Excel / 120KB）」
- 悪い例: 「こちら」「資料」（何が開くか分からない）

## 4. ファイルを差し替える時

<strong>同じ URL を維持したい</strong> 場合は、Asset Manager で <strong>既存ファイルの「Replace」</strong> 機能を使うのがおすすめです。これにより、本文中のリンクを編集しなくてもファイル内容が更新されます。

1. Asset Manager で対象ファイルを選択
2. <strong>「Replace asset」</strong> をクリック
3. 新しいファイルを選択してアップロード
4. URL は変わらないので、本文側の編集は不要

## 5. よくある質問 (Q&A)

<details>
<summary>PDFが直接サイト内で表示されません。</summary>

PDF は基本的に「ダウンロード」または「ブラウザの新しいタブで表示」という挙動になります。サイト内に埋め込み表示したい場合は、別途 PDF ビューア機能の実装が必要です（[IGNITE公式サイトのお問い合わせフォーム](https://igni7e.jp/contact/) からご相談ください）。

</details>

<details>
<summary>アップロードしたファイルを削除したいです。</summary>

Asset Manager から削除できます。ただし <strong>本文にリンクが残っている場合、リンク切れ（404）</strong> になります。事前に本文を確認してから削除してください。

</details>

<details>
<summary>10MBを超えるファイルはどうすれば？</summary>

圧縮（ZIP化）するか、Google Drive 等の外部ストレージにアップロードしてリンクを貼る方法があります。

</details>

---

<strong>次のステップ:</strong>
これで CMS の基本機能は一通り完了です。次は Designer モード編へ進みましょう → 「デザイナーモードを開く時の注意点」
