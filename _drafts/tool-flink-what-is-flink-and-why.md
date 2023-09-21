---
layout: post
title: "[Tool - Flink] What is Flink, and Why"
---

# What is Flink

> Apache Flink is a framework and distributed processing engine for **stateful** computations over unbounded and bounded **data streams**.
>
> -- https://flink.apache.org/what-is-flink/flink-architecture/

There a some important characteristics about Stream Processing:

- Delivery guarantees: At-least-once, At-most-once, Exactly-once
- Fault tolerance: Checkpointing, Savepoints, Failure recovery
- Performance: Latency, Throughput, Backpressure
- State management: Stateful processing, State TTL, State backend
- Event time processing: Watermarks, Timestamps, Windowing

### Native Streaming

Flink treat all data intput as stream, batch processing is just a special case of stream processing with bounded and recorded stream. Thus makes Flink a native streaming engine. It can process data as soon as it arrives, compared to Spark streaming, which process data in micro-batches. Spark streaming is called near real-time processing, while Flink is called real-time processing.

### Stateful Processing

Flink is a stateful processing engine, which means it can maintain the state of the data. It can remember the state of the data, and it can use the state of the data to process the data. For example, it can count the number of times a user has logged in, and it can use the number of times a user has logged in to determine whether the user is a frequent user.

### Architectural Characteristics

- Deployment: Standalone, YARN, Mesos, Kubernetes
- Scalability: Application can be scaled up to unlimited machines
- Performance: Low latency, High throughput

## Building Blocks

### Stream

Flink treats all data as stream:

- Bounded/unbounded data
- Real-time/recored data

### State

State is a base stone of Flink. Flink provides powerful state management:

- Multiple state priitives: value, list, map
- Multiple state backends: memory, file, rocksdb
- Exactly-once state consistency: checkpoint, savepoint
- Large state support: asynchronous snapshots, incremental checkpoints
- Scalable state: partitioned state, broadcast state to more or less machines

#### State Backends

- MemoryStateBackend
- FsStateBackend
- RocksDBStateBackend
- EmbeddedRocksDBStateBackend
- RemoteKeyedStateBackend

### Time

Flink provides rich set of time-related features: event-time mode, watermarks, late events handling, processing time mode.

### Checkpoint

Checkpoints make state in Flink fault tolerant by allowing state and the corresponding stream positions to be recovered. Checkpoints are the core of Flink's fault tolerance mechanism. Flink's checkpointing mechanism is based on the Chandy-Lamport distributed snapshotting algorithm.

#### Checkpoint vs Savepoint

The main difference between checkpoints and savepoints is that checkpoints are triggered by Flink, while savepoints are triggered by users. Checkpoints are used to recover from failures, while savepoints are used to upgrade or downgrade the application.

#### Unaligned Checkpoint

Unaligned checkpoints contain in-flight data, to overcome the problem of latency, makes checkpointing idpendent of the throughput of the data stream.



## Layered Architecture


As as streaming data processing framework, Flink is always compared with Spark Streaming and Storm. The following table shows the comparison of these three frameworks.

| Framework                | Spark  | Storm  | Flink  |
| ------------------------ | ------ | ------ | ------ |
| Stateful                 | No     | Yes    | Yes    |
| Bounded                  | Yes    | No     | Yes    |
| Latency                  | 100ms  | 10ms   | 1ms    |
| Release                  | 2013   | 2011   | 2014   |
| License                  | Apache | Apache | Apache |
| Exactly-once             | No     | No     | Yes    |
| Backpressure             | No     | No     | Yes    |
| Batch                    | Yes    | No     | Yes    |
| Window                   | Yes    | Yes    | Yes    |
| Iteration                | Yes    | Yes    | Yes    |
| SQL                      | Yes    | No     | Yes    |
| Machine Learning         | Yes    | No     | Yes    |
| Graph Processing         | Yes    | No     | Yes    |
| Complex Event Processing | Yes    | No     | Yes    |

# Appendix

## Chandy–Lamport’s global state recording algorithm

The Chandy–Lamport algorithm is a distributed algorithm for recording a consistent global state of a distributed system.

The algorithm has some assumptions:
- Finite number of processes
- Finite number of channels
- Process communicates with channels
- Channels are FIFO

## Algorithm:

### Initiating a snapshot

Process p_i initiates the snapshot
- p_i records its local state
- p_i sends a marker message to all processes using outgoing channels
- recording all incoming messages from channels c_ji for j not equal to i

### Propagating a snapshot

For all process p_j consider a message on channel c_kj
- If p_j see the marker for the first time
  - p_j records its local state and marks c_kj as empty
  - p_j sends the marker to all other processes using outgoing channels
  - start recording all incoming messages from channels c_lj for l not equal to j or k

- Else:
  - add all messages from incoming channels since recording to their state

### Terminate a snapshot

- All processes have received a marker and recorded their state
- All processes have received a marker from all n-1 incoming channels
- The central coordinator gather the partial state to build the global snapshot



