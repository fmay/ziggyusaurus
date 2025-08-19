---
title: Branch Block
description: Learn how to use the Branch block in Ziggy flows for conditional logic and decision making. Complete guide with examples and configuration options.
keywords: [ziggy, branch, core blocks, flows, no-code, conditional logic, decision making]
image: /img/ziggy-logo-light.webp
---

# Branch

With the Branch Block allows you can evaluate data on the incoming edge and branch to different Blocks accordingly.

<img src="/img/flows/blocks/core/block-branch.png" alt="Branch" width="900" />

You can add more conditions by pressing the **+** button and remove them with the **Trash** icon.

The syntax is anything you would write inside a normal ```if(...)``` statement.

## Alternatives
If you have more complex branching requirements, you can use the Javascript Block and use the ```branchTo(edgeIndexZeroBased, data)``` method as follows.

<img src="/img/flows/blocks/core/javscript/js-branch-to.png" alt="Brnach to" width="800" />
