---
title: Create Plugin
---

Use the CLI to create a new plugin project.

You should first navigate to a folder from which the plugin project will be created as a subfolder.

`ziggy plugin create`

You will be prompted to enter information before the project is created.

<img src="/img/plugins/plugin-create.png" alt="create command" width="700" />

This creates a plugin with one very simple Custom Block - `Reader`. 

## Authentication
You will be asked to authenticate your new plugin once everything is installed. If this fails or you want to do it later, you should use `ziggy auth`.

**Important** : when using plugin commands with the CLI, you must be in the root of the plugin folder. This includes authentication.

The authentication information is stored for each plugin. Once authenticated, you will not need to re-authenticate unless your login credentials have changed.

## The Plugin Project

Below is a screenshot of your freshly scaffolded project.

<img src="/img/plugins/plugin-files.png" alt="project files" width="500" />




