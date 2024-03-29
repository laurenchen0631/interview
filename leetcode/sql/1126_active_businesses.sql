Create table If Not Exists Events (business_id int, event_type varchar(10), occurences int)
Truncate table Events
insert into Events (business_id, event_type, occurences) values ('1', 'reviews', '7')
insert into Events (business_id, event_type, occurences) values ('3', 'reviews', '3')
insert into Events (business_id, event_type, occurences) values ('1', 'ads', '11')
insert into Events (business_id, event_type, occurences) values ('2', 'ads', '7')
insert into Events (business_id, event_type, occurences) values ('3', 'ads', '6')
insert into Events (business_id, event_type, occurences) values ('1', 'page views', '3')
insert into Events (business_id, event_type, occurences) values ('2', 'page views', '12')

SELECT business_id
FROM (
    SELECT *, AVG(occurences) OVER(PARTITION BY event_type) AS avg_occurrences
    FROm Events
) a
WHERE occurences > avg_occurrences
GROUP BY business_id
HAVING COUNT(*) >= 2