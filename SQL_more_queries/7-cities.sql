-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
-- create the database hbtn_0d_usa, should not fail if it does not already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table cities inside htbn_0d_usa, should not fail is already exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	-- id INT unique, auto generated, can't be null and is a primary key
	id INT AUTO_INCREMENT NOT NULL,
	-- state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table
	state_id INT NOT NULL, 
	-- name VARCHAR(256) can't be null
	name VARCHAR(256),
	-- primary of the id
	PRIMARY KEY (id),
	-- foreign key referencing to id of the states table
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);

