-- New Companies

SELECT company_code, founder, 
    (SELECT COUNT(DISTINCT(lead_manager_code)) FROM Lead_Manager L WHERE L.company_code=C.company_code),
    (SELECT COUNT(DISTINCT(senior_manager_code)) FROM Senior_Manager S WHERE S.company_code=C.company_code),
    (SELECT COUNT(DISTINCT(manager_code)) FROM Manager M WHERE M.company_code=C.company_code),
    (SELECT COUNT(DISTINCT(employee_code)) FROM Employee E WHERE E.company_code=C.company_code)
FROM Company C
ORDER BY company_code;
