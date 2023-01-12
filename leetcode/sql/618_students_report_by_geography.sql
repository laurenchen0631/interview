Create table If Not Exists Student (name varchar(50), continent varchar(7))
Truncate table Student
insert into Student (name, continent) values ('Jane', 'America')
insert into Student (name, continent) values ('Pascal', 'Europe')
insert into Student (name, continent) values ('Xi', 'Asia')
insert into Student (name, continent) values ('Jack', 'America')

SELECT 
    MAX(IF(continent='America', name, null)) AS America,
    MAX(IF(continent='Asia', name, null)) AS Asia,
    MAX(IF(continent='Europe', name, null)) AS Europe
FROM (
    SELECT *, RANK() OVER(PARTITION BY continent ORDER BY name) AS rnk
    FROM Student
)
GROUP BY rnk;