-- Ollivander's Inventory

SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W LEFT JOIN Wands_Property P
ON W.code = P.code
WHERE P.is_evil = 0
AND W.coins_needed = 
    (SELECT MIN(coins_needed)
     FROM Wands
     WHERE code = P.code AND power = W.power)
ORDER BY W.power DESC, P.age DESC;
