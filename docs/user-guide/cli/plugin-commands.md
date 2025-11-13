---
title: Plugin commands
---

The following commands support plugin scaffolding, block management and snychronization with your Ziggy instance.

**Important** : You should be in the root folder of your plugin project to run these commands.

If you accidentally unregister, remove or rename a block so that Flows no longer function that are affected, you can recover by adding back the block as it was beforehand.

## Authorization

`ziggy auth`

Authorization for plugins is handled when you run `ziggy plugin create`. However, this might fail, in which case you can authorize later. 

## Create a plugin project

`ziggy plugin create`

Creates a new plugin project scaffold with a simple block as a subdirectory relative to your current working directory.

## Add a block

`ziggy plugin block add`

**Important** : you must choose a block name that is unique across all plugins and standard Ziggy blocks. This check is performed for you.

You are asked details about the block you want to create. If you are creating a block that initiates [Batching](/user-guide/Batching.md) then answer that question with `Y'. This will insert the relevant helper functions.

Be sure to run `ziggy plugin build` then `ziggy plugin register` once ready to publish to the Ziggy instance.

See also [Client handler code](../plugin/client.md),  [Server handler code](../plugin/server.md) and [Batching server handler](../plugin/batcher.md).

## Remove a block

`ziggy plugin block remove`

Removes a block from a plugin. You should be aware that once you build and register the plugin, any Flows that contain the block you have removed will no longer function.

## Rename a block

`ziggy plugin block rename`

Renames a block and all its component parts, including the block name. If you want existing blocks in Flows to continue to function, you should change the name in the `.config.ts` file back to ots original name after everything else has been renamed.

## Build the plugin

`ziggy plugin build`

This will build the client and server components of the block. The `package.json` scripts contain various build scripts that may be relevant for development and production.

Building will be reflected in a running Ziggy instance for any blocks that are already registered. If you add or remove a block, you should register the changes with `ziggy plugin register`.

## List plugins and blocks

`ziggy plugin list`

Lists each registered plugin and its blocks.

## Register plugin

`ziggy plugin register`

Registers a plugin with the Ziggy istance. If the plugin is already registered then changes (added or removed) will be registered.

## Unregister plugin

`ziggy plugin unregister`

Removes a plugin and all associated blocks from the Zigy instance.