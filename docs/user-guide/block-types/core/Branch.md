---
title: Branch Block
---

# Branch

With the Branch Block allows you can evaluate data on the incoming edge and branch to different Blocks accordingly.

![Branch](block-branch.png){width="900"}

You can add more conditions by pressing the **+** button and remove them with the **Trash** icon.

The syntax is anything you would write inside a normal ```if(...)``` statement.

## Alternatives
If you have more complex branching requirements, you can use the Javascript Block and use the ```branchTo(edgeIndexZeroBased, data)``` method as follows.

![Brnach to](js-branch-to.png){width="800"}
