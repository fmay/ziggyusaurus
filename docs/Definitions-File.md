---
title: Definitions File
---

# Definitions File

This example is the HubSpot Write block. It consists of the following section.

- **Help** - we've created a markdown constant that is then added to the main definition's ```ThisBlock.help``` field.
- **Interface** - we define a Typescript interface that will store the necessary Block properties along with the default values.
- **Block Definition**

```javascript
import { v4 } from 'uuid'
import {
  BlockGroupEnum,
  StyleTypeEnum,
  IFlowBlock,
  IFlowBlockData,
} from '@/lib/api/Api.ts'
import { SiHubspot } from 'react-icons/si'
import { BlockDefinitionProps } from '@/blocks/blocks.manifest.ts'
import IFlowNodeBase from '@/blocks/IFlowNodeBase.tsx'
import HSCollectionWriteV1 from '@/blocks/collections/hubspot-collection/HSWrite/HSCollectionWrite.v1.tsx'

const markdown = `
Writes data to the specified HubSpot object. 

# Connection (required)
Choose a Connection that you have defined in Connections. This will contain your HubSpot API key.

# HS Object Name (required)
The Hubspot object to update. If it is a custom object, check the provided box.

# Operation type
## Upsert
You can choose to **Upsert** (recommended) or not. If you don't upsert, data will be written only if it doesn't exist. Existing records will be left untouched.

## Perform data property validation
This scans the incoming edge data and checks it against the available properties for the specified Hubspot object. You using the 

## Invalid to second output edge
If you have selected **Perform data property validation** then this option places the input edge data items that failed the validation 
  onto the second output edge. 
  
This lets you deal with errored data as you see fit. You might, for example, write it to the data store so you can inspect it later.

If you don't select this option, data that failed the validation will be discarded.

## Edge data
The upsert operation is performed on the following basis.

- The edge is assumed to have data that is in the right format for Hubspot to receive. 
- The edge data should contain data (whether array or not) that is a collection of key/value pairs with no extra data. Use data mapping to prepare a clean structure
- Hubspot will throw an error if data contains a property key where the property does not exist. You should there use the above mentioned validation to avoid this.

## HS property to match against (upsert only)
This indicates which Hubspot property should be used as the basis for the upsert lookup.
 
`

export interface BlockConfig_HSCollectionWriteV1 {
  shouldUpsert: boolean
  shouldValidate: boolean
  useFailedValidationEdge: boolean
  connectionUuid: string
  useErrorEdge: boolean
  objectName: string
  isCustomObject: boolean
  uniqueIdPropertyName: string
}

const DefaultHubspot: BlockConfig_HSCollectionWriteV1 = {
  shouldUpsert: true,
  shouldValidate: true,
  useFailedValidationEdge: true,
  connectionUuid: '',
  useErrorEdge: false,
  objectName: '',
  isCustomObject: false,
  uniqueIdPropertyName: '',
}

type ThisBlock = IFlowBlock & {
  data: IFlowBlockData & { config: BlockConfig_HSCollectionWriteV1 }
}
const NAME = 'HS_COLLECTION_WRITE_V1'

export const BlockHSCollectionWrite_V1: ThisBlock = {
  type: NAME,
  id: v4(),
  width: 100,
  height: 100,
  position: {
    x: 0,
    y: 200,
  },
  selected: false,
  data: {
    type: NAME,
    version: 1,
    isValid: true,
    name: 'Hubspot Write',
    info: 'Writes a record or batch of records to a Hubspot object',
    help: markdown,
    hasInternalOutputHandles: false,
    hasInternalInputHandles: false,
    icon: SiHubspot,
    group: BlockGroupEnum.Collection,
    styleType: StyleTypeEnum.STANDARD,
    numInputs: 1,
    numOutputs: 2,
    config: DefaultHubspot,
  },
}

export const HSCollectionWriteV1Block: BlockDefinitionProps = {
  block: BlockHSCollectionWrite_V1,
  component: HSCollectionWriteV1,
  baseNodeType: IFlowNodeBase,
}

```