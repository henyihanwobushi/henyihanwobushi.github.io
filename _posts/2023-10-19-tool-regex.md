---
layout: post
title: "[Tool] Regex"
date: 2023-10-19 20:29 +0800
---
## Regex match nested parenthesis

```(\{(?>[^{}]+|(?1))*\})```

This regex matches nested parenthesis like:
- ```{{{}}}```
- ```{{{}{}{}{}{}{{}}{}{{{}}{{}{}}}}}```

