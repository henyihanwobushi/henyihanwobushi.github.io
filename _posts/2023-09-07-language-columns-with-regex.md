---
layout: post
title: "[language] REGEX Column Specification"
date: 2023-09-07 00:47 +0800
---
> A SELECT statement can take regex-based column specification in Hive releases prior to 0.13.0, or in 0.13.0 and later releases if the configuration property hive.support.quoted.identifiers is set to none. 
> 
> We use Java regex syntax. Try http://www.fileformat.info/tool/regex.htm for testing purposes.
> The following query selects all columns except ds and hr.
> 
> ```sql
> SELECT `(ds|hr)?+.+` FROM sales
> ```

-- [Hive Language Manual - Select](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Select){:target="_blank"}

在Hive中，可以使用正则表达式来选择列，但是需要注意的是，这个功能在0.13.0版本之后才支持，而且需要设置`hive.support.quoted.identifiers`为`none`。

这个功能在一些特定的场合可以极大的减少代码行数，比如两个存在同名字段的表的关联，除同名字段需要特殊处理外，其他自动继承到结果表中：

```sql
SELECT 
    coalesce(a.id, b.id) as id,
    a.amount + b.amount as amount,
    a.`(id|amount)?+.+`,
    b.`(id|amount)?+.+`,
FROM a
FULL JOIN b 
ON a.id = b.id
```