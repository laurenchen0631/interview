Create table If Not Exists Customers (customer_id int, customer_name varchar(20))
Truncate table Customers
insert into Customers (customer_id, customer_name) values ('1', 'Alice')
insert into Customers (customer_id, customer_name) values ('4', 'Bob')
insert into Customers (customer_id, customer_name) values ('5', 'Charlie')

WITH RECURSIVE cte AS (
    SELECT 1 AS id
    UNION ALL
    SELECT id + 1 FROM cte WHERE id < (SELECT MAX(customer_id) FROM Customers)
)

SELECT id AS ids
FROM cte
WHERE id NOT IN (SELECT customer_id FROM Customers)
