Create table If Not Exists Product (product_id int, product_name varchar(30))
Create table If Not Exists Sales (product_id int, period_start date, period_end date, average_daily_sales int)
Truncate table Product
insert into Product (product_id, product_name) values ('1', 'LC Phone ')
insert into Product (product_id, product_name) values ('2', 'LC T-Shirt')
insert into Product (product_id, product_name) values ('3', 'LC Keychain')
Truncate table Sales
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('1', '2019-01-25', '2019-02-28', '100')
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('2', '2018-12-01', '2020-01-01', '10')
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('3', '2019-12-01', '2020-01-31', '1')

WITH RECURSIVE cte AS (
    SELECT MIN(period_start) as date FROM Sales
    UNION
    SELECT DATE_ADD(date, INTERVAL 1 DAY)
    FROM cte
    WHERE date <= (SELECT MAX(period_end) FROM Sales)
)

SELECT product_id, product_name, YEAR(date) as report_year, SUM(average_daily_sales) as total_amount
FROM Product p
    JOIN Sales s USING (product_id)
    JOIN cte ON date BETWEEN period_start AND period_end
GROUP BY product_id, YEAR(date)
ORDER BY product_id, YEAR(date)