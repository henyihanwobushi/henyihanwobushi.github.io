---
layout: post
title: "[python] String Format Cheat Sheet"
---

| Type        | Description                               | %-format | f-string/str.format() |
| :---------- | :---------------------------------------- | :------- | :-------------------- |
| String      | String                                    | %s       | {}                    |
| Float       | Float                                     | %f       | {:f}                  |
| Integer     | Integer                                   | %d       | {:d}                  |
| Binary      | Binary format                             | %b       | {:b}                  |
| Octal       | Octal number                              | %o       | {:o}                  |
| Hexadecimal | Hexadecimal number (lowercase letters)    | %x       | {:x}                  |
| Exponential | Exponential notation (with lowercase 'e') | %e       | {:e}                  |

## Padding and aligning strings

| Type    | Description    | %-format | f-string/str.format() |
| :------ | :------------- | :------- | :-------------------- |
| Padding | Align to Right | %20s     | {:20}                 |
| Padding | Align to Left  | %-20s    | {:<20}                |
| Padding | Centering      | %^20s    | {:^20}                |
| Triming | Trim to Length | %.5s     | {:.5}                 |
