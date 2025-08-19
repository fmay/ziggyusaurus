---
title: Slack App configuration
---

A Slack App interacts with Ziggy by executing Flows. These Flows perform queries and return data in a format that Sack can render.

## Slack response formatting
Refer to the [Slack Block Formatter](/user-guide/block-types/slack/slack-formatter) for how to format your Slack response.

## Slack App setup

### Developer Account
You should first create a [Slack developer account](https://api.slack.com/developer-program). This is free.

### Create an App
When doing this for the first time, go to your [Dashboard](https://api.slack.com/developer-program/dashboard) then press **Start building** for the docs page.

To create an App right away, [create an App](https://api.slack.com/apps).

### App configuration
There are two ways to configure an App. 

- Use the *App Manifest* (shown below)
- Use the individual menu items in the left sidebar.

You can use both approaches. When you update individual settings using the sidebar, the manifest is updated.

### Manifest
The manifest is a JSON document that describes the entire App. Feel free to use this as a starting point. It contains the necessary scopes and some slash commands.

```JSON
{
    "display_information": {
        "name": "Ziggy",
        "description": "Ziggy Hubspot NLQ",
        "background_color": "#7a7a7a"
    },
    "features": {
        "app_home": {
            "home_tab_enabled": true,
            "messages_tab_enabled": false,
            "messages_tab_read_only_enabled": false
        },
        "bot_user": {
            "display_name": "Ziggy",
            "always_online": false
        },
        "shortcuts": [
            {
                "name": "HS List",
                "type": "global",
                "callback_id": "hs_search",
                "description": "Perform a HubSpot Search"
            }
        ],
        "slash_commands": [
            {
                "command": "/zma",
                "url": "https://your-ziggy-domain/api/slack/events?executeFlow&flowUuid=f4b86248-69c3-458a-a381-7c94cb2124a7&executionKey=ziggy.ek-YqdAKUB/yy4ZUtU_ilKIcTvAVJv7t2&executionEnvironmentMode=DEV",
                "description": "Show the 5 most recent tasks and meetings",
                "should_escape": false
            },
            {
                "command": "/find",
                "url": "https://your-ziggy-domain/api/slack/events?executeFlow&flowUuid=fe73bef8-6ac2-4bc2-ba84-0ef1cf6d5c16&executionKey=ziggy.ek-YqdAKUB/yy4ZUtU_ilKIcTvAVJv7t2&executionEnvironmentMode=DEV",
                "description": "Get latest Tasks and Meetings",
                "should_escape": false
            },
            {
                "command": "/zsdb",
                "url": "https://your-ziggy-domain/api/slack/events?link=https://app-eu1.hubspot.com/reports-dashboard/144231748/view/109772092&linkText=Sales%20Dashboard",
                "description": "Show the sales dashboard",
                "should_escape": false
            },
            {
                "command": "/zspecial",
                "url": "https://your-ziggy-domain/api/slack/events?link=https://app-eu1.hubspot.com/contacts/144231748/objectLists/161/filters&linkText=Special%20Companies",
                "description": "Show \"Special Companies\" list",
                "should_escape": false
            },
            {
                "command": "/zlink",
                "url": "https://your-ziggy-domain/api/slack/events?shortcut",
                "description": "Add a custom, personal shortcut link",
                "usage_hint": "[url link name]",
                "should_escape": false
            },
            {
                "command": "/zsearch",
                "url": "https://your-ziggy-domain/api/slack/events?search",
                "description": "Save a search query to the Home page",
                "usage_hint": "[query]",
                "should_escape": false
            },
            {
                "command": "/clear",
                "url": "https://your-ziggy-domain/api/slack/events?cleardm",
                "description": "Clears messages in your private DM channel",
                "should_escape": false
            }
        ]
    },
    "oauth_config": {
        "redirect_urls": [
            "https://your-ziggy-domain/api/slack/oauth/callback"
        ],
        "scopes": {
            "bot": [
                "app_mentions:read",
                "channels:read",
                "chat:write",
                "chat:write.public",
                "commands",
                "groups:read",
                "im:write",
                "mpim:read",
                "team:read",
                "users:read",
                "users:read.email",
                "im:history"
            ]
        }
    },
    "settings": {
        "event_subscriptions": {
            "request_url": "https://your-ziggy-domain/api/slack/events",
            "bot_events": [
                "app_home_opened"
            ]
        },
        "interactivity": {
            "is_enabled": true,
            "request_url": "https://your-ziggy-domain/api/slack/events"
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": false
    }
}

```
### Slash Commands
You can see these in the manifest.

```JSON
    {
        "command": "/find",
        "url": "https://your-ziggy-domain/api/slack/events?executeFlow&flowUuid=fe73bef8-6ac2-4bc2-ba84-0ef1cf6d5c16&executionKey=ziggy.ek-YqdAKUB/yy4ZUtU_ilKIcTvAVJv7t2&executionEnvironmentMode=DEV",
        "description": "Get latest Tasks and Meetings",
        "should_escape": false
    }
```

You should configure the query parameters.

- **executeFlow** - always include this
- **flowUuid** - the Flow UUID to invoke. This can be found by clicking the Flow name in the Ziggy Flow Editor.
- **executionKey** - the execution key to use. This is explained [here](user-guide/Launching-flows.md).
- **executionEnvironmentMode** - `DEV` or `PROD`. This is relevant when you are using different Connections and Secrets for development or production.

### Scopes
The above manifest includes scopes that should be ok for regular Ziggy usage. However, you may require additional scopes. These can be added in the **OAuth & permissions** section of your Slack App configuration.

