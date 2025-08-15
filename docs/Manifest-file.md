---
title: Manifest file
---

# Manifest file

You register your new component in a manifest file. The Hubspot Write Block is a part of a collection of blocks, so we add it to ```CollectionsManifest```.

```JavaScript
export const BlocksManifest: BlockDefinitionProps[] = [
  CommanderV1Block,
  ReceiverBlock,
  TerminatorBlock,
  JavascriptBlock,
  DataStoreBlock,
  MemStoreBlock,
  EnrichStoreV1Block,
  IteratorV1Block,
  BatchEndBlock,
  SplitterBlock,
  RESTBlock,
  BranchBlock,
  CollectorBlockV1,
  MergerV1Block,
  AnnotationBlock,
  SubflowBlock,
  SQLBlock,
  SFTPBlock,
  ConverterBlock,
]

export const CollectionsManifest: CollectionDefinitionProps[] = [
  {
    blocks: [
      HSCollectionReadV1Block,
      HSCollectionWriteV1Block,
      HSCollectionOwnerV1Block,
      HSCollectionAssociationsGetV1Block,
      HsCollectionAssociationsSetV1Block,
      HsCollectionAttachmentsGetV1Block,
      HsCollectionAttachmentsSetV1Block,
    ],
    collectionName: 'Hubspot Collection',
    collectionDescription: 'HubSpot API functionality wrapper blocks',
  },
]
```