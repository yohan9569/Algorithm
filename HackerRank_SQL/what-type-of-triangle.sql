-- Type of Triangle

SELECT 
    CASE
        WHEN GREATEST(A,B,C) >= (A+B+C-GREATEST(A,B,C)) THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN (A=B AND B!=C) OR (A=C AND B!=C) OR (B=C AND A!=C) THEN 'Isosceles'
        WHEN A!=B AND A!=C AND B!=C THEN 'Scalene'
    END
FROM TRIANGLES;
