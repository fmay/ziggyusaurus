---
title: Block Helper
---

# Block Helper

This is the core functionality for the HubSpot Write Block.

Note how this is using the same interface we defined in the [client definition](/customisation/custom-utility-blocks/client/Definitions-File).

```JavaScript
export const hsCollectionWriteV1Helper = async (
  client: Client,
  config: BlockConfig_HSCollectionWriteV1,
  data: Record<string, any>[],
): Promise<
  BatchResponseSimplePublicUpsertObjectWithErrors | BatchResponseSimplePublicUpsertObject
> => {
  // Map to required HS object format
  const finalData: SimplePublicObjectBatchInputUpsert[] = data.map(inputRow => {
    return {
      idProperty: config.uniqueIdPropertyName || '',
      id: inputRow[config.uniqueIdPropertyName],
      properties: inputRow,
    }
  })
  const batch: BatchInputSimplePublicObjectBatchInputUpsert = {
    inputs: finalData,
  }

  // Upsert to HubSpot
  const result = await client.crm.objects.batchApi.upsert(config.objectName, batch)

  // Add the HubSpot object id to the returned data
  for (const r of result.results) {
    const inputData = data.find(
      d =>
        d[config.uniqueIdPropertyName].toString() ===
        r.properties[config.uniqueIdPropertyName].toString(),
    )
    if (inputData) inputData['hs_object_id'] = r.id
  }
  return result
}
```