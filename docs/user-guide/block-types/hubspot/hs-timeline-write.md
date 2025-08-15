---
title: HubSpot Timeline
---

# HubSpot Timeline

This Block is used to write data to the HubSpot timeline.

**Important** : in order to support all HubSpot plans, this requires authentication with oAuth and a Public App, rather
than the usual Private App. This is explained below.

<img src="/img/flows/blocks/hubspot/hubspot-timeline-write.png" alt="Hubspot timeline" width="400" />

- You should choose a [Connection](/user-guide/Connections). You will be presented with configured HubSpot Connections.
- Once the Connection is selected, you choose an Event Template. You cannot define these yourself 
due to the constraint of HubSpot Public Apps. You will need to contact Ziggy to configure a special Public App with 
the events you require.
- Ziggy detects all tokens available in the Timeline Event. You can choose the ones you want to use and 
associate these with data on the incoming edge.
- You can also use HubSpot's `extraData` feature, in which case you point **Extra Data edge key**  to the 
input key containing the data you wish to pass to `extraData`.

## oAuth Authentication
Because Timeline Events can only be written to using a Public App, authentication has to be handled by oAuth.

Certain Connection types, including HubSpot, have an oAuth button in the Connection Manager. 
This lets you login from the Ziggy UI.

- Open the Hubspot connection in the Connection Manager. 
- You can then press the oAuth button to authenticate.
- Note that you should press the oAuth button for Development and Production modes, if they are different.
- Note that this will not work until you have an `appId`, which we will need to supply. Please read the
**Public App* section below.

Ziggy stores the oAuth tokens and will automatically refresh tokens as long as the refresh token itself has not expired, 
in which case you will need to use the oAuth button to fetch new tokens.

Each the Timeline Write block runs, it will refresh tokens. However, if you never run the block, the tokens will 
eventually expire and you will need to reauthenticate through the UI.

## Public App
Because Public Apps are generic in nature, it is necessary for us to create a special Public App that is 
dedicated to you. This can contains as many Event Templates as you require.

Please contact info@ziggyservices.com to request this. We will then provide an **appId** to you, which you can 
enter in your Connection config as shown below.

```JavaScript
{
  accessToken: secrets.HUBSPOT_API_KEY,
  developerApiKey: secrets.HUBSPOT_DEVELOPER_API_KEY,
  numberOfApiCallRetries: 5,
  appId: 12345678
}
```
