Create table If Not Exists Tree (id int, p_id int)
Truncate table Tree
insert into Tree (id, p_id) values ('1', 'None')
insert into Tree (id, p_id) values ('2', '1')
insert into Tree (id, p_id) values ('3', '1')
insert into Tree (id, p_id) values ('4', '2')
insert into Tree (id, p_id) values ('5', '2')

SELECT id, IF(p_id IS NULL, 'Root',
  IF(id IN (SELECT DISTINCT(p_id) FROM Tree), 'Inner', 'Leaf')) AS type
FROM Tree
ORDER BY id;

-- SELECT
--     id,
--     CASE
--         WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
--           THEN 'Root'
--         WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
--           THEN 'Inner'
--         ELSE 'Leaf'
--     END AS Type
-- FROM
--     tree
-- ORDER BY `Id`