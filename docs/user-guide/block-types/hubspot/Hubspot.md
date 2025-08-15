---
title: HubSpot Blocks
---

# HubSpot Blocks

HubSpot blocks provide comprehensive integration capabilities with the HubSpot CRM platform. These blocks enable you to read, write, and manage HubSpot data within your Ziggy flows.

## Available HubSpot Blocks

### Data Reading Blocks

- [HubSpot Read](/block-types/hubspot/hs-read) - Read data from HubSpot objects
- [HubSpot Get Associated](/block-types/hubspot/hs-get-associated) - Retrieve associated records
- [HubSpot Get All Owners](/block-types/hubspot/hs-get-all-owners) - Get all HubSpot owners
- [HubSpot Owner Translate](/block-types/hubspot/hs-owner-translate) - Translate owner references

### Data Writing Blocks

- [HubSpot Write](/block-types/hubspot/hs-write) - Create and update HubSpot records
- [HubSpot Create Associations](/block-types/hubspot/hs-create-associations) - Create relationships between records
- [HubSpot Merge](/block-types/hubspot/hs-merge) - Merge duplicate records
- [HubSpot Timeline Write](/block-types/hubspot/hs-timeline-write) - Add entries to contact timelines

## HubSpot Object Types

HubSpot blocks support the following object types:

- **Contacts** - Individual people and their information
- **Companies** - Business organizations
- **Deals** - Sales opportunities and transactions
- **Tickets** - Customer support requests
- **Custom Objects** - Your custom HubSpot objects

## Authentication

HubSpot blocks require proper authentication:

- **API Key**: Your HubSpot API key for authentication
- **Scopes**: Appropriate permissions for the operations you need
- **Rate Limits**: Respect HubSpot's API rate limiting

## Common Use Cases

- **Data Migration**: Import data from other systems into HubSpot
- **Data Synchronization**: Keep HubSpot data in sync with external systems
- **Lead Processing**: Automatically process and qualify leads
- **Customer Onboarding**: Automate customer setup processes
- **Reporting**: Extract data for analysis and reporting

## Best Practices

- **Batch Processing**: Use batch operations for large datasets
- **Error Handling**: Implement proper error handling for API failures
- **Rate Limiting**: Respect HubSpot's API limits and implement backoff strategies
- **Data Validation**: Validate data before sending to HubSpot
- **Testing**: Test with small datasets before processing large amounts

## Configuration Examples

Each HubSpot block can be configured with:

- **Object Type**: Which HubSpot object to work with
- **Properties**: Which fields to read or write
- **Filters**: Conditions for data selection
- **Batch Size**: Number of records to process at once
- **Error Handling**: How to handle failed operations
