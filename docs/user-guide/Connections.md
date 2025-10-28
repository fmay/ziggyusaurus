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

See below for the currently available connection types.

It is very easy to add any other connection types. Please inquire if you would like a new Connection type to be added.

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
    apiKey: 'your-api-key | secrets.******',
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
    apiKey: 'apiKey | secrets.******',
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
        password: 'password | secrets.*****'
    }
}
```

## Hubspot object

```javascript
{
    accessToken: 'apiKey | secrets.*******',
    numberOfApiCallRetries: 5,
}
```

## SalesForce object

```javascript
{
    username: "myemail@agentforce.com",
    password: "password  | secrets.******",
    token: 'token | secrets.******'
}
```


## SFTP object

```javascript
{
    host: 'my-sftp-server.com',
    port: '22',
    username: 'username',
    password: 'password  | secrets.******'
}
```

## AWS S3 object
```javascript
{
    region: 'us-east-1',
    credentials: {
      accessKeyId: 'keyId | secrets.******',
      secretAccessKey: 'key | secrets.******',
    },
}
```

## Upsales
```javascript
{
    url: 'https://power.upsales.com/api/v2/',
    apiKey: 'apiKey | secrets.******'
}
```

## Postgres
```javascript
{
    host: 'connectionUrl',
    user: 'username',
    password: 'password | secrets.******',
    database: 'my_database',
    port: 5432
}
```

## SQL Server
```javascript
{
  user: 'user-name',
  password: 'password | secrets.******',
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
  password: 'eyJ....... | secrets.******',
  authenticator: 'PROGRAMMATIC_ACCESS_TOKEN',
}
```

## AWS MQQT
```javascript
{
    endPoint: 'xxxxxx-ats.iot.us-east-1.amazonaws.com',
    clientId: 'my-thing-name',
    certificate: '-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE----- | secrets.******',
    privateKey: '-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY----- | secrets.******',
    ca: '-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE----- | secrets.******',
}
```

## Generic MQQT
Use this for MQTT platforms other than AWS IoT Core.

### TLS Enabled

```javascript
{
    brokerUrl: 'mqtt.example.com',
    port: 8883,
    clientId: 'my-client-id',
    tlsEnabled: true,
    username: 'username',
    password: 'password | secrets.******',
    caCert: '-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE----- | secrets.******',
    clientCert: '-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE----- | secrets.******',
    clientKey: '-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY----- | secrets.******',
}
```

### No TLS
```javascript
{
    brokerUrl: 'mqtt.example.com',
    port: 1883,
    clientId: 'my-client-id',
    tlsEnabled: false,
    username: 'username',
    password: 'password | secrets.******',
    caCert: 'ca-certificate | secrets.******',
    clientCert: 'client-certificate | secrets.******',
    clientKey: 'client-private-key | secrets.******',
}
```



