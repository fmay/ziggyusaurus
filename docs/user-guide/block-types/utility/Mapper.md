---
title: Mapper
---

# Mapper
Maps value on the input edge from one value to another. Data can be read from the Google Sheet workbook/worksheet combination you enter.

![Mapper](/img/flows/blocks/utility/mapper/block-mapper.png){width=300}

## Google Sheet
Mapping data is loaded from the Google Sheet URL. You should create a sheet as explained below..

**About this mapping**

**Add anything else on any number of rows**

**At some point, it expects to find 'If' and 'Then' in the first two columns, followed by the mapping data**

**If** | **Then**
-------|--------
Mr. | 1
Mrs. | 2
Ms. | 3
Dr. | 4
`[$='Dame' OR $='Sir']` | 9
`$='Dame' OR $='Sir'` | 9
#Otherwise# | 99

You can also copy **[this sheet](https://docs.google.com/spreadsheets/d/1XpcmSuiKKP2yE135rUCmuTqLDZ7mGBGdkAVk2qIrAnQ/edit?gid=0#gid=0)** and format it to your liking.

## Expressions
You can enter an expression in the **If** cell. These are Javascript like expressions with some tolerance for ```=``` and ```||, OR, or```.

```javascript
{$='Dame' OR $='Sir'}
$='Dame' OR $='Sir'
```

You need to conform to the following **If** pattern.

- The ```$``` sign represents the incoming data.
- If you think your data might contain the ```$``` character then you should enclose it in ``` {...}```.
- You can write ```||``` or ```OR``` or ```or```. The same applies to ```AND```. This makes it less onerous for non-technical people to write.
- ```#Otherwise``` (case insensitive) is the ```else``` of the conditions list.

## Loading the data
Whenever you make changes to your sheet, you should load them into the Block by pressing the **Load from sheet** button.

## Viewing the mappings
Press the **Show** button to see the mappings that are currently loaded.
Editing must still be done in the Google Sheet but this lets you double check that the correct mappings are loaded.

## Input key
This refers to the data key in the input edge. The ```$``` symbol in an expression refers to data found on this key.

```javascript
age
address.city
```