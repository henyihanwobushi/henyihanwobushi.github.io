---
layout: post
title: "[Tool] fish Cheat Sheet(Updating...)"
date: 2023-09-07 22:59 +0800
---
# Introduction

| What                       | How                                     |
| :------------------------- | :-------------------------------------- |
| set environment variable   | `set -x VARNAME value`                  |
| Erase environment variable | `set -e VARNAME`                        |
| Alias                      | `alias name 'command'`                  |
| Add Path                   | `fish_add_path "/path/to/your/bin/"`    |
| For Loop                   | `for i in (seq 1 10); echo $i; end`     |
| Math                       | `math "12345679 * 9"`                   |
| Conditional                | `if [ -e a.out ]; ./a.out; end`         |
| Comparesion                | `if [ 1 -eq 1 ]; echo "true"; end`      |
| Function                   | `function hello; echo "hello"; end`     |
| Function with arguments    | `function f -a a1; echo $a1; end`       |
| Function on Event          | `function h -e e; echo "hear"; end`     |
| Emit a Event               | `emit e`                                |
| Unset function             | `functions -e hello`                    |
| Abberviation               | `abbr -a gs git status`                 |
| Complete                   | `complete -c jekyll -a 'draft publish'` |
| Complete Erase             | `complete -c jekyll -e`                 |
 
# Reference
[Fish Cookbook](https://github.com/jorgebucaran/cookbook.fish/blob/main/README.md)