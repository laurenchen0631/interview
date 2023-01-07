Create table If Not Exists UserActivity (username varchar(30), activity varchar(30), startDate date, endDate date)
Truncate table UserActivity
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-12', '2020-02-20')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Dancing', '2020-02-21', '2020-02-23')
insert into UserActivity (username, activity, startDate, endDate) values ('Alice', 'Travel', '2020-02-24', '2020-02-28')
insert into UserActivity (username, activity, startDate, endDate) values ('Bob', 'Travel', '2020-02-11', '2020-02-18')

SELECT username, activity, startDate, endDate
FROM (
    SELECT *,
        RANK() OVER (PARTITION BY username ORDER BY startDate DESC) AS rnk,
        COUNT(*) OVER (PARTITION BY username) AS cnt
    FROM UserActivity
) t
WHERE cnt = 1 OR rnk = 2
