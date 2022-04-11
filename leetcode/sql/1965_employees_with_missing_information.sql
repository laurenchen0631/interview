Create table If Not Exists Employees (employee_id int, name varchar(30))
Create table If Not Exists Salaries (employee_id int, salary int)
Truncate table Employees
insert into Employees (employee_id, name) values ('2', 'Crew')
insert into Employees (employee_id, name) values ('4', 'Haven')
insert into Employees (employee_id, name) values ('5', 'Kristian')
Truncate table Salaries
insert into Salaries (employee_id, salary) values ('5', '76071')
insert into Salaries (employee_id, salary) values ('1', '22517')
insert into Salaries (employee_id, salary) values ('4', '63539')

SELECT *
FROM (
  SELECT employee_id
  FROM Employees e
  WHERE NOT EXISTS (SELECT employee_id FROM Salaries s WHERE s.employee_id = e.employee_id)
  UNION
  SELECT employee_id
  FROM Salaries s
  WHERE NOT EXISTS (SELECT employee_id FROM Employees e WHERE s.employee_id = e.employee_id)
) d
ORDER BY d.employee_id;
