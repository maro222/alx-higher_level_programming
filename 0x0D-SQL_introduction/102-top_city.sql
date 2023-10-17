-- temperature #1
SELECT TOP 3 `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE month = 7 or month = 8
GROUP BY `avg_temp`
ORDER BY `value` DESC;
