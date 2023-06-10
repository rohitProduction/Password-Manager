Create your own database and insert config detail in the db.py to connect to it.
Also create the tables. I used these statements to create the tables:

CREATE TABLE users (
	username VARCHAR(255) PRIMARY KEY,
	hashedPassword VARCHAR(255) NOT NULL,
	salt VARCHAR(255) NOT NULL
);
CREATE TABLE websites (
	website VARCHAR(255) PRIMARY KEY,
    usersUsername VARCHAR(255) REFERENCES users (username),
	encryptedPassword VARCHAR(255) NOT NULL
);
 
Run gui.py file to execute application