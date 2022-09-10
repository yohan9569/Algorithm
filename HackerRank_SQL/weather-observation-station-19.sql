-- Weather Observation Station 19
-- *P1(a,c) and P2(b,d)*


SELECT TRUNCATE(
        SQRT(
            POW((MAX(LAT_N)-MIN(LAT_N)),2) +
            POW((MAX(LONG_W)-MIN(LONG_W)),2)
        )
    , 4)
FROM STATION;
