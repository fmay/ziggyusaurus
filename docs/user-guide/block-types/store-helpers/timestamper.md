---
title: Timestamper
---

# Timestamper

Used to generate, read or reset a timestamp. 

A typical use case is running a Flow that needs to fetch data that has changed since the last time the Flow ran.

Let's say you want to extract data from Hubspot for BI reporting. 
If you have very large amounts of data, you only want to fetch data that has 
changed since the last time you ran the Flow.

Below is an example Flow that does the following. You'll find this in the tutorial 
Flows under **Reporting 10 - Import Companies, Deals**.

<img src="/img/flows/blocks/store-utility/timestamper.png" alt="Upsert" width="1200" />

- uses the Timestamper block to get the timestamp of the last execution. If it has not run before, it sets the date to Jan 01, 1970.
- Reads in all the Deals, with a filter applied that references the timestamp.
- Gets association Companies.
- Writes that data to a SQL database.
- Once the batch has completed, it sets the current date time, which is read the next time you run the Flow.

In another Flow, or directly from the Data Store browser, you can reset this date in case 
you want to re-fetch all the data.

## Mode

- **Get** - reads the value specified by the **Identifier**. If it does not exist, it set the timestamp to Jan 01, 1970.
- **Set** - generates a timestamp with the current date and time.
- **Reset - resets the timestamp to Jan 01, 1970.

## Identifier
This is a string (Data Store namespace) that uniquely identifies this particular timestamp. 
You use the same name when reading at the start of the Flow (or in another Flow).

## Set from variable
Set the timestamp from the specified Flow variable. If neither this nor **Set from Edge** are specified, it will use the current date/time.

## Set from Edge
Set the timestamp from the specified edge key. If neither this nor **Set from variable** are specified, it will use the current date/time.

## Output key
For **Get** mode, this creates a key on the output edge with the timestamp that was stored.


