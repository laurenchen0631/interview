Create table If Not Exists Customers (customer_id int, name varchar(10))
Create table If Not Exists Orders (order_id int, order_date date, customer_id int, product_id int)
Create table If Not Exists Products (product_id int, product_name varchar(20), price int)
Truncate table Customers
insert into Customers (customer_id, name) values ('1', 'Winston')
insert into Customers (customer_id, name) values ('2', 'Jonathan')
insert into Customers (customer_id, name) values ('3', 'Annabelle')
insert into Customers (customer_id, name) values ('4', 'Marwan')
insert into Customers (customer_id, name) values ('5', 'Khaled')
Truncate table Orders
insert into Orders (order_id, order_date, customer_id, product_id) values ('1', '2020-07-31', '1', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('2', '2020-7-30', '2', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('3', '2020-08-29', '3', '3')
insert into Orders (order_id, order_date, customer_id, product_id) values ('4', '2020-07-29', '4', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('5', '2020-06-10', '1', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('6', '2020-08-01', '2', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('7', '2020-08-01', '3', '1')
insert into Orders (order_id, order_date, customer_id, product_id) values ('8', '2020-08-03', '1', '2')
insert into Orders (order_id, order_date, customer_id, product_id) values ('9', '2020-08-07', '2', '3')
insert into Orders (order_id, order_date, customer_id, product_id) values ('10', '2020-07-15', '1', '2')
Truncate table Products
insert into Products (product_id, product_name, price) values ('1', 'keyboard', '120')
insert into Products (product_id, product_name, price) values ('2', 'mouse', '80')
insert into Products (product_id, product_name, price) values ('3', 'screen', '600')
insert into Products (product_id, product_name, price) values ('4', 'hard disk', '450')

SELECT product_name, o.product_id, order_id, order_date
FROM Orders o JOIN Products p
  ON o.product_id = p.product_id
WHERE (o.product_id, order_date) IN (
  SELECT product_id, MAX(order_date)
  FROM Orders
  GROUP BY product_id )
ORDER BY product_name ASC, o.product_id ASC, order_id ASC
