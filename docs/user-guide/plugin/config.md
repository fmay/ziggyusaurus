---
title: Configuration
---

The first thing you should do is to configure the block properties in `my-block.v1.config.ts`.

```javascript
export interface MyBlockBlockV1Config {
  name: string
  // Add your config properties here
}
```

This interface defines the properties that your block needs. These are fields that will appear or be used in the block itself. This interface is available to both the client and server components.

```javascript
export const MyBlockV1Name = 'MY_BLOCK_V1'
```

Create a name for your block. This must be unique and must also not conflict with Ziggy's internal Blocks.

You can use `_V1` as a simple versioning mechanism should you want to add more functionality later without breaking any existing blocks. If you update a block once in production, you should be aware of potentially introducing breaking changes. 

```javascript
export const DefaultMyBlockBlockV1: IFlowBlock = {
  id: '',
  type: MyBlockV1Name,
  width: 280,
  height: 140,
  position: { x: 0, y: 0 },
  data: {
    type: MyBlockV1Name,
    name: 'my-block',
    version: 1,
    isValid: true,
    group: BlockGroupEnum.Custom,
    styleType: StyleTypeEnum.standard,
    numInputs: 1,
    numOutputs: 1,
    hasInternalOutputHandles: false,
    hasInternalInputHandles: false,
    headerColor: '#3b82f6',
    config: {
      name: 'my-block',
    } as MyBlockBlockV1Config,
  },
}
```

The only things you would normally change are

- `headerColor` - the color of the top block bar.
- `config` : these are the default values that should match your config's interface definition.


