Create table If Not Exists Employee (id int, company varchar(255), salary int)
Truncate table Employee
insert into Employee (id, company, salary) values ('1', 'A', '2341')
insert into Employee (id, company, salary) values ('2', 'A', '341')
insert into Employee (id, company, salary) values ('3', 'A', '15')
insert into Employee (id, company, salary) values ('4', 'A', '15314')
insert into Employee (id, company, salary) values ('5', 'A', '451')
insert into Employee (id, company, salary) values ('6', 'A', '513')
insert into Employee (id, company, salary) values ('7', 'B', '15')
insert into Employee (id, company, salary) values ('8', 'B', '13')
insert into Employee (id, company, salary) values ('9', 'B', '1154')
insert into Employee (id, company, salary) values ('10', 'B', '1345')
insert into Employee (id, company, salary) values ('11', 'B', '1221')
insert into Employee (id, company, salary) values ('12', 'B', '234')
insert into Employee (id, company, salary) values ('13', 'C', '2345')
insert into Employee (id, company, salary) values ('14', 'C', '2645')
insert into Employee (id, company, salary) values ('15', 'C', '2645')
insert into Employee (id, company, salary) values ('16', 'C', '2652')
insert into Employee (id, company, salary) values ('17', 'C', '65')

SELECT id, company, salary
FROM (
    SELECT *,
        ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary, id) AS n,
        COUNT(*) OVER(PARTITION BY company) AS cnt
    FROM Employee
) t
WHERE n IN (cnt / 2, (cnt+1)/2, (cnt+2)/2)