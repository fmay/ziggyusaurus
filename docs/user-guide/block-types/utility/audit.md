---
title: Audit
---

# Audit

The Audit block allows you to write data to an external data source so a process auditor
can track data at a point in time. 

You could use the [Data Store](Data-Store.md) block to achieve a similar objective. 
The advantage of the Audit block is the ability to manage the user interaction through any BI tool 
by connecting to the Snowflake database (see below).

This allows them to easily connect a reporting tool and run reports or searches.

While you could go to the target system and review the data, examining all fields can be difficult
if the dta is spread across many screens.

Using the Audit, you can easily perform random searches and then view the data in a view or Card.

The current implementation writes data to Snowflake. Other platforms can be added upon request.

![Audit flow](/img/flows/blocks/utility/audit/audit-flow.png){width=1200}

## Prerequisites and Connection
**Important** : your Snowflake table must be named `AUDIT_LOG`.

You should use this Snowflake SQL to create your table. Adapt `AUDIT.PUBLIC` (database and schema) 
as you like, but leave `AUDIT_LOG`.

```SQL
create or replace TABLE AUDIT.PUBLIC.AUDIT_LOG (
	ID NUMBER(38,0) autoincrement start 1 increment 1 noorder,
	NAMESPACE VARCHAR(255) NOT NULL,
    IDENTIFIER VARCHAR(255),
	EXECUTION_UUID VARCHAR(255),
	PRIMARY_KEY VARCHAR(255),
	SECONDARY_KEY VARCHAR(255),
	DATA VARCHAR(16777216),
	IS_ERROR BOOLEAN DEFAULT FALSE,
	CREATED_TIMESTAMP TIMESTAMP_NTZ(9) DEFAULT CURRENT_TIMESTAMP()
);
```

You should configure a Snowflake [Connection](/user-guide/connections/Connections) in the connection manager. The config field will 
look something like this.

```JavaScript
{
  account: 'zo96510.eu-west-1',
  username: 'your_user_name',
  // password: secrets.SNOWFLAKE_PASSWORD,
  authenticator: "SNOWFLAKE_JWT",
  privateKey: secrets.SNOWFLAKE_PRIVATE_KEY,
  warehouse: 'ZIGGY_AUDIT',
  database: 'AUDIT',
  schema: 'PUBLIC',
  timeout: 30000,
}
```

The above example uses key pair authentication. If you want to use basic authentication, you will need to 
configure this properly in Snowflake and then remove the `authenticator` and `privateKey` fields.

During a Snowflake trial, using basic authentication is fine. Once you have signed up, however, Snowflake enforces 
MFA authentication which means you should generate your keypair and configure this in Snowflake.

## Block fields
### Topic
This is a name given to identify a group of log entries. Let's say you were migrating a CRM system. 
An auditor might want to validate what Customer data was written to the target CRM system.

### Identifier
This is another field that you can write to to help segment your data. 

For example, if you are migrating from a source CRM platform to a target CRM platform, you might enter the
following **identifier** values.

- **source** when you read data from the source platform
- and then later in the Flow **target** once you have performed all transformations and write to the target platform.

### Primary Key
This is a value you want to search on. For example, you might choose the edge data key that contains the customer name.

### Secondary Key
This is a second value you want to search on. For example, you might choose the edge data key that contains the registered company number.

## Data Written

- `DATA` - the entire incoming data record is stored in this field in JSON format.
- The `IS_ERROR` field is set if the entry was created during error handling (see below).
- `EXECUTION_UUID` will contain the execution id of the Flow.

Note that there will also be an [Execution History](/user-guide/editor/Execution-history) entry.

## Error handling
When an Audit block is used when handling errors, the only fields that are written are 
the `TOPIC` `IDENTIFIER` and `EXECUTION_UUID` fields. 

The `data` field in the data store will contain the Flows error object. 
