---
layout: post
title: "[Algorithm] Map-Reduce"
---

Map-Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.

# Introduction

Map-Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. A MapReduce program is composed of a `Map()` procedure (method) that performs filtering and sorting (such as sorting students by first name into queues, one queue for each name) and a `Reduce()` method that performs a summary operation (such as counting the number of students in each queue, yielding name frequencies).

The "MapReduce System" (also called "infrastructure" or "framework") orchestrates the processing by marshalling the distributed servers, running the various tasks in parallel, managing all communications and data transfers between the various parts of the system, and providing for redundancy and fault tolerance.

The model is inspired by the map and reduce functions commonly used in **functional programming**, although their purpose in the MapReduce framework is not the same as their original forms. The key contributions of the MapReduce framework are not the actual map and reduce functions, but the scalability and fault-tolerance achieved for a variety of applications by optimizing the execution engine once. As such, a single-threaded implementation of MapReduce will usually not be faster than a traditional (non-MapReduce) implementation; any gains are usually only seen with multi-threaded implementations and/or multiple clustered machines.

Here is a simple shell script illustrating the basic idea of the MapReduce framework with a word count example:

# Reference

- Shuffle in Flink [https://www.alibabacloud.com/blog/flink-shuffle-3-0-vision-roadmap-and-progress_599809](https://www.alibabacloud.com/blog/flink-shuffle-3-0-vision-roadmap-and-progress_599809)
- MapReduce: A major step backwards [https://homes.cs.washington.edu/~billhowe/mapreduce_a_major_step_backwards.html](https://homes.cs.washington.edu/~billhowe/mapreduce_a_major_step_backwards.html)