Create table If Not Exists Players (player_id int, player_name varchar(20))
Create table If Not Exists Championships (year int, Wimbledon int, Fr_open int, US_open int, Au_open int)
Truncate table Players
insert into Players (player_id, player_name) values ('1', 'Nadal')
insert into Players (player_id, player_name) values ('2', 'Federer')
insert into Players (player_id, player_name) values ('3', 'Novak')
Truncate table Championships
insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2018', '1', '1', '1', '1')
insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2019', '1', '1', '2', '2')
insert into Championships (year, Wimbledon, Fr_open, US_open, Au_open) values ('2020', '2', '1', '2', '2')

SELECT
  player_id,
  player_name,
  (SUM(player_id=Wimbledon) + SUM(player_id=Fr_open) + SUM(player_id=US_open) +  SUM(player_id=Au_open)) AS grand_slams_count
FROM Players p JOIN Championships
ON player_id = Wimbledon OR
  player_id = Fr_open OR
  player_id = US_open OR
  player_id = Au_open
GROUP BY player_id;
