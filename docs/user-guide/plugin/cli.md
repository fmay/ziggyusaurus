---
title: CLI
---

You should use the CLI to help you scaffold a plugin, manage blocks and register/sync with the Ziggy instance.

## Current working directory
You must be in the root of a plugin project to run the Ziggy CLI `ziggy plugin` commands. 

## Authentication
When you create a new plugin (see below) you will be asked to authenticate. If this fails or you do not do this, then you can explicitly authenticate using `ziggy auth`.

Once authenticated, the details are remembered.

## Create a plugin
The first command you run is

```shell
ziggy plugin create
```

This creates a project scaffold for you and adds a very simple block. This will also ask you to authenticate.

## Adding Blocks
The easiest way to add blocks is using the following command.

```shell
ziggy plugin block add
```

This will ask you relevant questions and then add the code. Note that you will need to build and then register the plugin.

## Building
The `package.json` contains scripts for building and watching when developing. The server should pick up on client and server block components as soon as they are built.

**IMPORTANT** : if you add a new block, you need to build and then **register**.

You can also use `ziggy plugin build` to build your plugin.

## Registering
Registering is responsible for keeping your plugin synchronized with the Ziggy instance. 

You should run `ziggy plugin register` whenever you add or remove a block.

## Other CLI commands
The following CLI commands are also available.

- `ziggy plugin block add`
- `ziggy plugin block remove`
- `ziggy plugin block rename`
- `ziggy plugin list`
- `ziggy plugin unregister` 