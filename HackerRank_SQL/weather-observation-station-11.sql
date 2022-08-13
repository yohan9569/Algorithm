-- Weather Observation Station 11

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP "^[^aeiou]" OR CITY REGEXP "[^aeiou]$";
