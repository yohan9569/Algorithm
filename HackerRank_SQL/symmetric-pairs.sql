-- Symmetric Pairs
-- SELF JOIN

SELECT F1.X, F1.Y
FROM Functions F1
    INNER JOIN Functions F2
    ON F1.Y = F2.X AND F1.X = F2.Y
GROUP BY F1.X, F1.Y
HAVING COUNT(F1.X) > 1 OR F1.X < F1.Y -- X=Y OR X<Y
ORDER BY 1;
