---
title: Troubleshooting
---

# Troubleshooting

Here are some common issues you may encounter and how to deal with them.

## Rate Limited APIs
Let's say you build an integration with an API that has rate limits. If you trigger many Flows in parallel that access that API then you are likely to hit the short term API limits very quickly.

### Problem
For example, HubSpot allows 10 API requests per second. If you have a single call to the HubSpot API in your Flow, but it suddenly receives a burst of 50 update requests per second for a short while. You are going to have problems with HubSpot's API rate limiting.

The HubSpot API NPM client actually manages retries very effectively. However, because you are getting 50 requests per second, these retries will accumulate and your Flow will quickly start to timeout.

### Solution
The calling system might be able to recognise the failure and manage the retries itself. This is fine if it's possible. but it may not be.

You can solve the problem in Ziggy as follows.

- Change your Flow to write data to the [Ziggy Data Store](/user-guide/block-types/utility/Data-Store) or SQL database. This will ensure no requests are lost.
- Create another Flow that is scheduled to run very frequently. This reads from the Data Store or database and runs through the data sequentially.

Even with this solution you need to bear in mind that other Flows might be operating on HubSpot in parallel. A way to solve this is as follows.

- Use the [Ziggy Memory Store](/user-guide/Memory-Store) to set a flag to indicate that the HubSpot Api is in use. Flows that are accessing the HubSpot APi can then query the memory store. If it is currently in use then you can use the Javascript Block's ```sleep()``` method to build in a small delay before retrying.

If you are performing migrations or data loads as opposed to integrations that could execute in parallel then you won't really have this problem. You can let the HubSpot NPM client take care of retries in the background.

