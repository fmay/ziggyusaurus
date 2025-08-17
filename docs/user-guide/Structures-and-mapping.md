---
title: Structures, validation, mapping and transformations
---

# Structures, validation, mapping and transformations

## Introduction - video and tutorials
It is worth watching the video that explains this process in detail.

[//]: # (<video src="https://vimeo.com/video/1076607988" preview-src="ss-transform-mapping.png"/>)

<iframe 
  src="https://player.vimeo.com/video/1076607988" 
  width="100%" 
  height="400" 
  allow="autoplay; fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>

There is also a set of tutorials that both explain the process and provide Flows where you can build 
out validations, transformations and mappings.

- Go to the Flows listing
- Select **HubSpot** from the dropdown
- See the relevant tutorials circled below.

![Tuturials](/img/flows/structures/svtm-tutorials.png)

## Structures
Structures are used for two primary purposes.

- Validating edge data
- Mapping from one Structure to another

## Defining a Structure
Structures are managed in the **Structures** main navbar button. This shows you all available Structures.

![Structures](/img/flows/structures/svtm-structures.png)

There are two ways to add a Structure.

- In the Structures page, press the **+ Structure** button.
- Click on an edge bubble that has data and create a Structure from that data.

## Adding and editing Structures

- Click on the **+Structure** button to add a new Structure.
- or click a Structure in the Structures list to edit.

<img src="/img/flows/structures/structure-edit.png" alt="Edit" width="700" />


## The Zod validation object
This is the main part. It might look a little intimidating at first, 
but it is a very powerful way to validate data.

- You don't have to use structures in most cases, so only set them up when they help.
- It's simple to work with yet very powerful.
- We have some AI supported methods of automatically generating the object based on actual edge data. This is discussed below.

To get more details, please read the [Zod documentation](https://zod.dev/?id=primitives).

## Validation
This section will refer to the following Flow.

![validation flow](/img/flows/structures/svtm-validation-flow.png)


### Run the Flow
If you run the Flow, which reads in a batch of 10 records in a single batch iteration, 
you can see the edge has 10 records of data on it.

- Inspect the edge bubble to see the data.
- Note the 10 records and selected fields that have been read.
- Check the **Validate** box.
- Select the **Validate** tab.
- Press the **Generate from input data** button, which generates a validation object, which we'll explain in next tutorial.

![600](/img/flows/structures/tutorial-videos/A51-validate.png)

- Run the Flow again then click the edge bubble.
- You'll notice there is now a **Data out** tab. You can click on it and you'll see the same data as in the first Data tab (no validations failed).

### Force validation failure
Let's now force the validation to fail.

- Remove **Postal Code** from **HE properties to fetch**
- Run the Flow again.
- The edge bubble is now red, indicating and error.

<img src="/img/flows/structures/svtm-failed.png" alt="600" width="600" />

- Click it to see the reason for the failure in the Rejected tab.

![600](/img/flows/structures/tutorial-videos/A51-failed-validation.png)

### Aborting the Flow on failure
By default, Ziggy will abort the Flow if a validation fails.

However, you can tell Ziggy to strip records which fail the validation. We can, at the same time, store failed records in the data store.

![600](/img/flows/structures/tutorial-videos/A51-no-abort-validate.png)

- Uncheck **Abort flow for failed validation**.
- Optionally, enter a Data Store namespace name where rejected records can be added.
- Run the Flow again.
- Click the edge bubble.
- You'll notice that there is now a **Rejected** tab, which lists the records that failed the validation and the reason for the rejection.

![600](/img/flows/structures/tutorial-videos/A51-failed-validation.png)

### Using the Data Store for rejections
In the above screenshot, we specified that any rejections should be stored in the **rejected companies** namespace.

If you want, you can then use the **Data Store Block** to process these or just use the Data Store viewer as a log viewer.

To do this, hover on the Stores icon in the top navigation bar and click.

![1000](/img/flows/structures/tutorial-videos/A51-datastore-listing.png)

![500](/img/flows/structures/tutorial-videos/A51-datastore-item.png)

## Transformations
The **Transformer** tab lets you use basic Javascript to perform any sort of validation, data transformation or even a hard-coded mapping with ease.

- Click the edge bubble from the HubSpot Read block.
- Check **Transform** in the top row.
- A **Transform** tab will now appear, where you can enter some Javascript expressions.

![800](/img/flows/structures/tutorial-videos/A53-transformer.png)

Feel free to copy paste the following code.

```javascript
data['newKey'] = 'My New Key'
data['anotherKey'] = data.name.slice(0,5).toUpperCase()

if(!data['hs_country_code']) 
  data['hs_country_code'] = 'UNKNOWN'
```

Now run the Flow and inspect the edge data.

<img src="/img/flows/structures/tutorial-videos/A53-transformed.png" alt="600" width="500" />

You can see that the transformer has added two new keys `newKey` and `anotherKey`. It has also modifed `hs_country_code` where it was null when arriving on the edge.

### Rejecting data
You can also use the Transformer to perform custom validations that are not easy to specify 
using the **Validate** option.

To reject a record, you should return a string value with the reason for failure.

Try the following modified transformer code.

```javascript
if(!data['hs_country_code']) 
  return "Missing country code"
```

Run the Flow and inspect the edge data.

<img src="/img/flows/structures/tutorial-videos/A53-transform-reject.png" alt="600" width="500" />


### Combined with Validations and Mappings
You don't have to use a validation when using the Transformer. If you do, the validation will be executed first.

If you perform a mapping using the **Map** option, then the Transformer will execute before the Mapping.


## Mapping
Mapping helps you transform one data structure to another.

There are various ways you achieve this.

1. Use a **Transformer** as explained in the previous tutorial.
2. Use a **Javascript Block**, although you would normally only need to use this if you are performing asynchronous tasks as a part of the mapping process.
3. Use a Google Sheet in the **Mapper Block** for simple mappings that non-technical users can specify.
4. Use the **Map** option provided in the edge dialog, which we'll explore here.

### Structures (again)
To use the Map feature, you will need to have defined a **Structure** to map to.

- In the top navigation bar, hover and click on the Structures item.
- You should see a Structure **A50 Output**.

<img src="/img/flows/structures/tutorial-videos/A55-structures.png" alt="1000" width="700" />

<img src="/img/flows/structures/tutorial-videos/A55-structure.png" alt="400" width="500" />

This should be clear if you have already loooked at the earlier tutorials.

### Map
- Click on the edge bubble.
- Check the **Map** box in the top row of the dialog.
- From the dropdown, select **A50 Output**.

<img src="/img/flows/structures/tutorial-videos/A55-map-unselected.png" alt="500" width="400" />

- Press the **Guess Mapping** button. This will show a list of the input fields.
- You can map manually by clicking a pill and choosing the target field to map to.
- You can also press the **Guess mapping** button, which will do its best to automate this. You should carefully check the results and edit as needed.

<img src="/img/flows/structures/tutorial-videos/A55-map-selected.png" alt="500" width="500" />

Once you have the configuration you see above, run the Flow and click on the edge bubble.

If you look at the Data and Data Out tabs, you can see how the mapping has done its job.

![500](/img/flows/structures/tutorial-videos/A55-data-in.png)


![500](/img/flows/structures/tutorial-videos/A55-data-out.png)

### Combining Mapping with Validations and Transformers

By combining mapping with validations and transformers, you can build very powerful data transformations with no or minimal coding.







