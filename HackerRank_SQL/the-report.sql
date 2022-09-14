-- The Report

SELECT IF(Grade > 7, Name, NULL) AS 'Nm', Grade, Marks
FROM (
    SELECT Name, Marks, (
            SELECT Grade FROM Grades G WHERE G.Min_Mark <= S.Marks AND G.Max_Mark >= S.Marks
        ) AS 'Grade'
    FROM Students S
    ) T
ORDER BY 2 DESC, 1 ASC;
