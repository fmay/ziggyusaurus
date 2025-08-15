---
title: Block Handler
---

# Block Handler

This looks complex, but it's actually rather simple. You will typically copy code from another Block that comes close to meeting your requirements.

You will need to adjust very little. Note that most of the Blocks we have coded extract the code the core functionality into a helper file, which you can [see here](/customisation/custom-utility-blocks/Block-Helper). 

```JavaScript
export const HSCollectionWriteV1 = async (props: BlockExecutionProps) => {
  const { blockToExecute: block, clogging } = props

  const config: BlockConfig_HSCollectionWriteV1 = props.blockToExecute.data.config

  // ID of this block
  const thisBlock = block

  try {
    // Timer start for execution time recording
    const startTime = new Date()

    // Get the incoming edge data
    let inputData = await waitForInputEdgeData(props, block.id, 'i0')

    // Get connection
    const { connectionUuid } = block.data.config as BlockConfig_HSCollectionWriteV1
    const client: Client =
      props.environmentMode === ExecutionEnvironmentModeEnum.DEV
        ? props.marshallerSvc.connectionSvc.devConnectionsById[connectionUuid]
        : props.marshallerSvc.connectionSvc.prodConnectionsById[connectionUuid]

    // Perform a Hubspot validation against enumeration values, dates etc.
    const { goodData, badData } = await validateHsInputDataHelperV1(
      props,
      client,
      config,
      inputData.payload,
    )
    inputData.payload = goodData

    // EXECUTE UPSERT
    await hsCollectionWriteV1Helper(client, block.data.config, inputData.payload)

    // Put data on edge(s) and return
    let outEdges
    outEdges = outgoingEdgeAssignment(props, thisBlock.id, 0, goodData)

    // Failed validation edge
    if (config.useFailedValidationEdge && badData.length > 0)
      outEdges = outgoingEdgeAssignment(props, thisBlock.id, 1, badData)

    // Record time taken
    block.data.executionTime = new Date().getTime() - startTime.getTime()
    props.logTime(block, inputData, outEdges, block.data.executionTime)

  } catch (error) {
    if (config.useErrorEdge) {
      outgoingEdgeAssignment(props, thisBlock.id, 0, {})
      outgoingEdgeAssignment(props, thisBlock.id, 1, { error: error.stack })
    } else {
      props.errorObject.isFatalError = true
      props.errorObject.block = block
      props.errorObject.msg = `${error.stack}`
    }
  }
}```