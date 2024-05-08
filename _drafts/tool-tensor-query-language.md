---
layout: post
title: "[Tool] Tensor Query Language"
---

## Introduction

Tensor Query Language (TQL) is a domain-specific language for querying tensors. It is designed to be a human-readable and writable language for querying tensors. TQL is inspired by SQL and GraphQL, and it is designed to be a general-purpose language for querying tensors.

## Syntax

The syntax of TQL is similar to SQL and GraphQL. TQL queries are composed of a series of clauses, each of which specifies a part of the query. The clauses are separated by commas, and the query is terminated by a semicolon.

The basic structure of a TQL query is as follows:

```
SELECT <fields>
FROM <source>
WHERE <condition>
GROUP BY <grouping>
ORDER BY <ordering>
LIMIT <limit>
```

## Examples

Here are some examples of TQL queries:

```
SELECT name, age
FROM people
WHERE age > 18
ORDER BY age DESC
LIMIT 10;
```
