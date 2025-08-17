---
title: Branch Block
---

# Branch

With the Branch Block allows you can evaluate data on the incoming edge and branch to different Blocks accordingly.

<img src="/img/flows/blocks/core/block-branch.png" alt="Branch" width="900" />

You can add more conditions by pressing the **+** button and remove them with the **Trash** icon.

The syntax is anything you would write inside a normal ```if(...)``` statement.

## Alternatives
If you have more complex branching requirements, you can use the Javascript Block and use the ```branchTo(edgeIndexZeroBased, data)``` method as follows.

<img src="/img/flows/blocks/core/javscript/js-branch-to.png" alt="Brnach to" width="800" />
