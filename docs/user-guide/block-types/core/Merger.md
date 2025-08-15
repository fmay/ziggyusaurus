---
title: Merger
---

# Merger
Takes array data from multiple inputs and merges them into a single array. It is assumed that each of the input arrays are of the same size.

![Merger](block-merger.png#width=900)

If the first input, ```northwind``` and the second ```hubspot```, both of which contain 100 elements, then there will be a single output edge array of 100 elements. Each element will look like this.

```javascript
    {
        northwind: contents of input0's nth element
        hubspot: contents if input1's nth element
    },
    ...
```

## Use case
A common use case is

- Your incoming data contains data that you want to map to another structure, but you also want to keep the original data. 
- You create two output from the prior Block (as shown). 
- The first one contains the original data.  
- You perform a data mapping on the second one.
- The **Merger Block** then ensures was have new edge data with both sets of data in each array element.