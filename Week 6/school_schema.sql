DROP DATABASE IF EXISTS assigmentdb;
CREATE DATABASE IF NOT EXISTS assignmentdb;
USE assignmentdb;
CREATE TABLE IF NOT EXISTS exhibits (
	id INT NOT NULL PRIMARY KEY, 
	name VARCHAR(40) NOT NULL, 
	start_date DATE NOT NULL, 
	end_date DATE NOT NULL,
	curator_id INT NOT NULL,
);

CREATE TABLE IF NOT EXISTS curators (
	id INT NOT NULL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	bio TEXT NOT NULL
);

INSERT OR IGNORE INTO exhibits VALUES ("3","Free The Fishes","2018-01-01","2018-06-30","5")
INSERT OR IGNORE INTO exhibits VALUES ("17","Space, What Lies Above","2018-02-01","2018-05-30","11")
INSERT OR IGNORE INTO exhibits VALUES ("23","Bears Bears Bears","2018-02-14","2018-02-24","5")
INSERT OR IGNORE INTO exhibits VALUES ("46","Humans? Aliens?","2019-03-14","2019-10-21","11")

INSERT OR IGNORE INTO curators VALUES ("5","Rebecca Votea","Esteemed naturalist")
INSERT OR IGNORE INTO curators VALUES ("11","Simon Strauss","Space man")
INSERT OR IGNORE INTO curators VALUES ("71","Rick Sanchez","Grandfather")

