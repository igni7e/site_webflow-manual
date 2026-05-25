import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const siteUrl = 'https://webflow-manual.ignitejp.com';
const gtmId = process.env.PUBLIC_GTM_ID || 'GTM-PGPXHQBZ';
const googleSiteVerification = process.env.PUBLIC_GOOGLE_SITE_VERIFICATION;

export default defineConfig({
  site: siteUrl,
  redirects: {
    '/03-cms/26-morbido-cms-field-guide/': '/03-cms/26-booost-cms-field-guide/',
  },
  integrations: [
    starlight({
      title: 'IGNITE Webflow更新マニュアル',
      description: 'Webflowの更新方法、Content Editor、CMS投稿、SEO設定、フォーム確認、Localizationを日本語で解説する公開版Webflowマニュアル。',
      locales: {
        root: { label: '日本語', lang: 'ja' },
      },
      customCss: ['./src/styles/custom.css'],
      components: {
        SkipLink: './src/components/GtmSkipLink.astro',
      },
      head: [
        ...(googleSiteVerification
          ? [
              {
                tag: 'meta',
                attrs: {
                  name: 'google-site-verification',
                  content: googleSiteVerification,
                },
              },
            ]
          : []),
        {
          tag: 'meta',
          attrs: {
            name: 'robots',
            content: 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1',
          },
        },
        {
          tag: 'meta',
          attrs: {
            name: 'keywords',
            content:
              'Webflow 更新方法, Webflow 使い方, Webflow CMS 更新, Webflow Editor, Webflow Content Editor, Webflow 日本語 マニュアル, Webflow SEO設定, Webflow フォーム確認, Webflow Localization',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:site_name',
            content: 'IGNITE Webflow更新マニュアル',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:type',
            content: 'website',
          },
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:card',
            content: 'summary_large_image',
          },
        },
        {
          tag: 'script',
          attrs: { type: 'application/ld+json' },
          content: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: 'IGNITE Webflow更新マニュアル',
            alternateName: ['Webflow更新マニュアル', 'Webflow日本語マニュアル'],
            url: siteUrl,
            inLanguage: 'ja',
            description:
              'Webflowの更新方法、Content Editor、CMS投稿、SEO設定、フォーム確認、Localizationを日本語で解説する公開版Webflowマニュアル。',
            publisher: {
              '@type': 'Organization',
              name: 'IGNITE',
              url: 'https://igni7e.jp/',
            },
            about: [
              'Webflow 更新方法',
              'Webflow CMS 更新',
              'Webflow Content Editor',
              'Webflow SEO設定',
              'Webflow Localization',
            ],
          }),
        },
        ...(gtmId
          ? [
              {
                tag: 'script',
                content: `
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','${gtmId}');
`,
              },
            ]
          : []),
        {
          tag: 'script',
          attrs: { type: 'module' },
          content: `
const key = 'ignite-sidebar-scroll-top';
const getSidebar = () => document.getElementById('starlight__sidebar');
const saveSidebarScroll = () => {
  const sidebar = getSidebar();
  if (!sidebar) return;
  sessionStorage.setItem(key, String(sidebar.scrollTop));
};
const restoreSidebarScroll = () => {
  const sidebar = getSidebar();
  const stored = Number(sessionStorage.getItem(key) || 0);
  if (!sidebar || !stored) return;
  requestAnimationFrame(() => {
    sidebar.scrollTop = stored;
  });
};
const bindSidebarScroll = () => {
  const sidebar = getSidebar();
  if (!sidebar || sidebar.dataset.igniteScrollBound) return;
  sidebar.dataset.igniteScrollBound = 'true';
  sidebar.addEventListener('scroll', saveSidebarScroll, { passive: true });
};
const initSidebarScroll = () => {
  bindSidebarScroll();
  restoreSidebarScroll();
};
const initExternalLinks = () => {
  const currentHost = window.location.host;
  for (const link of document.querySelectorAll('a[href]')) {
    const rawHref = link.getAttribute('href');
    if (!rawHref || rawHref.startsWith('#') || rawHref.startsWith('mailto:') || rawHref.startsWith('tel:')) continue;
    const url = new URL(rawHref, window.location.href);
    if (url.host === currentHost) continue;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  }
};
const initPageEnhancements = () => {
  initSidebarScroll();
  initExternalLinks();
};
document.addEventListener('DOMContentLoaded', initPageEnhancements);
document.addEventListener('astro:page-load', initPageEnhancements);
document.addEventListener('click', (event) => {
  if (event.target instanceof Element && event.target.closest('a[href]')) saveSidebarScroll();
}, true);
window.addEventListener('pagehide', saveSidebarScroll);
window.addEventListener('beforeunload', saveSidebarScroll);
`,
        },
      ],
      sidebar: [
        { label: 'A. はじめの一歩', autogenerate: { directory: '01-getting-started' } },
        { label: 'WORK. やりたいことから探す', autogenerate: { directory: 'work' } },
        { label: 'B. Content Editor', autogenerate: { directory: '02-editor' } },
        { label: 'C. CMS更新', autogenerate: { directory: '03-cms' } },
        { label: 'D. デザイナー', autogenerate: { directory: '04-designer' } },
        { label: 'E. Locale翻訳', autogenerate: { directory: '07-localization' } },
        { label: 'F. 便利な設定', autogenerate: { directory: '05-settings' } },
        { label: 'G. トラブル解決', autogenerate: { directory: '06-troubleshooting' } },
      ],
      social: {
        github: 'https://github.com/igni7e/site_webflow-manual',
      },
      lastUpdated: true,
      pagination: true,
    }),
  ],
});
