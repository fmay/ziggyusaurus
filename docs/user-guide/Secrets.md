---
title: Secrets
description: Securely manage API keys, passwords, and sensitive data in Ziggy flows. Complete guide to secrets management and security best practices.
keywords: [ziggy secrets, security, api keys, configuration, sensitive data, encryption]
image: /img/ziggy-logo-light-bg.webp
---

# Secrets

The Secrets Manager can be accessed from the nav bar.

![Secrets](/img/secrets/secrets-listing.png)

## Add/Edit secret
To add a new secret, press the **+Secret** button. Click on the row to edit an existing secret.

<img src="/img/secrets/secret-dialog.png" alt="Dialog" width="500" />

- The **Name** field should not contain spaces and is limited to characters that are permitted in a Javascript variable.
- Add **Tags** if you have a lot of secrets and want to find them from the main secrets listing.

## Development and Production values
A secret should always have a development value. This also acts as the production value if nothing is provided in the **Production value** field.

Ziggy will select the appropriate value at runtime. See [Dev/Prod mode](/user-guide/Dev-Prod-Modes) for information on switching modes.

## Where do I reference secrets from?
There are two places where you reference a secret.

### Connections
When defining a [Connection](Connections), you can specify a secret. 

<img src="/img/secrets/secret-connection-reference.png" alt="Connections" width="400" />

### Javascript Block
You can reference a connection in a [Javascript Block](user-guide/block-types/core/Javascript.md) like this.

```JavaScript
const apiKey = secrets.NORTHWIND_DB_PASSWORD
```
