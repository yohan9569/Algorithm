-- 15 Days of Learning SQL


SELECT totals.submission_date, totals.total, maximums.maximum, H.name
FROM (
    -- total number of unique hackers
    SELECT submission_date, COUNT(DISTINCT hacker_id) total
    FROM Submissions S1
    WHERE (submission_date - DATE('2016-03-01')) = (
        SELECT COUNT(DISTINCT submission_date)
        FROM Submissions S1_1
        WHERE S1.submission_date > S1_1.submission_date
            AND S1.hacker_id = S1_1.hacker_id
        )
    GROUP BY submission_date
) totals
JOIN(
    -- the hacker who made maximum number of submissions
    SELECT submission_date, hacker_id maximum
    FROM Submissions S2
    WHERE hacker_id = (
        SELECT hacker_id
        FROM Submissions S2_1
        WHERE S2.submission_date = S2_1.submission_date
        GROUP BY hacker_id
        ORDER BY COUNT(submission_id) DESC, hacker_id
        LIMIT 1
        )
    GROUP BY submission_date, hacker_id
) maximums
ON totals.submission_date = maximums.submission_date
JOIN Hackers H
ON maximums.maximum = H.hacker_id
ORDER BY totals.submission_date;
