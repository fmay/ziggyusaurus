const config = {
  title: 'Ziggy Documentation',
  url: 'https://docs.ziggyservices.com',
  baseUrl: '/',
  organizationName: 'ziggyservices',
  projectName: 'ziggyusaurus',
  onBrokenLinks: 'warn', // Temporarily warn instead of fail
  
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
  
  // Search functionality can be added later
  // plugins: [
  //   require.resolve('@easyops-cn/docusaurus-search-local'),
  // ],
};

module.exports = config;
