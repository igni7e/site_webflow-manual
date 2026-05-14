import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://webflow-manual.ignitejp.com',
  integrations: [
    starlight({
      title: 'IGNITE Webflow更新マニュアル',
      description: 'IGNITE提供の公開版Webflowサイト更新マニュアル',
      locales: {
        root: { label: '日本語', lang: 'ja' },
      },
      customCss: ['./src/styles/custom.css'],
      head: [
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
        { label: 'B. Content Editor', autogenerate: { directory: '02-editor' } },
        { label: 'C. CMS更新', autogenerate: { directory: '03-cms' } },
        { label: 'D. デザイナー', autogenerate: { directory: '04-designer' } },
        { label: 'E. 便利な設定', autogenerate: { directory: '05-settings' } },
        { label: 'F. トラブル解決', autogenerate: { directory: '06-troubleshooting' } },
        { label: 'G. Locale翻訳', autogenerate: { directory: '07-localization' } },
      ],
      social: {
        github: 'https://github.com/igni7e/site_webflow-manual',
      },
      lastUpdated: true,
      pagination: true,
    }),
  ],
});
