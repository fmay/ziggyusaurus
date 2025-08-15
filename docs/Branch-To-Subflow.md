---
title: Branch to Subflow
---

# Branch to Subflow

Branches to a subflow based on the input edge element. This expects an array with only a **single element**.

![Branch subflow](block-branch-subflow.png#width=800)

A common combination is using the [Iterator Block](Iterator.md) to
take an edge with multiple rows on it and split it up into single elements.

For each entry you add to the branch, you specify an expression that evaluates the incoming data.

For example. if your incoming edge data looks like this

```javascript
[
  {
    objectId: 86906762466,
    propertyName: "name",
    attemptNumber: 0,
    propertyValue: "Maison Deweys",
    subscriptionId: 3153733,
    subscriptionType: "company.propertyChange"
  }
]
```

You can use the following **conditional expression** to decide which Flow to branch to.

```javascript
subscriptionId === 3153733
``` 

## Else
An entry without an expression will be assumed to be the **else** condition.

If there is no **else** condition then the Flow will error if none of the prior conditions evaluate to true.
