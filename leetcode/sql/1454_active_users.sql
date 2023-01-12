Create table If Not Exists Accounts (id int, name varchar(10))
Create table If Not Exists Logins (id int, login_date date)
Truncate table Accounts
insert into Accounts (id, name) values ('1', 'Winston')
insert into Accounts (id, name) values ('7', 'Jonathan')
Truncate table Logins
insert into Logins (id, login_date) values ('7', '2020-05-30')
insert into Logins (id, login_date) values ('1', '2020-05-30')
insert into Logins (id, login_date) values ('7', '2020-05-31')
insert into Logins (id, login_date) values ('7', '2020-06-01')
insert into Logins (id, login_date) values ('7', '2020-06-02')
insert into Logins (id, login_date) values ('7', '2020-06-02')
insert into Logins (id, login_date) values ('7', '2020-06-03')
insert into Logins (id, login_date) values ('1', '2020-06-07')
insert into Logins (id, login_date) values ('7', '2020-06-10')

WITH distinct_login AS (
    SELECT DISTINCT id, login_date
    FROM Logins
), cte AS (
    SELECT *, RANK() OVER(PARTITION BY id ORDER BY login_date) AS rnk
    FROM distinct_login
)
SELECT DISTINCT id, name
FROM cte JOIN Accounts USING (id) 
GROUP BY id, DATE_ADD(login_date, interval -rnk DAY)
HAVING COUNT(*) >= 5
ORDER BY id