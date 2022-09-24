-- Placements

SELECT S.Name
FROM Friends F
    LEFT JOIN Packages P1
    ON F.ID = P1.ID
    LEFT JOIN Packages P2
    ON F.Friend_ID = P2.ID
    LEFT JOIN Students S
    ON F.ID = S.ID
WHERE P2.Salary > P1.Salary
ORDER BY P2.Salary;
