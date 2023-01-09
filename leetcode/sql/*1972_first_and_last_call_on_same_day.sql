Create table If Not Exists Calls (caller_id int, recipient_id int, call_time datetime)
Truncate table Calls
insert into Calls (caller_id, recipient_id, call_time) values ('8', '4', '2021-08-24 17:46:07')
insert into Calls (caller_id, recipient_id, call_time) values ('4', '8', '2021-08-24 19:57:13')
insert into Calls (caller_id, recipient_id, call_time) values ('5', '1', '2021-08-11 05:28:44')
insert into Calls (caller_id, recipient_id, call_time) values ('8', '3', '2021-08-17 04:04:15')
insert into Calls (caller_id, recipient_id, call_time) values ('11', '3', '2021-08-17 13:07:00')
insert into Calls (caller_id, recipient_id, call_time) values ('8', '11', '2021-08-17 22:22:22')

WITH cte AS (
    SELECT * FROM Calls
    UNION ALL
    SELECT recipient_id, caller_id, call_time FROM Calls
), cte2 AS (
    SELECT caller_id, recipient_id, call_time,
        DATE(call_time) AS day,
        RANK() OVER (PARTITION BY caller_id, DATE(call_time) ORDER BY call_time) AS rnk1,
        RANK() OVER (PARTITION BY caller_id, DATE(call_time) ORDER BY call_time DESC) AS rnk2
    FROM cte
)

SELECT DISTINCT caller_id AS user_id
FROM cte2
WHERE rnk1 = 1 OR rnk2 = 1
GROUP BY caller_id, day
HAVING COUNT(DISTINCT recipient_id) = 1