-- 从route表中统计各省份（province）的uv、pv
SELECT
    province,
    COUNT(DISTINCT uid) AS uv,
FROM
    route
GROUP BY
    province;

-- 采用先Group by再Count的方式，改写SQL以优化去重计数性能
select
    count(1),
    province
from
    (
        SELECT
            province,
            uid,
        FROM
            route
        GROUP BY
            province,
            uid
    )
GROUP BY
    province;