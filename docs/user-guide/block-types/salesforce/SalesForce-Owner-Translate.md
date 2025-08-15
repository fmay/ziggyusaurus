---
title: SalesForce Owner Translate
---

# SalesForce Owner Translate

This block is used in any integration or migration where the source data has an email
that you need to translate to an Owner ID before writing to SalesForce.

![SalesForce owner translate](sf-owner-translate.png#width=900)

## Email key on input edge
We have specified the key where we expect to find the email address to lookup - `email`.

## Output key
This is the field to add to the input data that should contain the Owner Id. We have specified `OwnerId`.

## Output edge
This output edge will contain the data on the incoming edge with the `OwnerId` added as a new key, if it was found in the lookup.

![SalesForce owner translate](sf-owner-translate-data.png#width=400)
