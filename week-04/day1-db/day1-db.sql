/* List the users who registered in 2018 with a .com email address and living in China? */
SELECT * FROM users 
WHERE EXTRACT(year FROM "date_of_registration") = 2018
AND country LIKE 'China'
AND email LIKE '%.com';

 id |  username   |          email           | date_of_registration | first_name | last_name | country | gender
----+-------------+--------------------------+----------------------+------------+-----------+---------+--------
  2 | dcrampsy1   | dcrampsy1@artisteer.com  | 2018-11-08           | Daveen     | Crampsy   | China   | Female
 21 | bsurgenork  | bsurgenork@typepad.com   | 2018-12-07           | Bebe       | Surgenor  | China   | Female
 46 | cdrissell19 | cdrissell19@springer.com | 2018-06-08           | Costanza   | Drissell  | China   |
 76 | eturnbull23 | eturnbull23@wikia.com    | 2018-07-21           | Ely        | Turnbull  | China   | Male
 83 | mlampen2a   | mlampen2a@globo.com      | 2018-12-01           | Matelda    | Lampen    | China   | Female

/* How many users are there? */
SELECT count(id) as number_of_users
FROM users;

 number_of_users
-----------------
             100
(1 row)

/* How many users registered in 2019? */
SELECT count(id) as number_of_users
FROM users
WHERE EXTRACT(year FROM "date_of_registration") = 2019;

number_of_users
-----------------
              42
(1 row)

/* How many users registered in January? */
SELECT count(id) as number_of_users
FROM users
WHERE EXTRACT(month FROM "date_of_registration") = 01;

 number_of_users
-----------------
               4
(1 row)

/* Which country has the most users? */
SELECT country, count(id) as number_of_users
FROM users
GROUP BY country
ORDER BY number_of_users DESC
LIMIT 1;

 country | number_of_users
---------+-----------------
 China   |              17
(1 row)

/* What is the gender ratio? */
SELECT (SELECT count(gender) FROM users WHERE gender = 'Female') as num_female,
       (SELECT count(gender) FROM users WHERE gender = 'Male') as num_male,
       (SELECT count(gender) FROM users) as total       
FROM users
LIMIT 1;

num_female | num_male | total
------------+----------+-------
         55 |       40 |    95
(1 row)

/* How many users left at least one field blank? */
SELECT count(id) as number_of_users
FROM users
WHERE email IS NULL 
OR date_of_registration IS NULL
OR first_name IS NULL
OR last_name IS NULL
OR country IS NULL
OR gender IS NULL;

 number_of_users
-----------------
              11
(1 row)

/* Which are the 3 most expensive products? */
SELECT id, name, category, price FROM products 
ORDER BY price DESC
LIMIT 3;

 id |      name      |  category   |  price
----+----------------+-------------+----------
 17 | vestibulum ac  | Home        | 149.4001
 97 | ipsum praesent | Fashion     | 148.3893
 23 | vestibulum     | Electronics | 147.0537
(3 rows)

/* Which are the 4th and 5th cheapest products? */
SELECT id, name, category, price FROM products
ORDER BY price ASC
LIMIT 2 OFFSET 3; 

 id |         name         |  category   | price
----+----------------------+-------------+--------
 70 | pede lobortis ligula | Electronics | 4.5345
 47 | neque aenean auctor  | Other       | 4.6891
(2 rows)

/* What is the average price for an electric product? */
SELECT round(avg(price),2) as average_electronics_price
FROM products
WHERE category = 'Electronics';

 average_electronics_price
---------------------------
                     76.17
(1 row)

/* How much would it cost me to buy all the toys? */
SELECT round(sum(price),2) as total_price
FROM products;

total_price
-------------
     7932.67
(1 row)

/* What is the average rating? */
SELECT round(avg(rating),2) as average_rating
FROM reviews;

 average_rating
----------------
           3.09
(1 row)

/* Which product has the best average rating? */
SELECT product_id, round(avg(rating),2) as average_rating
FROM reviews
GROUP BY product_id
HAVING round(avg(rating),2) = (SELECT max(average_rating) FROM (SELECT round(avg(rating),2) as average_rating FROM reviews GROUP BY product_id) AS max_query);

 product_id | average_rating
------------+----------------
         56 |           5.00
         29 |           5.00
         41 |           5.00
         78 |           5.00
         18 |           5.00
(5 rows)

/* Which product has the worst rating? */
SELECT product_id, round(avg(rating),2) as average_rating
FROM reviews
GROUP BY product_id
HAVING round(avg(rating),2) = (SELECT min(average_rating) FROM (SELECT round(avg(rating),2) as average_rating FROM reviews GROUP BY product_id) AS min_query);

 product_id | average_rating
------------+----------------
         27 |           1.00
         83 |           1.00
          2 |           1.00
         98 |           1.00
         88 |           1.00
(5 rows)

/* Which products have no review(no comments at all)? */
SELECT reviews.product_id, products.name, products.category, count(comment) as num_of_comment 
FROM reviews, products
WHERE products.id = reviews.product_id
GROUP BY reviews.product_id, products.name, products.category
HAVING count(comment) = 0;

 product_id |          name          |  category   | num_of_comment
------------+------------------------+-------------+----------------
         57 | a suscipit nulla       | Home        |              0
         62 | phasellus id           | Home        |              0
         41 | erat eros              | Other       |              0
         24 | vel pede               | Fashion     |              0
         95 | proin                  | Toys        |              0
         29 | nulla pede ullamcorper | Fashion     |              0
         78 | lobortis est           | Toys        |              0
         45 | quis odio              | Electronics |              0
         56 | mi                     | Fashion     |              0
         27 | sed justo pellentesque | Other       |              0
         53 | ipsum primis           | Home        |              0
         98 | venenatis turpis       | Art         |              0
(12 rows)

/* Which user reviewed the most? */
SELECT user_id, users.username, count(product_id)
FROM reviews, users
GROUP BY user_id, users.username
ORDER BY count(product_id) DESC
LIMIT 1;

user_id | username  | count
---------+-----------+-------
      81 | kwalpoleu |     7
(1 row)

/* List the average rating for each product */
SELECT product_id, Round(avg(rating),2) as average_rating
FROM reviews
GROUP BY product_id
ORDER BY product_id
LIMIT 5;

 product_id | average_rating
------------+----------------
          1 |           4.33
          2 |           1.00
          3 |           2.75
          4 |           2.50
          5 |           3.67
(5 rows)


/* How many days passed since the last review? */
select date_part('day',age('2019-05-27', (SELECT date 
FROM reviews
ORDER BY date DESC
LIMIT 1)));

 date_part
-----------
         3
(1 row)
