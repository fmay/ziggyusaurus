const config = {
  title: 'Ziggy Docs',
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

  // Load Poppins font from Google Fonts
  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: 'anonymous',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap',
      },
    },
  ],

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
        src: 'img/ziggy-z-light.svg',
        srcDark: 'img/ziggy-z-dark.svg',
      },
      items: [
        {
          href: 'https://github.com/fmay/ziggyusaurus',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'custom-docsearch',
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
    
    // Algolia search configuration - DISABLED (using custom DocSearch component instead)
    // algolia: {
    //   appId: 'XPMSD22TBN',
    //   apiKey: 'd306c3a1645bb47380811310974fed3b',
    //   askAi: 'IPIDvjstyBlu',
    //   indexName: 'Ziggy Docs',
    //   contextualSearch: false,
    //   sitemaps: ["https://docs.ziggyservices.com/sitemap.xml"],
    //   externalUrlRegex: 'external\\.com|domain\\.com',
    //   replaceSearchResultPathname: {
    //     from: '/docs/',
    //     to: '/',
    //   },
    //   searchPagePath: 'search',
    //   searchParameters: {
    //     facetFilters: []
    //   }
    // },
  },
};

module.exports = config;
