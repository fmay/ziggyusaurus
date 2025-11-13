---
title: Overview
---

Ziggy lets TypeScript developers build their own Custom Blocks using a plugin system. This is supported by the Ziggy CLI, which streamlines the scaffolding, plugin and block registration process.

## Plugin
A plugin is a project that contains a collection of one or more Custom Blocks.

This plugin is then registered with your Ziggy instance using the CLI or the Ziggy UI. From this point on, your Custom Blocks are available along with the default Ziggy Blocks.

The CLI scaffolded plugin project comes with the following.

- TypeScript source code for your Custom Blocks
- ES Lint 
- Prettier
- `package.json` containing dev and build scripts.

## Custom Block
Your plugin can contain as many Custom Blocks as you require. Each Custom Block comprises the following source files.

- `my-block.v1.block.tsx` - the React component that renders the Custom Block in the Ziggy Flow
- `my-block.v1.config.ts` - the properties and block definition for the React Custom Block component.
- `my-block.v1.definition.ts` - metadata for both the client and server.
- `my-block.v1.server.ts` - the server code that executes when the Flow is running. 

## CLI
The CLI is very helpful for building plugins. It will help you with all important aspects of plugin abd block creation. It also registers the plugin with your Ziggy instance.

