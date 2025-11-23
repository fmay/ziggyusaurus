---
title: HubSpot Currency
---

This block lets you both get and set currencies.

## Get
This retrieves all current HubSpot currencies and the current exchange rates. The data is placed on the output edge.

<img src="/img/flows/blocks/hubspot/hs-currency-get.png" alt="Markdown" width="300" />

You will see data like this on the edge.

<img src="/img/flows/blocks/hubspot/hs-currency-get-data.png" alt="Markdown" width="300" />

## Set
This sets exchange rates for your defined HubSpot currencies.

<img src="/img/flows/blocks/hubspot/hs-currency-set.png" alt="Markdown" width="300" />

### Data Key
If the currency data on the input edge contains the data array with your currency data then leave this empty. If not, point to the key in the input data.

### Currency code key
This is a required field. You should specify which key in each array element contains the currency code.

### Exchange rate key
This is a required field. You should specify which key in each array element contains the exchange rate.

### Example
The flow below shows 

- a REST block, which fetches data from a currency server. 
- The Javascript block gets the data into an array (see below).
- The HubSpot Currency block then updates HubSpot.

<img src="/img/flows/blocks/hubspot/hs-currency-set-input.png" alt="Markdown" width="1000" />

