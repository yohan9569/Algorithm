-- Weather Observation Station 12

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP "^[^aeiou]" AND CITY REGEXP "[^aeiou]$";
