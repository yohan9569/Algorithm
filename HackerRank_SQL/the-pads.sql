-- The PADS

SELECT CONCAT(Name, "(", LEFT(Occupation,1), ")")
FROM OCCUPATIONS
ORDER BY Name;
SELECT CONCAT('There are a total of ', SUM(1), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY SUM(1), Occupation;
