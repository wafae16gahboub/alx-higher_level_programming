-- script that creates the database hbtn_0d_usa and the table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.cities(id), name VARCHAR(256) NOT NULL);
