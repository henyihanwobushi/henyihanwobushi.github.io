---
layout: post
title: "[Algorithm] Cardinality"
---

Cardinality is the number of elements in a set or other grouping, as a property of that grouping. For example, the cardinality of a set $A$ is denoted as $|A|$, which means the number of elements in $A$.

When we calculate DAU, MAU, WAU, we are actually calculating the cardinality of the set of users who use the app daily, monthly, weekly. We can easily calculate the cardinality of a set by using the `count` function in SQL.

```sql
SELECT COUNT(DISTINCT user_id) FROM user_table;
```

But when there is a large amount of data, the `count distinct` function will be very slow. So we need to use other methods to calculate the cardinality of a set.


# Distinct then Count

The most common method is get distinct user id first, and then count the number of user id.

```sql
SELECT COUNT(*) FROM (
    SELECT DISTINCT user_id FROM user_table
) AS t;
```

Or we can use `GROUP BY` to get the distinct user id.

```sql
SELECT COUNT(*) FROM (
    SELECT user_id FROM user_table GROUP BY user_id
) AS t;
```

Or we can use a window function `ROW_NUMBER` to get the distinct user id.

```sql
SELECT COUNT(*) FROM (
    SELECT user_id, ROW_NUMBER() OVER (PARTITION BY user_id) AS row_number FROM user_table
) AS t WHERE row_number = 1;
```

In Hive, all these methods requires one more Reducer to do the `distinct` operation, which will generate a temporary table. But with the distinct process, the data size will be reduced, and the `COUNT` operation can run faster. Because the `COUNT` operation without `DISTINCT` can be partially aggregated in the Mapper with just a number, but `COUNT` with `DISTINCT` requires a set to store the distinct values, which may be very large.

# Optimized Count Distinct

There are some optimized algorithms to calculate the cardinality of a set. The most common one is **HyperLogLog** algorithm. The basic idea is to use a hash function to map the elements in the set to a binary string, and then count the number of leading zeros in the binary string. The number of leading zeros is the estimated cardinality of the set.

```sql
SELECT HLL_COUNT.MERGE(HLL_COUNT.INIT(user_id)) FROM user_table;
```

Or, in MaxCompute, we can use `APPROX_DISTINCT` function to calculate the cardinality of a set.

```sql
SELECT APPROX_DISTINCT(user_id) FROM user_table;
```

## HyperLogLog Algorithm

The HyperLogLog algorithm is a probabilistic algorithm, which means it can only give an estimated result.

The basic idea of HyperLogLog algorithm is to use a hash function to map the elements in the set to a binary string, and then count the number of leading zeros in the binary string. The number of leading zeros is the estimated cardinality of the set. If the number of leading zeros is $n$, then the estimated cardinality of the set is $2^n$.

For example, if we have a set of 1000 elements, and we use a hash function to map the elements to a binary string, the binary string may be like this.

```
000
001
010
011
100
101
110
111
```

The number of leading zeros is 3, so the estimated cardinality of the set is 8.

There will be three operations in the HyperLogLog algorithm:

- ADD


- COUNT: count the number of leading zeros in the binary string

- MERGE: merge two binary strings