Create table If Not Exists Triangle (x int, y int, z int)
Truncate table Triangle
insert into Triangle (x, y, z) values ('13', '15', '30')
insert into Triangle (x, y, z) values ('10', '20', '15')

SELECT *, IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS Triangle
FROM Tri