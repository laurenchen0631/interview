Create table If Not Exists Student (student_id int,student_name varchar(45), gender varchar(6), dept_id int)
Create table If Not Exists Department (dept_id int, dept_name varchar(255))
Truncate table Student
insert into Student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1')
insert into Student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1')
insert into Student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2')
Truncate table Department
insert into Department (dept_id, dept_name) values ('1', 'Engineering')
insert into Department (dept_id, dept_name) values ('2', 'Science')
insert into Department (dept_id, dept_name) values ('3', 'Law')

SELECT dept_name, COUNT(student_id) AS student_number
FROM Department d
  LEFT JOIN Student s ON d.dept_id = s.dept_id
GROUP BY dept_name
ORDER BY student_number DESC, dept_name ASC