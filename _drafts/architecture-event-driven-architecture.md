---
layout: post
title: "[Architecture] Event-Driven Architecture"
---

Event-driven architecture also known as reactive architecture, is a software architecture pattern promoting the production, detection, consumption of, and reaction to events.

The reactive manifesto defines four characteristics of reactive systems:

- **Responsive**: the system responds in a timely manner if at all possible. Responsiveness means that problems may be detected quickly and dealt with effectively. Responsive systems focus on providing rapid and consistent response times, establishing reliable upper bounds so they deliver a consistent quality of service. This consistent behaviour **simplifies error handling**, builds end user confidence, and encourages further interaction.
- **Resilient**: the system stays responsive in the face of failure. This applies not only to highly-available, mission critical systems — any system that is not resilient will be unresponsive after a failure. Resilience is achieved by **replication, containment, isolation and delegation**. Failures are contained within each component, isolating components from each other and thereby ensuring that parts of the system can fail and recover without compromising the system as a whole. Recovery of each component is delegated to another (external) component and high-availability is ensured by replication where necessary. The client of a component is not burdened with handling its failures.
- **Elastic**: the system stays responsive under varying workload. Reactive Systems can react to changes in the input rate by increasing or decreasing the resources allocated to service these inputs. This implies designs that have no contention points or central bottlenecks, resulting in the ability to shard or replicate components and distribute inputs among them. Reactive Systems support **predictive**, as well as reactive, scaling algorithms by providing relevant live performance measures. They achieve elasticity in a cost-effective way on commodity hardware and software platforms.
- **Message Driven**: Reactive Systems rely on asynchronous message-passing to establish a boundary between components that ensures loose coupling, isolation, location transparency, and provides the means to **delegate errors as messages**. Employing explicit message-passing enables load management, elasticity, and flow control by shaping and monitoring the message queues in the system—and applying **back-pressure when necessary**. Location transparent messaging as a means of communication makes it possible for rebalancing to occur automatically across the distributed system, in order to address failures and hotspots as they occur.

## Multi-Thread vs Asynchronous

In a multi-threaded system, threads are used to handle concurrent requests. Each thread is assigned to a request, and will be blocked when waiting for I/O. When the I/O is complete, the thread will be unblocked and continue to process the request. The number of threads is limited by the number of CPU cores. When the number of requests exceeds the number of threads, the system will become unresponsive.

In an asynchronous system, requests are handled by a single thread. When a request comes in, the thread will start the I/O operation, and register a callback. When the I/O is complete, the callback will be called. The thread will then process the request, and register another callback. The system will never be blocked by I/O, and can handle an unlimited number of requests.

## Try it out

We will implement a simple kv store using event-driven architecture. The kv store will support the following operations:

- `get(key)`: get the value of a key
- `set(key, value)`: set the value of a key
- `delete(key)`: delete a key
- `scan(start, end)`: scan keys in a range
- `compact()`: compact the kv store
- `flush()`: flush the kv store

The kv store will be implemented as a LSM tree. We will use the following components:

- **Memtable**: a sorted in-memory data structure, usually a red-black tree or a skip list. It is used to store recently written data. When the memtable is full, it is flushed to disk as a new SSTable.
- **SSTable**: a sorted on-disk data structure, usually a sorted string table. It is used to store data that has been flushed from the memtable. SSTables are immutable, and are never updated. When an SSTable is full, it is merged with other SSTables to form a new SSTable.
- **Bloom Filter Index**: a probabilistic data structure used to test whether an element is a member of a set. It is used to reduce the number of disk reads when looking up a key. It is usually stored in memory.
- **Write-Ahead Log (WAL)**: a log used to ensure durability. It is usually stored on disk.


# References

- The Reactive Manifesto [https://www.reactivemanifesto.org/](https://www.reactivemanifesto.org/)