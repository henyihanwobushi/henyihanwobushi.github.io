---
layout: post
title: "[language] Coroutine"
---

# Introduction

Coroutine is a computer program component that generalizes subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed. Coroutines are well-suited for implementing familiar program components such as cooperative tasks, exceptions, event loops, iterators, infinite lists and pipes.

# Coroutine in Python

Python has supported coroutines since version 2.5, released in September 2006. The implementation is based on the generators introduced in version 2.2. The `yield` statement, which was introduced in version 2.3, is used to suspend and resume execution in a way that is similar to the way `return` is used. The `yield` statement suspends execution and sends a value back to the caller, but retains enough state to enable the function to resume where it is left off. When resumed, the function continues execution immediately after the last `yield` run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

```python

```

# Reference

- The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software ([http://www.gotw.ca/publications/concurrency-ddj.htm](http://www.gotw.ca/publications/concurrency-ddj.htm))
- [https://www.finclip.com/news/f/54409.html](https://www.finclip.com/news/f/54409.html)