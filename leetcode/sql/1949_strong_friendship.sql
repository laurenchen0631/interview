Create table If Not Exists Friendship (user1_id int, user2_id int)
Truncate table Friendship
insert into Friendship (user1_id, user2_id) values ('1', '2')
insert into Friendship (user1_id, user2_id) values ('1', '3')
insert into Friendship (user1_id, user2_id) values ('2', '3')
insert into Friendship (user1_id, user2_id) values ('1', '4')
insert into Friendship (user1_id, user2_id) values ('2', '4')
insert into Friendship (user1_id, user2_id) values ('1', '5')
insert into Friendship (user1_id, user2_id) values ('2', '5')
insert into Friendship (user1_id, user2_id) values ('1', '7')
insert into Friendship (user1_id, user2_id) values ('3', '7')
insert into Friendship (user1_id, user2_id) values ('1', '6')
insert into Friendship (user1_id, user2_id) values ('3', '6')
insert into Friendship (user1_id, user2_id) values ('2', '6')

With AllFriends As (
    Select user1_id, user2_id From Friendship
    Union All
    Select user2_id, user1_id From Friendship
)

SELECT a.user1_id AS user1_id, b.user1_id AS user2_id, COUNT(*) as common_friend
FROM AllFriends a JOIN AllFriends b
    ON a.user1_id < b.user1_id AND a.user2_id = b.user2_id
WHERE (a.user1_id, b.user1_id) IN (SELECT user1_id, user2_id FROM Friendship)
GROUP BY a.user1_id, b.user1_id
HAVING COUNT(*) >= 3