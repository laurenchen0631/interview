Create table If Not Exists Points (id int, x_value int, y_value int)
Truncate table Points
insert into Points (id, x_value, y_value) values ('1', '2', '7')
insert into Points (id, x_value, y_value) values ('2', '4', '8')
insert into Points (id, x_value, y_value) values ('3', '2', '10')


SELECT 
  a.id AS p1,
  b.id AS p2,
  (ABS(a.x_value - b.x_value) * ABS(a.y_value - b.y_value)) AS area
FROM Points a CROSS JOIN Points b
WHERE a.id < b.id AND a.x_value != b.x_value AND a.y_value != b.y_value 
ORDER BY area DESC, p1 ASC, p2 ASC