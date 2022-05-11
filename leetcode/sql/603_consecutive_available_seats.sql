Create table If Not Exists Cinema (seat_id int primary key auto_increment, free bool)
Truncate table Cinema
insert into Cinema (seat_id, free) values ('1', '1')
insert into Cinema (seat_id, free) values ('2', '0')
insert into Cinema (seat_id, free) values ('3', '1')
insert into Cinema (seat_id, free) values ('4', '1')
insert into Cinema (seat_id, free) values ('5', '1')

SELECT seat_id
FROM Cinema a
WHERE free = 1 AND EXISTS (
  SELECT * 
  FROM Cinema b
  WHERE (a.seat_id-1 = b.seat_id and b.free=1) OR (a.seat_id+1 = b.seat_id and b.free=1)
)