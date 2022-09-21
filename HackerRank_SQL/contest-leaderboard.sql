-- Contest Leaderboard
-- 1. maximum scores for all of the challenges.
-- 2. sum of maximum scores.

SELECT H.hacker_id, H.name, SUM(S.max_socre) total_score
FROM Hackers H 
    LEFT JOIN (
        SELECT hacker_id, MAX(score) max_socre
        FROM Submissions
        GROUP BY hacker_id, challenge_id
    ) S
    ON H.hacker_id = S.hacker_id
GROUP BY H.hacker_id, H.name
HAVING total_score > 0
ORDER BY total_score DESC, H.hacker_id;
