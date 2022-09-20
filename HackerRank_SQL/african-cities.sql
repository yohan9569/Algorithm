-- African Cities

SELECT CT.NAME
FROM CITY CT INNER JOIN COUNTRY CN
ON CT.COUNTRYCODE = CN.CODE
WHERE CN.CONTINENT = 'Africa';