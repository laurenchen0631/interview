Create table If Not Exists Seat (id int, student varchar(255))
Truncate table Seat
insert into Seat (id, student) values ('1', 'Abbot')
insert into Seat (id, student) values ('2', 'Doris')
insert into Seat (id, student) values ('3', 'Emerson')
insert into Seat (id, student) values ('4', 'Green')
insert into Seat (id, student) values ('5', 'Jeames')

SELECT
  (CASE 
    WHEN MOD(id, 2) = 1 AND count != id THEN id+1
    WHEN MOD(id, 2) = 1 AND count = id THEN id
    ELSE id-1
  ) AS id,
  student
FROM
  Seat,
  (SELECT COUNT(*) AS count FROM Seat) c
ORDER BY id
