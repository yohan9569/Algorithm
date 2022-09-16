-- Draw The Triangle 1
-- information_schema.tables, It acts as dummy.

SET @R = 21;
SELECT REPEAT('* ', @R:=@R-1)
FROM information_schema.tables;
