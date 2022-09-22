-- SQL Project Planning

SELECT S.Start_Date, MIN(E.End_Date)
FROM (SELECT Start_Date
    FROM Projects
    WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)
     ) S,
    (SELECT End_Date
    FROM Projects
    WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)
     ) E
WHERE S.Start_Date < E.End_Date
GROUP BY S.Start_Date
ORDER BY MIN(E.End_Date) - S.Start_Date, S.Start_Date;
