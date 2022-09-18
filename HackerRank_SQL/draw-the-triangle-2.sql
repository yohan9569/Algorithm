-- Draw The Triangle 2

-- information_schema.tables, It acts as dummy.
-- 'where' clause runs before the 'select' clause.


SET @R = 0;
SELECT REPEAT('* ', @R:=@R+1)
FROM information_schema.tables
WHERE @R<20;
