-- Challenges

SELECT H.hacker_id, H.name, COUNT(1) CC
FROM Hackers H LEFT JOIN Challenges C
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING CC = (SELECT MAX(SUB1.CC1)
             FROM (SELECT COUNT(1) CC1
                   FROM Challenges
                   GROUP BY hacker_id
             ) SUB1
    )
    OR CC IN (SELECT SUB2.CC2
              FROM (SELECT COUNT(1) CC2
                    FROM Challenges
                    GROUP BY hacker_id
              ) SUB2
              GROUP BY SUB2.CC2
              HAVING COUNT(1) = 1
    )
ORDER BY CC DESC, H.hacker_id;
