Create table If Not Exists Relations (user_id int, follower_id int)
Truncate table Relations
insert into Relations (user_id, follower_id) values ('1', '3')
insert into Relations (user_id, follower_id) values ('2', '3')
insert into Relations (user_id, follower_id) values ('7', '3')
insert into Relations (user_id, follower_id) values ('1', '4')
insert into Relations (user_id, follower_id) values ('2', '4')
insert into Relations (user_id, follower_id) values ('7', '4')
insert into Relations (user_id, follower_id) values ('1', '5')
insert into Relations (user_id, follower_id) values ('2', '6')
insert into Relations (user_id, follower_id) values ('7', '5')


SELECT user1_id, user2_id
FROM (
    SELECT a.user_id AS user1_id, b.user_id as user2_id, RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM Relations a
        JOIN Relations b ON a.follower_id = b.follower_id AND a.user_id < b.user_id
    GROUP BY a.user_id, b.user_id) a
WHERE rnk = 1