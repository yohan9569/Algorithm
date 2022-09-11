-- Weather Observation Station 20



-- WINDOW FUNCTION VERSION

SELECT ROUND(LAT_N, 4)
FROM (SELECT PERCENT_RANK() OVER(ORDER BY LAT_N) PR, LAT_N FROM STATION) TMP
WHERE PR=0.5;




-- VARIABLE VERSION
-- 'if the number of observations is even, then the median is the simple average of the middle two numbers.'

SET @ROWNUM = -1;

SELECT ROUND(AVG(LAT_N), 4)
FROM (SELECT @ROWNUM := @ROWNUM+1 RN, LAT_N FROM STATION ORDER BY LAT_N) TMP
WHERE RN IN (FLOOR(@ROWNUM / 2), CEIL(@ROWNUM / 2));
