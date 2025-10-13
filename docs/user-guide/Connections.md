---
title: Connections
description: Learn how to set up and manage connections to external systems in Ziggy. Connect to APIs, databases, and services for seamless data integration.
keywords: [ziggy connections, external systems, api integration, database connections, system setup]
image: /img/ziggy-logo-light.webp
---

# Connections

Connections are hooks into external modules along with a corresponding setup that you can reference from

- a Javascript Block
- a Block that relies on that Connection as a part of its configuration.

Connections are managed the Ziggy UI.

![Connections](/img/flows/connections/connections-listing.png)

The following connection types are currently supported.

- **Hubspot**
- **SalesForce**
- **SFTP** 
- **AWS S3**
- **Postgres**
- **SQL Server**
- **Snowflake**

It is very easy to add any other connection types. 
Anything that is available as an NPM module can be quickly added.

## Configuration
The configuration you enter is an object. The example below shows a Hubspot connection object.

<img src="/img/flows/connections/connections-object-general.png" alt="Connection object" width="500" />

### Development and Production
Note that you can specify a different connection object for Development and Production modes. 
[Click here](/user-guide/Dev-Prod-Modes) for details on switching modes.

### Secrets
It is good practice to use the [Secrets Manager](Secrets) 
to avoid exposing sensitive information in the Connection object. 

You can specify a secret as shown in the above screenshot.

### Test Connection
Use the Test Connection button to test your connection definition. You (currently) need to save and open the dialog again to test after making changes.

## OpenAI/ChatGPT

```javascript

{
apiKey: 'your-api-key',
organization: 'your-org-****',
project: 'your-proj-***'
}
```

## Elastic Search
The typical connection objects are shown below. Full details can be found in [Elastic docs](https://www.elastic.co/docs/reference/elasticsearch/clients/javascript/getting-started). The Ziggy connection object is what you are looking for. Note that the object is different for Severless, Hosted and Local offerings. 

Serverless
```javascript
{
  node: 'https://my-elasticsearch-project-xxxx.es.eu-west-1.aws.elastic.cloud:443',
  auth: {
    apiKey: secrets.ELASTIC_API_KEY
  }
  serverMode: 'serverless',
}
```

Hosted
```javascript
{
    cloud: {
        id: 'My_deployment:your_deployment_id='
    },
    auth: {
        username: 'elastic',
        password: secrets.MY_ELASTIC_PW
    }
}
```

## Hubspot object

```javascript
{
    accessToken: secrets.HUBSPOT_API_KEY,
    numberOfApiCallRetries: 5,
}
```

## SalesForce object

```javascript
{
    username: "myemail4@agentforce.com",
    password: "H8KK87KHJA7JGH7",
    token: '987JHGehKJHh7KJh8wOiu77dd'
}
```


## SFTP object

```javascript
{
    host: 'my-sftp-server.com',
    port: '22',
    username: 'a8759b3dxxxxxx70c146ed99fc2xxxx',
    password: 'XMsxxxxry8yN5flxxxxBEktDGV2Rw'
}
```

## AWS S3 object
```javascript
{
    region: 'us-east-1',
    credentials: {
    accessKeyId: secrets.S3ExperimentorKeyId,
    secretAccessKey: secrets.S3ExperimentorSecret,
  },
}
```

## Upsales
```javascript
{
url: 'https://power.upsales.com/api/v2/',
apiKey: secrets.UPSALES_API_KEY
}
```

## Postgres
```javascript
{
    host: 'connectionUrl',
    user: 'username',
    password: 'password',
    database: 'my_database',
    port: 5432
}
```

## SQL Server
```javascript
{
  user: 'user-name',
  password: 'password',
  database: 'database-name',
  server: 'server-name',
  options: {
    encrypt: true, // required for Azure
    trustServerCertificate: false
  }
}
```

## Snowflake
SnowFlake can be tricky to configure. The recommended configuration is to use an access token, which is shown below.

You will need to create this in SnowFlake first.

The following must be done by an ADMIN user. 

### Create a Network Policy
CREATE NETWORK POLICY MY_PAT_POLICY
ALLOWED_IP_LIST = ('0.0.0.0/1', '128.0.0.0/1')
BLOCKED_IP_LIST = ()
COMMENT = 'Network policy for programmatic access token from Node.js server';

### Attach Policy
ALTER USER USER_NAME
ADD PROGRAMMATIC ACCESS TOKEN NEW_PAT_NAME
NETWORK_POLICY = MY_PAT_POLICY
DAYS_TO_EXPIRY = 365;

This will generate a new PAT that will be displayed and must be copied immediately.

Note that the reported errors are generally misleading and all parameters will need to be checked regardless of error message.

```javascript
{
  account: 'XXXXXX-XXXXXX',
  username: 'USER_NAME',
  password: 'eyJ.......',
  authenticator: 'PROGRAMMATIC_ACCESS_TOKEN',
}
```


[TODO] : screenshots, Test buttons