import { mkdir, readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();
const docsDir = path.join(root, 'src/content/docs');
const imageDir = path.join(root, 'src/assets/captures');
const inventoryPath = path.join(root, 'docs/capture-checklist.md');
const imagePattern = /!\[([^\]]*)\]\(https:\/\/uploads-ssl\.webflow\.com\/xxxxxxxx\/xxxxxxxx_([A-Za-z0-9]+)\.png\)[ \t]*/g;
const oldLocalImagePattern = /!\[([^\]]*)\]\(\.\.\/_images\/captures\/([^)]+)\)[ \t]*/g;
const localImagePattern = /!\[([^\]]*)\]\(\.\.\/\.\.\/\.\.\/assets\/captures\/([^)]+)\)/g;

const categoryLabels = {
  '01-getting-started': 'A. はじめの一歩',
  '02-editor': 'B. エディター',
  '03-cms': 'C. CMS更新',
  '04-designer': 'D. デザイナー',
  '05-settings': 'E. 便利な設定',
  '06-troubleshooting': 'F. トラブル解決',
};

function escapeXml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function toKebab(value) {
  return value
    .replace(/([a-z0-9])([A-Z])/g, '$1-$2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1-$2')
    .toLowerCase();
}

async function listMarkdownFiles(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name.startsWith('_')) continue;
      files.push(...await listMarkdownFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(fullPath);
    }
  }
  return files.sort();
}

function createSvg(title, sourceName) {
  const safeTitle = escapeXml(title || sourceName);
  const safeSource = escapeXml(sourceName);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">
  <title id="title">${safeTitle}</title>
  <desc id="desc">Webflow manual capture placeholder. Replace this SVG with the real screenshot.</desc>
  <rect width="1280" height="720" fill="#f8fafc"/>
  <rect x="56" y="56" width="1168" height="608" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="56" y="56" width="1168" height="72" rx="18" fill="#111827"/>
  <circle cx="100" cy="92" r="10" fill="#ef4444"/>
  <circle cx="132" cy="92" r="10" fill="#f59e0b"/>
  <circle cx="164" cy="92" r="10" fill="#10b981"/>
  <text x="96" y="226" fill="#0f172a" font-family="Arial, sans-serif" font-size="42" font-weight="700">${safeTitle}</text>
  <text x="96" y="290" fill="#475569" font-family="Arial, sans-serif" font-size="26">実際のWebflow画面キャプチャに差し替えてください</text>
  <rect x="96" y="344" width="520" height="44" rx="8" fill="#e2e8f0"/>
  <rect x="96" y="416" width="760" height="44" rx="8" fill="#e2e8f0"/>
  <rect x="96" y="488" width="620" height="44" rx="8" fill="#e2e8f0"/>
  <rect x="912" y="344" width="216" height="144" rx="14" fill="#dbeafe" stroke="#60a5fa" stroke-width="2"/>
  <text x="936" y="424" fill="#1d4ed8" font-family="Arial, sans-serif" font-size="28" font-weight="700">Capture</text>
  <text x="96" y="604" fill="#64748b" font-family="Arial, sans-serif" font-size="20">${safeSource}</text>
</svg>
`;
}

await mkdir(imageDir, { recursive: true });

const rows = [];
const files = await listMarkdownFiles(docsDir);

for (const filePath of files) {
  const original = await readFile(filePath, 'utf8');
  let changed = false;
  const relativeFromRoot = path.relative(root, filePath);
  const category = relativeFromRoot.split(path.sep)[3] || '';

  let next = original.replace(imagePattern, (match, alt, sourceName) => {
    const fileName = `${toKebab(sourceName)}.svg`;
    const imagePath = path.join(imageDir, fileName);
    const relativeImage = path.relative(path.dirname(filePath), imagePath).split(path.sep).join('/');
    changed = true;
    return `![${alt}](${relativeImage})`;
  });

  next = next.replace(oldLocalImagePattern, (match, alt, fileName) => {
    const imagePath = path.join(imageDir, fileName);
    const relativeImage = path.relative(path.dirname(filePath), imagePath).split(path.sep).join('/');
    changed = true;
    return `![${alt}](${relativeImage})`;
  });

  if (changed) {
    await writeFile(filePath, next);
  }

  for (const match of next.matchAll(localImagePattern)) {
    const [, alt, fileName] = match;
    rows.push({
      category,
      page: relativeFromRoot,
      alt,
      sourceName: fileName.replace(/\.[^.]+$/, ''),
      fileName,
    });
  }
}

const uniqueImages = new Map();
for (const row of rows) {
  if (!uniqueImages.has(row.fileName)) {
    uniqueImages.set(row.fileName, row);
    await writeFile(
      path.join(imageDir, row.fileName),
      createSvg(row.alt, row.sourceName),
    );
  }
}

const inventoryRows = rows
  .sort((a, b) => a.page.localeCompare(b.page) || a.fileName.localeCompare(b.fileName))
  .map((row) => `| ${categoryLabels[row.category] || row.category} | \`${row.page}\` | ${row.alt} | ![${row.alt}](../src/assets/captures/${row.fileName}) | 未撮影 |`)
  .join('\n');

const inventory = `---
title: "Webflowマニュアル キャプチャ収集チェックリスト"
description: "Webflow更新マニュアルで必要なスクリーンショットの収集一覧"
sidebar:
  order: 1
---

# Webflowマニュアル キャプチャ収集チェックリスト

このファイルはObsidianで確認するためのキャプチャ一覧です。各画像は現在、仮のローカル画像です。実際のWebflow画面を撮影したら、同じファイル名で \`src/assets/captures/\` に上書きしてください。

## 撮影ルール

- 対象サイトにログインした状態で撮影する
- 個人情報、メールアドレス、顧客名、非公開ドメインが写る場合はマスクする
- 画像サイズは横1280px前後を目安にする
- ファイル名は変更せず、既存のSVGをPNGまたはJPGに差し替える場合はMarkdown側の拡張子も合わせて変更する
- Editor、Designer、CMS、SettingsなどWebflowの英語UI名はそのまま残す

## キャプチャ一覧

| カテゴリ | 掲載ページ | 撮影対象 | 現在の画像 | 状態 |
|---|---|---|---|---|
${inventoryRows}
`;

await writeFile(inventoryPath, inventory);
