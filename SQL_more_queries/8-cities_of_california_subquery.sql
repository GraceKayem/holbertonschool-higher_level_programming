-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
-- The states table contains only one record where name = California (but the id can be different, as per the example)

-- selecting id and name columns from the cities table
SELECT * FROM cities
-- include whose state_id matches one of the IDs
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
-- Results must be sorted in ascending order by cities.id
ORDER BY id ASC;

