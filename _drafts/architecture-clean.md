---
layout: post
title: "[architecture] Clean"
---

# Introduction

The Clean Architecture is a set of practices to create a software architecture that is simple, understandable, flexible, testable, and maintainable.

# The Clean Architecture

The Clean Architecture is a layered architecture. The layers are:

- Entities
- Use Cases
- Interface Adapters
- Frameworks and Drivers
- Boundaries

In my opinion, the Clean Architecture is based on the basic principles of Object Oriented Programming and the SOLID principles. The Clean Architecture is a set of practices to create a software architecture that is simple, understandable, flexible, testable, and maintainable.

## SOLID principles:

- S: **S**ingle Responsibility Principle
- O: **O**pen-Closed Principle
- L: **L**iskov Substitution Principle
- I: **I**nterface Segregation Principle
- D: **D**ependency Inversion Principle

When we take the Business Rules as the most valuable part of the software, and based on the SOLID principles, we can see why the architecture is designed in this way.

## Entities

Entities encapsulate Enterprise wide business rules. An entity can be an object with methods, or it can be a set of data structures and functions. It doesn’t matter so long as the entities could be used by many different applications in the enterprise.

## Use Cases

Use Cases encapsulate application specific business rules. They are not reusable across different applications. They are also called Interactors.

## Interface Adapters

Interface Adapters convert data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the Database or the Web. They are also called Presenters and Controllers.

## Frameworks and Drivers

Frameworks and Drivers are the mechanisms that connect everything together. They are not reusable. They are specific to an application.

## Boundaries

Boundaries separate the use cases and entities from the interface adapters and frameworks and drivers. They are the places where the data crosses from one circle to another.

# How to Implement the Clean Architecture

## Entities

Entities are the business objects of the application. They encapsulate the most general and high-level rules. They are the least likely to change when something external changes. For example, you would not expect these objects to be affected by a change to page navigation, or security. No operational change to any particular application should affect the entity layer.

The Entities layer is where the most general business rules are kept. Entities encapsulate Enterprise wide business rules. An entity can be an object with methods, or it can be a set of data structures and functions. It doesn’t matter so long as the entities could be used by many different applications in the enterprise.

Other layers can have no knowledge of what an entity is doing. Entities can have no knowledge of the other layers. The only thing that matters is that the Entities layer is the heart of the business software.

Entities are also the least likely to change when something external changes. For example, you would not expect these objects to be affected by a change to page navigation, or security. No operational change to any particular application should affect the entity layer.

## Use Cases

The software in this layer contains application specific business rules. It encapsulates and implements all of the use cases of the system. These use cases orchestrate the flow of data to and from the entities, and direct those entities to use their enterprise wide business rules to achieve the goals of the use case.

We do not expect changes in this layer to affect the entities. We also do not expect this layer to be affected by changes to externalities such as the database, the UI, or any of the common frameworks. This layer is isolated from such concerns.

## Interface Adapters

The software in this layer is a set of adapters that convert data from the format most convenient for the use cases and entities, to the format most convenient for some external agency such as the Database or the Web.

It is this layer, for example, that will wholly contain the MVC architecture of a GUI. The Presenters, Views, and Controllers all belong in here. The models are likely just data structures that are passed from the controllers to the use cases, and then back from the use cases to the presenters and views.

Similarly, data is converted, in this layer, from the form most convenient for entities and use cases, into the form most convenient for whatever persistence framework is being used. i.e. The Database. No code inward of this circle should know anything at all about the database. If the database is a SQL database, then all the SQL should be restricted to this layer, and in particular to the parts of this layer that have to do with the database.

Also in this layer is any other adapter necessary to convert data from some external form, such as an external service, to the internal form used by the use cases and entities.

## Frameworks and Drivers

The outermost layer is generally composed of frameworks and tools such as the Database, the Web Framework, etc. Generally you don’t write much code in this layer other than glue code that communicates to the next circle inwards.

## Boundaries

The boundaries between the circles are interfaces that allow data to flow inwards. Nothing crosses the boundaries going the other direction. The use cases layer has interfaces that are implemented by the entities layer. The interface adapters layer has interfaces that are implemented by the use cases layer. The frameworks and drivers layer has interfaces that are implemented by the interface adapters layer.

