Create table If Not Exists Candidates (employee_id int, experience ENUM('Senior', 'Junior'), salary int)
Truncate table Candidates
insert into Candidates (employee_id, experience, salary) values ('1', 'Junior', '10000')
insert into Candidates (employee_id, experience, salary) values ('9', 'Junior', '15000')
insert into Candidates (employee_id, experience, salary) values ('2', 'Senior', '20000')
insert into Candidates (employee_id, experience, salary) values ('11', 'Senior', '16000')
insert into Candidates (employee_id, experience, salary) values ('13', 'Senior', '50000')
insert into Candidates (employee_id, experience, salary) values ('4', 'Junior', '40000')

WITH cte AS (
    SELECT *, SUM(salary) OVER(PARTITION BY experience ORDER BY salary) As acc
    FROM Candidates
), Seniors AS (
    SELECT employee_id, salary
    FROM cte
    WHERE experience = 'Senior' AND acc <= 70000
)

SELECT employee_id FROM Seniors
UNION
SELECT employee_id
FROM cte
WHERE experience = 'Junior' AND acc <= 70000 - (SELECT SUM(salary) FROM Seniors)