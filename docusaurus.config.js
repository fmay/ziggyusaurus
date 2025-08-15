const config = {
  title: 'Ziggy Documentation',
  url: 'https://docs.ziggyservices.com',
  baseUrl: '/',
  organizationName: 'ziggyservices',
  projectName: 'ziggyusaurus',
  
  // Algolia DocSearch configuration
  algolia: {
    // The application ID provided by Algolia
    appId: 'YOUR_ALGOLIA_APP_ID',
    
    // Public API key: it is safe to commit it
    apiKey: 'YOUR_ALGOLIA_SEARCH_API_KEY',
    
    indexName: 'ziggyusaurus',
    
    // Optional: see doc section below
    contextualSearch: true,
    
    // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
    externalUrlRegex: 'external\\.com|domain\\.com',
    
    // Optional: Replace parts of the item URLs from Algolia search results. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
    replaceSearchResultPathname: {
      from: '/docs/', // or as RegExp: /\/docs\//
      to: '/',
    },
    
    // Optional: Algolia search parameters
    searchParameters: {},
    
    // Optional: path for search page that enabled by default (`false` to disable it)
    searchPagePath: 'search',
    
    // Set this to "false" if you only want to enable search on the search page
    // Set this to "true" if you want to enable search on all pages
    searchBarPosition: 'right',
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
      },
    ],
  ],
  
  // Enable search functionality
  plugins: [
    require.resolve('@easyops-cn/docusaurus-search-local'),
  ],
};

module.exports = config;
