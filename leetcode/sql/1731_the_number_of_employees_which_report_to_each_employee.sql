Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
Truncate table Employees
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', 'None', '43')
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', 'None', '37')

SELECT
  a.employee_id,
  a.name,
  COUNT(*) AS reports_count,
  ROUND(AVG(b.age)) AS average_age
FROM Employees a JOIN Employees b
  ON a.employee_id = b.reports_to
GROUP BY a.employee_id
ORDER BY a.employee_id