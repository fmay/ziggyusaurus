---
title: Salesforce Owner Translate
description: Translate and map Salesforce record owners using Ziggy's Owner Translate block. Complete guide for user mapping and data migration flows.
keywords: [ziggy, salesforce owner translate, user mapping, record owners, data migration, salesforce users]
image: /img/ziggy-logo-light.webp
---

# SalesForce Owner Translate

This block is used in any integration or migration where the source data has an email
that you need to translate to an Owner ID before writing to SalesForce.

<img src="/img/flows/blocks/salesforce/sf-owner-translate.png" alt="SalesForce owner translate" width="900" />

## Email key on input edge
We have specified the key where we expect to find the email address to lookup - `email`.

## Output key
This is the field to add to the input data that should contain the Owner Id. We have specified `OwnerId`.

## Output edge
This output edge will contain the data on the incoming edge with the `OwnerId` added as a new key, if it was found in the lookup.

<img src="/img/flows/blocks/salesforce/sf-owner-translate-data.png" alt="SalesForce owner translate" width="400" />
