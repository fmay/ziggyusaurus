---
title: Adding your own custom Blocks
---


Custom Utility Blocks are very helpful for encapsulating and simplifying commonly used Javascript code. This allows you to modularise the nuts and bolts of an integration and present access to it through a friendly front-end.

The following information is not intended as a detailed guide. It's purpose is to provide a thorough overview of the the process. We are able to supply a more detailed guide upon request.

## How long does it take to add a Custom Block
Assuming you have already written the core code that drives your Block in a Javascript Block, or in another prototyping area, it takes about one to two hours each for the front end and back end. 
Of course, the final figure depends very much on the complexity of what you are trying to achieve.

## Client Side
The first thing you'll do is to write the client side React code along with a definitions file.

Expand this section to see example code.

## Adding your Custom Block to a Flow
Once the client side functionality has been added, you can add, test and modify your Block by pressing the Add Block icon in the Flow toolbar. It will then appear in the dialog.

<img src="/img/customisation/customisation-add-block.png" alt="add block" width="500" />

The section it ids displayed is in controlled by the ``` group: BlockGroupEnum.Custom``` in the ```customBlockName.block.v1.ts``` file.

```JavaScript
export enum BlockGroupEnum {
  Core = 'Core',
  Utility = 'Utility',
  Custom = 'Custom',
}
```

## Server Side
The server side is also quite easy to create. Again, you have all the other Ziggy Blocks to refer to.

## Support framework
Ziggy provides all of the support framework you need for slotting your Block into any Flow.

- **Batching** - if your Block should support [Batching](/user-guide/Batching) then a few utility methods are available for you to use. Referring to other Utility Blocks such as SQL, SFTP or REST give you plenty of example of how these work.
- **Logging** - most logging happens by default but custom logging can also be handled.
- **Edge Data** - all input edge data management is handled for you and standard utility methods make this very easy to work with.
- **Connections** and **modules** - you can create custom [Connection](/user-guide/Connections) types and use external modules (typically NPM) and use these in your Block code.
- **Internal API** - you have access to all of the system objects such as Secrets, Variables, Connections.




