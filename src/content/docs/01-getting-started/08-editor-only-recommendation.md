---
title: "普段の更新はContent editor roleでOKです"
description: "クライアント向けWebflow更新マニュアル：普段の更新はContent editor roleで安全に行う"
sidebar:
  order: 8
  label: "普段の更新はContent editor role"
---

<!-- capture-callout:start -->
:::note[キャプチャー指示]
このページには、撮影後に `src/assets/captures/manual/a-08-content-editor-vs-designer-entry.png` を入れてください。
撮影対象: A-08「サイトカード上でContent editor入口とDesigner入口が分かる状態」。通常更新で押すもの、押さないものを比較できる構図

Webflow画面は数秒待ってから撮影し、Loading表示、個人情報、未公開情報が写っていない画像だけを使います。
:::
<!-- capture-callout:end -->

<!-- body-callout:start -->
:::tip[編集の基本]
Content editor roleでは、文章、画像、リンクなどの内容を安全に更新できます。レイアウトやデザインを変えたい時は、無理に触らずDesigner操作が必要か確認してください。
:::
<!-- body-callout:end -->


> 旧マニュアル番号: [No.8](/01-getting-started/08-editor-only-recommendation/)

前のマニュアルでContent editor roleとDesignerの大きな違いについて学びました。このページでは、なぜ日常更新はContent editor roleで十分なのか、そしてContent editor roleを使うことのメリットを整理します。
*実画面例: Designerでは見た目だけでなく構造にも触れます。文章や画像の通常更新だけなら、Content editor roleを優先してください。*

---

## 1. なぜContent editor roleで良いのか？

Webサイト制作会社は、お客様が更新する可能性のある箇所（お知らせ、ブログ、施工実績、事業内容の文章など）を、Content editor roleで安全に編集できるように設計しています。

つまり、<strong>お客様が「更新したいな」と思うであろう箇所のほとんどは、すでにContent editor roleで触れるように準備されている</strong>のです。

デザインの根幹に関わる部分（サイトの全体的なレイアウト、色、フォントの種類、ボタンのデザインなど）は、意図せず変更してブランドイメージを損なうことがないよう、Designerの領域で管理されています。これは、サイトの品質と統一感を保つための重要な仕組みです。

## 2. Content editor roleを使う3つの大きなメリット

### メリット1：とにかく「安全」

Content editor roleでの操作は、決められた範囲内でのテキストや画像の変更が中心です。そのため、「操作を間違えて、サイトのデザインがバラバラに崩れてしまった」というような、最も避けたい事態を防ぎやすくなります。

### メリット2：操作が「直感的」

Content editor roleでは、Webflowのcanvas上で見た目を確認しながら編集できます。文章、画像、リンク、CMSコンテンツを文脈の中で確認しながら更新できます。

### メリット3：更新が「スピーディー」

Designerのような構造編集を避けながら、目的の作業（文章の修正や画像の差し替えなど）を素早く行うことができます。これにより、情報の鮮度を保ち、タイムリーな情報発信が可能になります。

## 3. 「もしも」の時もご安心を

「更新したけど、やっぱり元に戻したい」
そんな時は、公開前であれば変更を取り消せる場合があります。公開後に大きく戻したい場合は、サイトのバックアップから復元する機能（[No.57](/06-troubleshooting/05-backup-restore/)参照）もあります。

## 4. まとめ

- <strong>日常の更新作業は、Content editor roleで進めます。</strong>
- <strong>Content editor roleは「安全」「直感的」「スピーディー」に更新できる安心設計です。</strong>
- <strong>Designerは必要な時だけ開き、まずはContent editor roleでの更新に慣れていきましょう。</strong>

---

<strong>次のステップ:</strong>
ここからはいよいよ、具体的な更新作業の方法に入っていきます。まずは基本の「[No.9](/02-editor/01-open-editor/) 【基本】Content editor roleでWebflowを開く方法」からスタートです。
