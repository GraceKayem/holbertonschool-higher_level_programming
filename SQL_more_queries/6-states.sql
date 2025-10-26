-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- id INT unique, auto generated, can't be null and is a primary key
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	-- id INT unique, auto generated, can't be null and is a primary key
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	-- name VARCHAR(256) can't be null
	name VARCHAR(256) NOT NULL,
	-- make the id a primary key
	PRIMARY KEY (id)
);

