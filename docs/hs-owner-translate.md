---
title: Hubspot Owner Translate
---

# Hubspot Owner Translate

This block is used in any integration or migration where the source data has an email 
that you need to translate to an Owner ID before writing to Hubspot.

![Hubspot owner translate](hubspot-owner-translate.png#width=600)

## Email key on input edge
We have specified the key where we expect to find the email address to lookup - `salesPersonEmail`.

## Output key
This is the field to add to the input data that should contain the Owner Id. In most cases, this will be `hs_owner_id`.

## Output edge
This output edge will contain the data on the incoming edge with the `hs_owner_id` added as a new key, if it was found in the lookup.
