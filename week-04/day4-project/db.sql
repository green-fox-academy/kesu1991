create table reaction(
    id INT,
    user_id VARCHAR(50),
    message_id VARCHAR(200),
    reaction VARCHAR(50)                     
);

 id |  user_id  |              message_id              |    reaction
----+-----------+--------------------------------------+----------------
  1 | UB1ATRBQV | 2e3e16f0-928e-4ad9-b28a-3a29f1f2f01d | smile
  2 | U93GXHPA7 | 5c9fc5fd-2317-4048-9d62-f83c469436ce | green_heart
  3 | UB1ATRBQV | 9123ae9b-3159-4eb2-a47f-8092cdff765c | champagne
  4 | UB1ATRBQV | 9123ae9b-3159-4eb2-a47f-8092cdff765c | dancing_banana
  5 | UB1ATRBQV | 9123ae9b-3159-4eb2-a47f-8092cdff765c | clap
  6 | U0AA4Q8LS | 5f277707-199f-42a4-9e97-52e0add7802d | metal
  7 | U0AA4Q8LS | 5f277707-199f-42a4-9e97-52e0add7802d | eyes
  8 | U0AA4Q8LS | 2306b817-ecfc-4c3c-9110-683ebefc497d | green_heart
  9 | U0AA4Q8LS | 2306b817-ecfc-4c3c-9110-683ebefc497d | metal
 10 | U95512YE6 | f97531e8-f76d-4dd5-a6f0-bfbc20115f0a | heart

SELECT user_id, count(reaction)
FROM reaction
GROUP BY user_id
ORDER BY count(reaction) DESC
LIMIT 5;

SELECT count(reaction)
FROM reaction
GROUP BY reaction
ORDER BY count(reaction) DESC
LIMIT 5;
