import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://webflow-manual.ignitejp.com',
  integrations: [
    starlight({
      title: 'Webflow更新マニュアル',
      description: 'クライアント向けWebflowサイト更新マニュアル（IGNITE提供）',
      defaultLocale: 'ja',
      locales: {
        ja: { label: '日本語', lang: 'ja' },
      },
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        { label: 'A. はじめの一歩', autogenerate: { directory: '01-getting-started' } },
        { label: 'B. エディター', autogenerate: { directory: '02-editor' } },
        { label: 'C. CMS更新', autogenerate: { directory: '03-cms' } },
        { label: 'D. デザイナー', autogenerate: { directory: '04-designer' } },
        { label: 'E. 便利な設定', autogenerate: { directory: '05-settings' } },
        { label: 'F. トラブル解決', autogenerate: { directory: '06-troubleshooting' } },
      ],
      social: {
        github: 'https://github.com/igni7e/site_webflow-manual',
      },
      lastUpdated: true,
      pagination: true,
    }),
  ],
});
