Create table If Not Exists Student (student_id int, student_name varchar(30))
Create table If Not Exists Exam (exam_id int, student_id int, score int)
Truncate table Student
insert into Student (student_id, student_name) values ('1', 'Daniel')
insert into Student (student_id, student_name) values ('2', 'Jade')
insert into Student (student_id, student_name) values ('3', 'Stella')
insert into Student (student_id, student_name) values ('4', 'Jonathan')
insert into Student (student_id, student_name) values ('5', 'Will')
Truncate table Exam
insert into Exam (exam_id, student_id, score) values ('10', '1', '70')
insert into Exam (exam_id, student_id, score) values ('10', '2', '80')
insert into Exam (exam_id, student_id, score) values ('10', '3', '90')
insert into Exam (exam_id, student_id, score) values ('20', '1', '80')
insert into Exam (exam_id, student_id, score) values ('30', '1', '70')
insert into Exam (exam_id, student_id, score) values ('30', '3', '80')
insert into Exam (exam_id, student_id, score) values ('30', '4', '90')
insert into Exam (exam_id, student_id, score) values ('40', '1', '60')
insert into Exam (exam_id, student_id, score) values ('40', '2', '70')
insert into Exam (exam_id, student_id, score) values ('40', '4', '80')

WITH cte AS (
    SELECT student_id,
        RANK() OVER (PARTITION BY exam_id ORDER BY score) AS rnk1,
        RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS rnk2
    FROM Exam
)

SELECT DISTINCT student_id, student_name
FROM Exam JOIN Student USING (student_id)
WHERE student_id NOT IN (
    SELECT student_id
    FROM cte
    WHERE rnk1 = 1 OR rnk2 = 1
)
ORDER BY student_id

