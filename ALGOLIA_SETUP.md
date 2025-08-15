# Algolia Search Setup Guide for Ziggy Documentation

## Overview
This guide will help you set up Algolia DocSearch for your Ziggy documentation site. Algolia provides powerful, fast search functionality that will help users find content quickly.

## Step 1: Sign Up for Algolia DocSearch

1. Go to [https://docsearch.algolia.com/](https://docsearch.algolia.com/)
2. Click "Apply" to request DocSearch for your site
3. Fill out the application form:
   - **Project name**: Ziggy Documentation
   - **Project URL**: https://docs.ziggyservices.com
   - **Project description**: Documentation for Ziggy integration and migration platform
   - **Contact email**: Your email address
   - **Project type**: Documentation site
   - **Framework**: Docusaurus

## Step 2: Wait for Approval
- Algolia will review your application (usually takes 1-2 business days)
- They'll send you an email with your API credentials
- The service is **free for open source projects**

## Step 3: Get Your API Credentials
Once approved, you'll receive:
- **Application ID** (appId)
- **Search API Key** (apiKey) 
- **Index Name** (indexName)

## Step 4: Update Configuration
Replace the placeholder values in `docusaurus.config.js`:

```javascript
algolia: {
  appId: 'YOUR_ACTUAL_APP_ID',        // Replace this
  apiKey: 'YOUR_ACTUAL_SEARCH_API_KEY', // Replace this  
  indexName: 'YOUR_ACTUAL_INDEX_NAME',   // Replace this
  
  contextualSearch: true,
  searchPagePath: 'search',
}
```

## Step 5: Test the Search
1. Run `npm run build` to build the site
2. Run `npm run serve` to test locally
3. Look for the search icon in the top-right corner of the navbar
4. Click it to test the search functionality

## Current Configuration Status
✅ **Navbar**: Configured with search icon  
✅ **Footer**: Added with navigation links  
✅ **Build**: Successful with no errors  
✅ **Search Bar**: Ready for Algolia integration  

## What You'll Get
- **Fast Search**: Instant search results as users type
- **Smart Ranking**: Results are intelligently ordered by relevance
- **Search Analytics**: See what users are searching for
- **Mobile Optimized**: Works great on all devices
- **Keyboard Navigation**: Full keyboard support for accessibility

## Alternative: Local Search (Optional)
If you prefer local search instead of Algolia, you can:
1. Install a compatible local search plugin
2. Configure it in the plugins section
3. Remove the Algolia configuration

## Next Steps
1. Apply for Algolia DocSearch
2. Wait for approval and credentials
3. Update the configuration with real API keys
4. Test the search functionality
5. Deploy your updated site

## Support
- [Algolia DocSearch Documentation](https://docsearch.algolia.com/docs/)
- [Docusaurus Search Documentation](https://docusaurus.io/docs/search)
- [GitHub Issues](https://github.com/ziggyservices/ziggyusaurus/issues)

---

**Note**: The search icon will appear in your navbar once you add valid Algolia credentials. Until then, it may show a placeholder or not function.
