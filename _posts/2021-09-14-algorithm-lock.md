---
layout: post
title: "[Algorithm] Lock"
date: 2021-09-14 00:25 +0800
---
# Introduction

A lock is a synchronization mechanism for enforcing limits on access to a resource in an environment where there are many threads of execution. A lock is designed to enforce a mutual exclusion concurrency control policy.

# Lock Types

## Optimistic/Pessimistic locking

Optimistic locking is a strategy where the lock is acquired only when it is needed. That is, the lock is acquired only when a transaction is about to commit. If the lock is not acquired, the transaction is rolled back and retried.

Pessimistic locking is a strategy where the lock is acquired as soon as possible. That is, the lock is acquired as soon as a transaction starts. If the lock is not acquired, the transaction is blocked until the lock is released.

The optimistic locking is usually used in a read-heavy environment where the chance of conflict is low. While the pessimistic locking is usually used in a write-heavy environment where the chance of conflict is high.

Java provides optimistic locking through `java.util.concurrent.atomic` package. The `AtomicInteger` class provides atomic operations on `int` values. The `AtomicLong` class provides atomic operations on `long` values. The `AtomicReference` class provides atomic operations on reference values.

Here is a simple implementation of optimistic locking:

```java
public class Foo {
    private final AtomicInteger counter = new AtomicInteger();

    public void bar() {
        int oldValue = counter.get();
        int newValue = oldValue + 1;
        while (!counter.compareAndSet(oldValue, newValue)) {
            oldValue = counter.get();
            newValue = oldValue + 1;
        }
    }
}
```

We will talk about the implementation of optimistic locking in detail on another article.

## Coarse-Grained/Fine-Grained locking

Coarse-grained locking is a strategy where the lock is acquired on a large scope. That is, the lock is acquired on a large data structure. While fine-grained locking is a strategy where the lock is acquired on a small scope. That is, the lock is acquired on a small data structure.

The coarse-grained locking is usually used in a read-heavy environment where the chance of conflict is low. While the fine-grained locking is usually used in a write-heavy environment where the chance of conflict is high.

Here is a simple implementation of coarse-grained locking:

```java
public class Foo {
    private final List<String> list = new ArrayList<>();

    public void bar() {
        synchronized (list) {
            // do something
        }
    }
}
```

Here is a simple implementation of fine-grained locking:

```java
public class Foo {
    private final List<String> list = new ArrayList<>();
    private final Object lock = new Object();

    public void bar() {
        synchronized (lock) {
            // do something
        }
    }
}
```

## Spinlock/Mutex

A spinlock is a lock where the thread simply waits in a loop ("spins") repeatedly checking until the lock becomes available. A mutex is a lock where the thread blocks until the lock becomes available.

Spinlocks are efficient if threads are likely to be blocked for only a short period of time, as they avoid overhead from operating system process rescheduling or context switching. While mutexes are efficient if threads are likely to be blocked for a long period of time, as they avoid wasting CPU time.

Spinlocks are usually used in a read-heavy environment where the chance of conflict is low. While mutexes are usually used in a write-heavy environment where the chance of conflict is high.

Mutexes are usually implemented by operating system. While spinlocks are usually implemented by programming language.

Here is a simple implementation of spinlock:

```java
public class Foo {
    private final AtomicBoolean lock = new AtomicBoolean(false);

    public void bar() {
        while (!lock.compareAndSet(false, true)) {
            // do nothing
        }
        try {
            // do something
        } finally {
            lock.set(false);
        }
    }
}
```

Or we can use `tryLock` method of `Lock` interface:

```java
public class Foo {
    private final Lock lock = new ReentrantLock();

    public void bar() {
        while (!lock.tryLock()) {
            // do nothing
        }
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }
}
```

Here is a simple implementation of mutex:

```java
public class Foo {
    private final Lock lock = new ReentrantLock();

    public void bar() {
        lock.lock();
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }
}
```

## Blocking/Non-blocking

A blocking lock is a lock where the thread blocks until the lock becomes available. A non-blocking lock is a lock where the thread does not block until the lock becomes available.

## Reentrant Lock

A reentrant lock is a lock that can be acquired multiple times by the same thread. Reentrant locks require the thread to track how many times the lock has been acquired and to ensure that the lock is unlocked the same number of times.

The reentrant lock is owned by the thread that acquires it. That is, the thread that acquires the lock is the only thread that can release it, but can't be acquired by other threads.

Here is a simple implementation of reentrant lock:

```java
public class Foo {
    private final Lock lock = new ReentrantLock();

    public void bar() {
        lock.lock();
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }

    public void baz() {
        lock.lock();
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }
}
```

Opposite to reentrant lock is non-reentrant lock. A non-reentrant lock is a lock that can be acquired only once by the same thread. Non-reentrant locks do not require the thread to track how many times the lock has been acquired and to ensure that the lock is unlocked the same number of times.

In Java world, the `synchronized` keyword is a non-reentrant lock. That is, a thread can acquire a `synchronized` lock only once. If a thread try to acquire a `synchronized` lock that is already acquired by itself, the thread will be blocked forever.

## Fair Lock

A fair lock is a lock that grants access to the longest waiting thread. That is, the lock is acquired in the order that threads requested it. While unfair lock is a lock that grants access to a thread that is randomly selected from the set of waiting threads.

A thread try to acquire a fair lock will be blocked if there is a thread waiting for the lock. While a thread try to acquire an unfair lock will be blocked only if there is a thread waiting for the lock and the lock is not available.

Reentrant lock is unfair by default. To create a fair reentrant lock, pass `true` to the constructor of `ReentrantLock`:

```java
public class Foo {
    private final Lock lock = new ReentrantLock(true);

    public void bar() {
        lock.lock();
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }

    public void baz() {
        lock.lock();
        try {
            // do something
        } finally {
            lock.unlock();
        }
    }
}
```

Fair lock is implemented by a queue. When a thread try to acquire a fair lock, it will be added to the queue. When the lock is released, the thread at the head of the queue will be granted access to the lock.

### AQS

AQS is the abbreviation of AbstractQueuedSynchronizer. AQS is a framework for implementing blocking locks and related synchronizers. AQS is the foundation of `java.util.concurrent` package.

AQS implements a FIFO queue that can be used to implement a fair lock. AQS provides a `tryAcquire` method that can be used to implement a non-blocking lock. AQS provides a `tryAcquireNanos` method that can be used to implement a timed lock.

AQS provides a `ConditionObject` class that can be used to implement a condition variable. A condition variable is a synchronization primitive that allows threads to wait until a particular condition occurs.

The core of AQS is a `volatile int` variable named `state`. The `state` variable is used to represent the state of the synchronizer. The `state` variable is used to represent the number of locks held by the thread if the synchronizer is a lock. The `state` variable is used to represent the number of permits available if the synchronizer is a semaphore.

### AQS vs CLH

AQS is a FIFO queue. CLH is a queue that is implemented by a linked list. AQS is a framework for implementing blocking locks and related synchronizers. CLH is a queue that can be used to implement a blocking lock.

AQS is the foundation of `java.util.concurrent` package. CLH is the foundation of `java.util.concurrent.locks` package.

AQS is used to implement a fair lock. CLH is used to implement a non-fair lock.

AQS is implemented by a `volatile int` variable named `state`. CLH is implemented by a linked list.

AQS provides a `tryAcquire` method that can be used to implement a non-blocking lock. CLH provides a `tryAcquire` method that can be used to implement a non-blocking lock.

AQS provides a `tryAcquireNanos` method that can be used to implement a timed lock. CLH does not provide a `tryAcquireNanos` method.

AQS provides a `ConditionObject` class that can be used to implement a condition variable. CLH does not provide a `ConditionObject` class.

## Read/Write Lock

A read lock allows concurrent access for read-only operations, while a write lock allows for mutual-exclusive access for read and write operations. That is, read locks are shared while write locks are exclusive.

Here is a simple implementation of read lock:

```java
public class Foo {
    private final ReadWriteLock lock = new ReentrantReadWriteLock();
    private final Lock readLock = lock.readLock();
    private final Lock writeLock = lock.writeLock();

    public void read() {
        readLock.lock();
        try {
            // do something
        } finally {
            readLock.unlock();
        }
    }

    public void write() {
        writeLock.lock();
        try {
            // do something
        } finally {
            writeLock.unlock();
        }
    }
}
```

## Shared/Exclusive Lock

The difference between read/write lock and shared/exclusive lock is that the former is a lock while the latter is a lock type. That is, read/write lock is a lock that has two lock types: read lock and write lock. A read lock is a shared lock while a write lock is an exclusive lock.

