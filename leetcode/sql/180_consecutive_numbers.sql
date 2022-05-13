Create table If Not Exists Logs (id int, num int)
Truncate table Logs
insert into Logs (id, num) values ('1', '1')
insert into Logs (id, num) values ('2', '1')
insert into Logs (id, num) values ('3', '1')
insert into Logs (id, num) values ('4', '2')
insert into Logs (id, num) values ('5', '1')
insert into Logs (id, num) values ('6', '2')
insert into Logs (id, num) values ('7', '2')

SELECT DISTINCT num AS ConsecutiveNums
FROM Logs a
WHERE EXISTS (
  SELECT * FROM Logs b
  WHERE a.id+1 = b.id and a.num = b.num
) AND EXISTS (
  SELECT * FROM Logs b
  WHERE a.id+2 = b.id and a.num = b.num
)