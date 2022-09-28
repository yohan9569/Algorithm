-- Interviews

SELECT CT.contest_id, CT.hacker_id, CT.name, 
    SUM(SS.TS), SUM(SS.TAS), 
    SUM(VS.TV), SUM(VS.TUV)
FROM Contests CT
    JOIN Colleges CL
    ON CT.contest_id = CL.contest_id
    JOIN Challenges CH
    ON CL.college_id = CH.college_id
    LEFT JOIN (
        SELECT challenge_id, SUM(total_submissions) TS, 
            SUM(total_accepted_submissions) TAS
        FROM Submission_Stats
        GROUP BY challenge_id
    ) SS
    ON CH.challenge_id = SS.challenge_id
    LEFT JOIN (
        SELECT challenge_id, SUM(total_views) TV, SUM(total_unique_views) TUV
        FROM View_Stats
        GROUP BY challenge_id
    ) VS
    ON CH.challenge_id = VS.challenge_id
GROUP BY 1,2,3
HAVING SUM(SS.TS) + SUM(SS.TAS) + SUM(VS.TV) + SUM(VS.TUV) != 0
ORDER BY 1;
