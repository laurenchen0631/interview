Create Table If Not Exists Point (x int not null)
Truncate table Point
insert into Point (x) values ('-1')
insert into Point (x) values ('0')
insert into Point (x) values ('2')

SELECT ABS(a.x - b.x) AS shortest
FROM Point AS a JOIN Point b ON a.x < b.x