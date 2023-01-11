Create table If Not Exists Failed (fail_date date)
Create table If Not Exists Succeeded (success_date date)
Truncate table Failed
insert into Failed (fail_date) values ('2018-12-28')
insert into Failed (fail_date) values ('2018-12-29')
insert into Failed (fail_date) values ('2019-01-04')
insert into Failed (fail_date) values ('2019-01-05')
Truncate table Succeeded
insert into Succeeded (success_date) values ('2018-12-30')
insert into Succeeded (success_date) values ('2018-12-31')
insert into Succeeded (success_date) values ('2019-01-01')
insert into Succeeded (success_date) values ('2019-01-02')
insert into Succeeded (success_date) values ('2019-01-03')
insert into Succeeded (success_date) values ('2019-01-06')

WITH cte AS (
    SELECT fail_date AS date, 'failed' as status, RANK() OVER(ORDER BY fail_date) AS rk
    FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION
    SELECT success_date AS date, 'succeeded' as status, RANK() OVER(ORDER BY success_date) AS rk
    FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
)

SELECT status as period_state, MIN(date) As start_date, MAX(date) AS end_date
FROM (
    SELECT *, (RANK() OVER(ORDER BY date) - rk) AS inv
    FROM cte
) t
GROUP BY inv, status
ORDER BY start_date