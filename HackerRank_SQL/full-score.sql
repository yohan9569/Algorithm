-- Top Competitors

SELECT S.hacker_id, H.name
FROM Submissions S 
    INNER JOIN Challenges C 
    ON S.challenge_id = C.challenge_id
    INNER JOIN Difficulty D
    ON C.difficulty_level = D.difficulty_level
    INNER JOIN Hackers H
    on S.hacker_id = H.hacker_id
WHERE S.score = D.score
GROUP BY S.hacker_id, H.name
HAVING COUNT(*)>1
ORDER BY COUNT(*) DESC, S.hacker_id ASC;
