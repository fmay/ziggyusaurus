---
title: Client
---

The file `my-block.v1.block.tsx` is the React component that renders in the Ziggy flow editor. 

You are free to use whatever UI components you like, but the Plugin SDK provides the following standard components that are in keeping with Ziggy's own components.

Each of these components has various properties that you can explore.

- `CheckboxWithLabel` - a checkbox with an associated label.
- `InputSimple.tsx` - a simple input field.
- `LabelInputPairHorizontal.tsx` - an input field with the label on the same line.
- `LabelInputPairVertical.tsx` - an input field with the label above the input.
- `PopupHelp.tsx` - used for standalone labels. You can optionally supply simple associated help `.md` file in a popup.
- `SelectItems.tsx` - a dropdown component for single and multi-select. Can also create values not yet in the list.

## Tailwind
Ziggy uses Tailwind for styling, which you can take advantage of.

## Building
In order for the Ziggy server to pick up on changes in your React code, your plugin needs to be rebuilt. You should use one of the `package.json` scripts. With `dev`, it will build on any changes. 

The Ziggy server will pick up on changes in real-time. If you do not see changes in the Ziggy UI, then reload the browser.

If you have added new blocks, then you should run `ziggy plugin register`.

## The code
Here's a very simple Custom Block as created by the CLI. 

```javascript
export const MyBlockBlockComponentV1: React.FC<BlockComponentProps> = ({ block, nodeId, flowApi }) => {
  const [config, setConfig] = useState<MyBlockBlockV1Config>(block.config)

  const save = (newConfig: MyBlockBlockV1Config) => {
    const blockCopy = deepCopy(block)
    blockCopy.config = newConfig
    setConfig(newConfig)
    flowApi.updateBlock(nodeId, blockCopy)
  }

  return (
    <div className="p-4">
      <div>
        <LabelInputPairHorizontal
          label="Name"
          value={config.name}
          onChange={txt => save({ ...config, name: txt })}
        />
      </div>

      {/* Add more configuration fields here */}
    </div>
  )
}
```

This is hopefully self-explanatory but the following things are worth pointing out.

- The `save()` method uses `flowApi.updateBlock(nodeId, blockCopy)` to persist any block changes to the flow. 
- The properties defined in `my-block.v1.config.ts` are available in the `config` property.

