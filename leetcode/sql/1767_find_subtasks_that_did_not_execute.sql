Create table If Not Exists Tasks (task_id int, subtasks_count int)
Create table If Not Exists Executed (task_id int, subtask_id int)
Truncate table Tasks
insert into Tasks (task_id, subtasks_count) values ('1', '3')
insert into Tasks (task_id, subtasks_count) values ('2', '2')
insert into Tasks (task_id, subtasks_count) values ('3', '4')
Truncate table Executed
insert into Executed (task_id, subtask_id) values ('1', '2')
insert into Executed (task_id, subtask_id) values ('3', '1')
insert into Executed (task_id, subtask_id) values ('3', '2')
insert into Executed (task_id, subtask_id) values ('3', '3')
insert into Executed (task_id, subtask_id) values ('3', '4')

WITH RECURSIVE cte AS (
    SELECT task_id, subtasks_count AS subtask_id FROM Tasks
    UNION
    SELECT task_id, subtask_id - 1
    FROM cte
    WHERE subtask_id > 1
)

SELECT *
FROM cte
WHERE (task_id, subtask_id) NOT IN (SELECT * FROM Executed)