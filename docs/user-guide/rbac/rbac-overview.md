---
title: RBAC & User Management
---

This section covers user management and role-based access control (RBAC) in Ziggy.

General User Management, Team Management and logs can be accessed from Global Settings by Sys Admins or Admins.

<img src="/img/rbac/rbac-settings.webp" alt="rbac settings" width="1000" />

## Entities
Entities are the main objects within Ziggy : Flows, Connections, Secrets, Schedules, Messaging Items.

## SMTP

It is strongly recommended you configure your [SMTP settings](/user-guide/Global-Settings.md#smtp) before creating any users. If you don't then you will need to manage passwords entirely through the CLI, which is cumbersome.

Once SMTP is configured, new users will receive new passwords and password resets via email.

## Summary 
Ziggy supports the following general RBAC concepts.

- [**User**](/user-guide/rbac/rbac-users.md) - individual users. For multi-tenant installations, users can switch between organizations.
- [**Team**](/user-guide/rbac/rbac-teams.md) - a collection of users. Entities can grant access to teams an a specific role for that assignment.
- [**Role**](/user-guide/rbac/rbac-roles.md) - Sys Admin, Admin, Editor, Operator, Service Account 
- [**Logs**](/user-guide/rbac/rbac-logs.md) - accessible, by Admins, show logs of logins, access denials and entity modifications (creations, updates and deletions).
- [**Assignments**](/user-guide/rbac/rbac-assignments.md) - a user can assign access to an individual Entity by a) assigning a user with a specific role for that entity or b) a Team with a specific role.
