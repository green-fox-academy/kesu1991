/* SQL Movie-Rating Query Exercises */

/* 
Q1
Find the titles of all movies directed by Steven Spielberg. 
*/
SELECT title
FROM Movie
WHERE director = 'Steven Spielberg';

Query Result: 
E.T.
Raiders of the Lost Ark


/* 
Q2 
Find all years that have a movie that received a rating of 4 or 5, 
and sort them in increasing order. 
*/
SELECT DISTINCT year 
FROM Movie
LEFT JOIN Rating
ON Movie.mID = Rating.mID
WHERE Rating.stars >= 4;

Query Result: 
1937
1939
1981
2009


/* 
Q3 
Find the titles of all movies that have no ratings. 
*/
SELECT Movie.title
FROM Movie
LEFT JOIN Rating
ON Movie.mID = Rating.mID
WHERE Rating.mID is NULL;

Query Result: 
Star Wars
Titanic


/* 
Q4
Some reviewers didn't provide a date with their rating.
Find the names of all reviewers who have ratings with a NULL value 
for the date. 
*/
SELECT Reviewer.name
FROM Reviewer
LEFT JOIN Rating
ON Reviewer.rID = Rating.rID
WHERE Rating.ratingDate is NULL;

Query Result: 
Chris Jackson
Daniel Lewis


/* 
Q5
Write a query to return the ratings data in a more readable format: 
reviewer name, movie title, stars, and ratingDate. Also, sort the data, 
first by reviewer name, then by movie title, and lastly by number of stars.
*/
SELECT Reviewer.name, Movie.title, Rating.stars, Rating.ratingDate
FROM Rating
LEFT JOIN Reviewer
ON Reviewer.rID = Rating.rID
LEFT JOIN Movie
ON Movie.mID = Rating.mID
ORDER BY Reviewer.name, Movie.title, Rating.stars;







/* SQL Movie-Rating Query Exercises Extras*/

/* 
Q1
Find the names of all reviewers who rated Gone with the Wind. 
*/
SELECT DISTINCT Reviewer.name
FROM Rating
LEFT JOIN Reviewer
ON Reviewer.rID = Rating.rID
LEFT JOIN Movie
ON Movie.mID = Rating.mID
WHERE Movie.title = 'Gone with the Wind'
ORDER BY Reviewer.name;

Query Result: 
Mike Anderson
Sarah Martinez


/* 
Q2
For any rating where the reviewer is the same as the director of the movie,
return the reviewer name, movie title, and number of stars.  
*/
SELECT DISTINCT Reviewer.name, Movie.title, Rating.stars
FROM Rating
LEFT JOIN Reviewer
ON Reviewer.rID = Rating.rID
LEFT JOIN Movie
ON Movie.mID = Rating.mID
WHERE Reviewer.name = Movie.director
ORDER BY Reviewer.name;

Expected Query Result: 
James Cameron Avatar 5







/* Joins and Subqueries */

/*
Retrieve the start times of members' bookings
*/
SELECT starttime 
FROM cd.bookings
JOIN cd.members
ON cd.bookings.memid = cd.members.memid
WHERE cd.members.surname = 'Farrell'
AND cd.members.firstname = 'David'


/*
Work out the start times of bookings for tennis courts
*/
SELECT bks.starttime as start, facl.name as name
FROM cd.facilities facl
JOIN cd.bookings bks
ON facl.facid = bks.facid
WHERE facl.name LIKE 'Tennis%'
AND bks.starttime >= '2012-09-21' 
AND bks.starttime < '2012-09-22'
ORDER BY bks.starttime;


/*
Produce a list of all members who have recommended another member 
*/
SELECT DISTINCT membs1.firstname as firstname, membs1.surname as surname
FROM cd.members membs
INNER JOIN cd.members membs1
ON membs1.memid = membs.recommendedby
ORDER BY surname, firstname;


/*
Produce a list of all members who have used a tennis court 
*/
SELECT DISTINCT membs.firstname || ' ' || membs.surname as member, facs.name as facility
FROM cd.members membs
INNER JOIN cd.bookings bks 
ON membs.memid = bks.memid
INNER JOIN cd.facilities facl
ON bks.facid = facl.facid
WHERE facl.name LIKE 'Tennis%'
order by member;





