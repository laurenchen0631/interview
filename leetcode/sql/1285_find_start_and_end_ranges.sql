SELECT MIN(log_id) as start_id, MAX(log_id) as end_id
FROM (
    SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) as num
    FROM Logs) a
GROUP BY log_id - num