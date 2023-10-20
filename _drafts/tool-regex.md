---
layout: post
title: "[Tool] Regex"
---

## Regex match nested parenthesis

```(\{(?>[^{}]+|(?1))*\})```

This regex matches nested parenthesis like:
- ```{{{}}}```
- ```{{{}{}{}{}{}{{}}{}{{{}}{{}{}}}}}```

[https://regex101.com/r/7jKYoA/1](https://regex101.com/r/7jKYoA/1)