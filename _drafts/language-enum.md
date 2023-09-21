---
layout: post
title: "[Language] Enum"
---

# Introduction

Enum is a data type that has a set of predefined values. It is used to represent a set of possible values. For example, the days of the week can be represented using an enum.

In the book of "The Art of Readable Code", it says that "Enums are a great way to make your code more readable. They make it clear to the reader that a variable is meant to have a limited set of values."

# Usage

## Singleton

The value of enum is handled by JVM and will be generated when the class is loaded. Which makes enum a singleton class. We can demonstrate this by the following code.

```java
public enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        System.out.println("do something");
    }

    public static void main(String[] args) {
        System.out.println(new String("abc") == new String("abc"));
        // prints false
        System.out.println(SingletonEnum.INSTANCE == SingletonEnum.INSTANCE);
        // prints true
    }
}
```

## Switch

Enum can be used in switch statement. It is more readable than using integer or string.

```java
public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;

    public static void main(String[] args) {
        for (Day day : Day.values()) {
            switch (day) {
                case SATURDAY:
                case SUNDAY:
                    System.out.println(day.name() + ": Weekends");
                    break;
                default:
                    System.out.println(day.name() + ": Weekdays");
                    break;
            }
        }
    }
}
```

# Enum and Code Smell

When use enum in switch statement to control the flow of the program, it will spread to multiple places, causing fragility. For example, if we add a new value to the enum, we need to modify the switch statement as well. It is better to use polymorphism to handle this.

We can use strategy pattern to handle this. We can create an interface and implement it in each enum value. Then we can use the interface to control the flow of the program.

```java
public interface Day {
    void doSomething();
}

public enum Monday implements Day {
    INSTANCE;

    @Override
    public void doSomething() {
        System.out.println("do something on Monday");
    }
}

public enum Tuesday implements Day {
    INSTANCE;

    @Override
    public void doSomething() {
        System.out.println("do something on Tuesday");
    }
}

```