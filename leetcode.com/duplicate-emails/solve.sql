SELECT Email
FROM (
    SELECT
        COUNT(1) AS cnt,
        Email AS Email
    FROM Person
    GROUP BY Email
) CountTable
WHERE cnt > 1
