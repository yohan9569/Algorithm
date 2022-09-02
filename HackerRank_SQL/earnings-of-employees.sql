-- Top Earners

SELECT salary*months AS total_earnings, SUM(1)
FROM Employee
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;
