---
title: Salesforce Blocks
---

# Salesforce Blocks

Salesforce blocks provide comprehensive integration capabilities with the Salesforce CRM platform. These blocks enable you to read, write, and manage Salesforce data within your Ziggy flows.

## Available Salesforce Blocks

### Data Reading Blocks

- [Salesforce Read Object](/user-guide/block-types/salesforce/sf-read-object) - Read data from Salesforce objects
- [Salesforce Get Associated Object](/user-guide/block-types/salesforce/SalesForce-Get-Associated-Object) - Retrieve associated records

### Data Writing Blocks

- [Salesforce Write Object](/user-guide/block-types/salesforce/sf-write-object) - Create and update Salesforce records
- [Salesforce Set Associations](/user-guide/block-types/salesforce/SalesForce-Set-Assciations) - Create relationships between records

### Utility Blocks

- [Salesforce Owner Translate](/user-guide/block-types/salesforce/SalesForce-Owner-Translate) - Translate owner references

## Salesforce Object Types

Salesforce blocks support the following object types:

- **Standard Objects**: Accounts, Contacts, Leads, Opportunities, Cases
- **Custom Objects**: Your custom Salesforce objects
- **Related Lists**: Associated records and relationships
- **External Objects**: Data from external systems

## Authentication

Salesforce blocks require proper authentication:

- **Username/Password**: Your Salesforce credentials
- **Security Token**: Additional security token for API access
- **OAuth**: For more secure authentication flows
- **API Limits**: Respect Salesforce's API rate limiting

## Common Use Cases

- **Data Migration**: Import data from other systems into Salesforce
- **Data Synchronization**: Keep Salesforce data in sync with external systems
- **Lead Processing**: Automatically process and qualify leads
- **Customer Onboarding**: Automate customer setup processes
- **Reporting**: Extract data for analysis and reporting
- **Workflow Automation**: Trigger actions based on data changes

## Best Practices

- **Batch Processing**: Use batch operations for large datasets
- **Error Handling**: Implement proper error handling for API failures
- **Rate Limiting**: Respect Salesforce's API limits and implement backoff strategies
- **Data Validation**: Validate data before sending to Salesforce
- **Testing**: Test with small datasets before processing large amounts
- **Field Mapping**: Ensure proper field mapping between systems

## Configuration Examples

Each Salesforce block can be configured with:

- **Object Type**: Which Salesforce object to work with
- **Fields**: Which fields to read or write
- **Filters**: SOQL conditions for data selection
- **Batch Size**: Number of records to process at once
- **Error Handling**: How to handle failed operations
- **Relationship Fields**: How to handle related records

## SOQL Support

Salesforce blocks support SOQL (Salesforce Object Query Language) for:

- **Complex Queries**: Multi-object queries with relationships
- **Filtering**: Conditional data selection
- **Sorting**: Ordering results by specific fields
- **Limiting**: Controlling the number of returned records