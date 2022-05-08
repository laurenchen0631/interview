Create table If Not Exists Employee (employee_id int, team_id int)
Truncate table Employee
insert into Employee (employee_id, team_id) values ('1', '8')
insert into Employee (employee_id, team_id) values ('2', '8')
insert into Employee (employee_id, team_id) values ('3', '8')
insert into Employee (employee_id, team_id) values ('4', '7')
insert into Employee (employee_id, team_id) values ('5', '9')
insert into Employee (employee_id, team_id) values ('6', '9')

SELECT employee_id, team_size
FROM Employee e JOIN (
  SELECT team_id, COUNT(*) AS team_size
  FROM Employee 
  GROUP BY team_id
) t ON e.team_id = t.team_id

SELECT
  employee_id,
  COUNT(employee_id) OVER (PARTITION BY team_id) team_size
FROM EMPLOYEE