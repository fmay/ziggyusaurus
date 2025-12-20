---
title: Authorization
---

`ziggy auth [options] [commands]`

## Authorize for a server
You can authorize against as many servers as you like. Typically, you will have a development instance and a production instance, each of which needs to be authenticated against.

Just enter `ziggy auth` to start the authorization process. 

You will be asked whether you are authenticating for a server or plugin. Enter `s` or `p`. 

- If a plugin, all CLI operations, including the authorization, need to be run from the root plugin folder.
- If a server, you can use the CLI from any folder.

You will then be asked to provide details for

- Friendly name - you will use this name later with --server options. Alphanumeric only and it should not start with a number.
- Ziggy server url - either localhost or the full protocol and domain name of the server like `http://localhost` or `https://prod.ziggy.mycom.com`. Do not include the port.
- Port : usually `3000` for localhost and `443` for a remote instance.
- User Name
- Password

Once authenticated, the server configuration will be stored on your local machine and can be referenced by the friendly name.

## List authenticated servers

`ziggy aith -l` or `ziggy auth --list`

Lists authenticated servers and plugins.


## Set default server

To avoid having to use the `-s` or `--server` options in other commands, you can set the default server with

`ziggy auth use friendlyName`

## Removing a server configuration
To remove a locally stored server configuration use

`ziggy auth remove -s friedlyName`


## Plugin commands

Authorization for plugins is handled when you run `ziggy plugin create`. However, this might fail, in which case you can authorize later.

## Other commands
You will need to authorize when running management commands.