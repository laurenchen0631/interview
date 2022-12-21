Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
Truncate table Activity
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6')
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '3', '2017-06-25', '1')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0')
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5')

-- SELECT a.player_id, a.event_date, (
--     SELECT SUM(games_played)
--     FROM Activity b
--     WHERE b.player_id = a.player_id AND b.event_date <= a.event_date
-- ) AS games_played_so_far
-- FROM Activity a;


SELECT a.player_id, a.event_date, SUM(a.games_played) OVER (PARTITION BY a.player_id ORDER BY a.event_date) AS games_played_so_far
FROm Activity a;