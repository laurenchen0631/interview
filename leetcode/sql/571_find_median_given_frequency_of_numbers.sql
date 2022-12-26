Create table If Not Exists Numbers (num int, frequency int)
Truncate table Numbers
insert into Numbers (num, frequency) values ('0', '7')
insert into Numbers (num, frequency) values ('1', '1')
insert into Numbers (num, frequency) values ('2', '3')
insert into Numbers (num, frequency) values ('3', '1')

SELECT ROUND(AVG(n.num), 1) AS median
FROM Numbers n
WHERE n.frequency >= ABS(
    (SELECT SUM(n2.frequency) FROM Numbers n2 WHERE n2.num <= n.num) -
    (SELECT SUM(n2.frequency) FROM Numbers n2 WHERE n2.num >= n.num)
)