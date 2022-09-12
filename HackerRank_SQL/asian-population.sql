-- Population Census


SELECT SUM(CT.POPULATION)
FROM CITY CT INNER JOIN COUNTRY CN
ON CT.COUNTRYCODE = CN.CODE 
WHERE CN.CONTINENT = 'Asia';


/* 
Performance wise, they are exactly the same. 
I would personally stick with joining tables explicitly... that is the "socialy acceptable" way of doing it.
- stackoverflow

SELECT SUM(CT.POPULATION)
FROM CITY CT, COUNTRY CN
WHERE CT.COUNTRYCODE = CN.CODE AND CN.CONTINENT = 'Asia';
*/
