-- 현재 계획 날마다 제출한 인원수 & 날마다 가장 제출 많이한 사람 & 이름 join

-- -- total number of unique hackers
-- SELECT S.submission_date, COUNT(DISTINCT S.hacker_id)
-- FROM Submissions S
-- GROUP BY S.submission_date
-- ORDER BY S.submission_date

-- 날마다 가장 제출 많이한 사람 뽑기
SELECT submission_date, hacker_id
FROM(SELECT submission_date, COUNT(hacker_id) CNT, hacker_id
    FROM Submissions
    GROUP BY submission_date, hacker_id
    ORDER BY submission_date) CT
GROUP BY submission_date
WHERE CNT = MAX(CNT) -- 여기가 안 풀리는 중

