---
layout: post
title: "[Algorithm] LSM-Tree"
---

LSM-Tree is a data structure provides low cost indexing and high write throughput. It is commonly used in various applications and systems, including: [HBase](https://hbase.apache.org/), [Cassandra](https://cassandra.apache.org/), [RocksDB](https://rocksdb.org/).

## Overview

LSM trees are designed to handle high write volumes. They are append-only, and keep data sorted in memory, and optimized for write-heavy workloads. LSM trees are usually used with a write-ahead log (WAL) to ensure durability.

## Design

A typical LSM tree consists of various components:

- **Memtable**: a sorted in-memory data structure, usually a red-black tree or a skip list. It is used to store recently written data. When the memtable is full, it is flushed to disk as a new SSTable.
- **SSTable**: a sorted on-disk data structure, usually a sorted string table. It is used to store data that has been flushed from the memtable. SSTables are immutable, and are never updated. When an SSTable is full, it is merged with other SSTables to form a new SSTable.
- **Bloom filter**: a probabilistic data structure used to test whether an element is a member of a set. It is used to reduce the number of disk reads when looking up a key. It is usually stored in memory.
- **Write-ahead log (WAL)**: a log used to ensure durability. It is usually stored on disk.

With these components, we can describe how write, read and compaction works in a LSM tree.

### Write

When a write request comes in, the data will be appended to the WAL, and then inserted into the memtable. If the memtable is full, it will be flushed to disk as a new SSTable. The write is considered complete when it is appended to the WAL. The memtable will be recovered from the WAL when the LSM tree is restarted. The bloom filters is also updated when the memtable is flushed.

### Read

When a read request comes in, the LSM tree will first check the memtable. If the key is found in the memtable, the read is complete. Otherwise, it will check the bloom filters of the SSTables. If the key is not found in the bloom filters, the read is complete. Otherwise, it will check the SSTables. If the key is found in the SSTables, the read is complete. Otherwise, the read is complete.

### Compaction

When the number of SSTables reaches a certain threshold, the LSM tree will trigger a compaction. During compaction, the LSM tree will read all SSTables, merge them, and write the result to a new SSTable. The new SSTable will replace the old SSTables. The bloom filters will also be updated.

## Conclusion

Other than algorithms, LSM tree is like a system design parttern, which can be used in various applications and systems. It is a good example of how to design a system with low cost indexing and high write throughput.

# References
- RocksDB: [https://rocksdb.org/](https://rocksdb.org/)