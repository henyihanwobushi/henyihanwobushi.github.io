---
layout: post
title: "[Architecture] CQRS"
---

Command Query Responsibility Segregation (CQRS) is an architectural pattern that separates the responsibilities of commands and queries in a system.

The pattern uses two separate models:
- queries, which are responsible for reading data, and 
- commands, which are responsible for updating data. 

CQRS is used to **decouple** read and write workloads from each other for better performance, security, and scalability.

## Read/Write Separation

MySQL supports master-slave replication, which allows you to replicate data from one database to another. The master database is used for writes, while the slave database is used for reads. This is a form of read/write separation.

## CQRS with Read/Write Separation

CQRS is a more general form of read/write separation. Instead of having a single database that handles both reads and writes, you have two separate databases: one for reads and one for writes.

