-- Write a script that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use db
USE hbtn_0d_usa;
-- Create tables
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL UNIQUE, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
