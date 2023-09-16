---
layout: post
title: "[Algorithm] Geo-Hashing"
---

# Introduction

Geo-Hashing is a way to encode a geographic location into a short string of letters and digits. It's a hierarchical spatial data structure which subdivides space into buckets of grid shape, which is one of the many applications of what is known as a Z-order curve, and generally space-filling curves.

## Geo-Hashing vs Geo-Referencing

Georeferencing is the process of adding geographic information to a digital image so that mapping software can place the image in its real-world location.

Geohashing and Georeferencing solve different problems to express the location of a point on the earth's surface.

# Geo-Reference Types

| Type | Description |
| ---- | ----------- |
| S2   | Google S2   |
| H3   | Uber H3     |


# References

- H3: [https://github.com/uber/h3](https://github.com/uber/h3)