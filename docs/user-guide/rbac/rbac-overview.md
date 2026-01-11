---
title: RBAC & User Management
---

This section covers user management and role-based access control (RBAC) in Ziggy.

General User Management, Team Management and logs can be accessed from Global Settings by Sys Admins or Admins.

## Entities
Entities are the main objects within Ziggy : Flows, Connections, Secrets, Schedules, Messaging Items.

## SMTP

It is strongly recommended you configure your SMTP settings before creating any users. If you don't then you will need to manage passwords entirely through the CLI, which is cumbersome.

Once SMTP is configured, new users will receive new passwords and password resets via email.

## Summary 
Ziggy supports the following general RBAC concepts.

- **User**
- **Team** - a collection of users. Teams can be assigned to 
- **Role** - Sys Admin, Admin, Editor, Operator, Service Account 
- **Logs** - accessible, by Admins, show logs of logins, access denials and entity modifications (creations, updates and deletions)).
- **Assignments** - a user can assign access to an individual Entity by a) assigning a user with a specific role for that entity or b) a Team with a specific role.



- has a SysAdmin who has full control over all aspects of the platform and can fully access Flows, Connections, Secrets, Schedules, Messaging etc.
