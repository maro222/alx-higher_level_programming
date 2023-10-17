-- temperature #0
SELECT city, AVG(`value`) As avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `value` DESC;
