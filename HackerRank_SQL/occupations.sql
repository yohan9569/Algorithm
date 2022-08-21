-- Occupations

SELECT
    MAX(IF(Occupation='Doctor', Name, Null)),
    MAX(IF(Occupation='Professor', Name, Null)),
    MAX(IF(Occupation='Singer', Name, Null)),
    MAX(IF(Occupation='Actor', Name, Null))
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY Occupation ORDER BY Name) RN FROM OCCUPATIONS
) temp
GROUP BY RN;
