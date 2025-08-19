const config = {
  title: 'Ziggy Documentation - No-Code Data Platform & AI Search',
  tagline: 'Complete guide to Ziggy\'s no-code data platform, flows, blocks, and AI-powered search capabilities',
  url: 'https://docs.ziggyservices.com',
  baseUrl: '/',
  organizationName: 'ziggyservices',
  projectName: 'ziggyusaurus',
  onBrokenLinks: 'warn', // Temporarily warn instead of fail
  favicon: 'img/favicon.ico',
  
  // Improve hot reloading
  customFields: {
    enableHotReload: true,
  },
  
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
        // Enable sitemap generation
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
      },
    ],
  ],

  // Navbar configuration
  themeConfig: {
    navbar: {
      title: 'Documentation',
      logo: {
        alt: 'Ziggy Logo',
        src: 'img/ziggy-logo-light.webp',
        srcDark: 'img/ziggy-logo-dark.webp',
      },
      items: [
        {
          href: 'https://github.com/fmay/ziggyusaurus',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'search',
          position: 'right',
        },
      ],
    },
    
    // Footer configuration (commented out to hide footer)
    /*
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/user-guide',
            },
            {
              label: 'Block Types',
              to: '/user-guide/block-types',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/ziggyservices/ziggyusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Ziggy Services. Built with Docusaurus.`,
    },
    */
    
    // Algolia search configuration
    // You'll need to sign up at https://docsearch.algolia.com/
    // and replace these placeholder values with your actual API keys
    algolia: {
      // The application ID provided by Algolia
      appId: 'XPMSD22TBN',
      
      // Public API key: it is safe to commit it
      apiKey: 'd306c3a1645bb47380811310974fed3b',
      
      indexName: 'Ziggy Docs',
      
      // Optional: see doc section below
      contextualSearch: false,
      
      // Sitemap for crawling
      sitemaps: ["https://docs.ziggyservices.com/sitemap.xml"],
      
      // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
      externalUrlRegex: 'external\\.com|domain\\.com',

      // Optional: Replace parts of the item URLs from Algolia search results. Useful when using the same search index for multiple deployments using a different baseUrl. For example: localhost:3000 vs myCompany.com/docs
      replaceSearchResultPathname: {
        from: '/docs/', // or as RegExp: /\/docs\//
        to: '/',
      },
      
      // Optional: Algolia search parameters
      
      // Optional: path for search page that enabled by default (`false` to disable it)
      searchPagePath: 'search',

      searchParameters: {
        facetFilters: [] // This will remove all tag filtering
      }
    },
  },
};

module.exports = config;
