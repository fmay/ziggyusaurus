---
title: React component
---

# React component

This is the React component that will render in the canvas. There's really nothing special about this. Ziggy provides some methods for loading and saving.

- ```fetch()``` loads the Flow values for the Block.
- ```update()``` saves them.
- ```connections()``` may not be required but is in this case. It loads the Ziggy
- **Connection** items so you can render them in a drop down, for example.

```javascript
const HSCollectionWriteV1: FC<HubspotBodyV1Props> = React.memo(
  ({ nodeId, block }) => {
    const fetch = useConnectionStore.getState().fetch
    const updateBlock = useFlowStore.getState().updateBlock
    const connections = useConnectionStore(state => state.connections)

    if (!block) return <></>

    const [config, setConfig] = useState<BlockConfig_HSCollectionWriteV1>(
      block.config as BlockConfig_HSCollectionWriteV1,
    )
    const [isDirty, setIsDirty] = useState<boolean>(false)
    const [connectionOptions, setConnectionOptions] = useState<
      StandardDropdownItem[]
    >([])

    useEffect(() => {
      const init = async () => {
        await fetch()
      }
      init()
    }, [])

    useEffect(() => {
      const options: StandardDropdownItem[] = connections.map(c => {
        return {
          id: c.uuid,
          label: c.name,
        }
      })
      setConnectionOptions(options)
    }, [connections])

    useEffect(() => {
      setConfig(block.config as BlockConfig_HSCollectionWriteV1)
    }, [block])

    useEffect(() => {
      if (isDirty) {
        handleSave()
        setIsDirty(false)
      }
    }, [isDirty])

    const handleSave = async () => {
      const copy = deepCopy(block)
      copy.config = config
      updateBlock(nodeId, copy)
      setIsDirty(false)
    }

    const handleShouldUpsert = () => {
      setConfig({ ...config, shouldUpsert: !config.shouldUpsert })
      setIsDirty(true)
    }

    const handleShouldValidate = () => {
      const newShouldValidate = !config.shouldValidate
      const newConfig = { ...config, shouldValidate: newShouldValidate }
      setConfig(newConfig)
      const blockCopy = deepCopy(block)
      blockCopy.numOutputs =
        newShouldValidate && newConfig.useFailedValidationEdge ? 2 : 1
      blockCopy.config = newConfig
      updateBlock(nodeId, blockCopy)
    }

    const handleFailedValidationEdge = () => {
      const newUseFailedValidationEdge = !config.useFailedValidationEdge
      const newConfig = {
        ...config,
        useFailedValidationEdge: newUseFailedValidationEdge,
      }
      setConfig(newConfig)
      const blockCopy = deepCopy(block)
      blockCopy.numOutputs = newUseFailedValidationEdge ? 2 : 1
      blockCopy.config = newConfig
      updateBlock(nodeId, blockCopy)
    }

    const handleSetConnection = (item: StandardDropdownItem) => {
      setConfig({ ...config, connectionUuid: item.id })
      setIsDirty(true)
    }

    const getCurrentItemPair = () => {
      return connectionOptions.find(co => co.id === config.connectionUuid)
    }

    const handleUniqueIdPropertyName = (text: string) => {
      setConfig({ ...config, uniqueIdPropertyName: text })
      setIsDirty(true)
    }

    return (
      <>
        <div className="flex flex-col gap-1 min-w-[300px]">
          {/*CONNECTION */}
          <BlockParameterSection label="Connection">
            <StandardDropdownPaired
              options={connectionOptions}
              onSelect={handleSetConnection}
              item={getCurrentItemPair()}
            />
          </BlockParameterSection>

          {/*TYPE*/}
          <BlockParameterSection label="Operation type">
            <CheckboxWithLabel
              label="Upsert"
              checked={config.shouldUpsert}
              onChange={handleShouldUpsert}
            />
            <CheckboxWithLabel
              className="mt-3"
              label="Perform data property validation"
              checked={config.shouldValidate}
              onChange={handleShouldValidate}
            />
            {config.shouldValidate && (
              <CheckboxWithLabel
                className="mt-3 ml-3"
                label="Invalid to second output edge"
                checked={config.useFailedValidationEdge}
                onChange={handleFailedValidationEdge}
              />
            )}
          </BlockParameterSection>

          <div className="pt-2">
            <HSObjectName
              config={config}
              setConfig={setConfig as any}
              onDirty={() => setIsDirty(true)}
            />

            <div className="py-2"></div>

            {config.shouldUpsert && (
              <LabelInputPairVertical
                label="HS property to match against"
                value={config.uniqueIdPropertyName}
                onChange={handleUniqueIdPropertyName}
              />
            )}
          </div>
        </div>
      </>
    )
  },
)
```