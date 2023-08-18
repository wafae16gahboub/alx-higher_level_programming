-- a
USE hbtn_0d_usa;
DROP table cities,states;
use hbtn_0d_usa;
CREATE TABLE states(id INT auto_increment PRIMARY KEY, name VARCHAR(200));
INSERT INTO states(name) VALUE ('California'),
('Arizona'),
('Texas'),
('Utah');

CREATE TABLE cities(id INT , state_id INT , name VARCHAR(200),FOREIGN KEY (state_id) REFERENCES states(id));
INSERT INTO cities(id ,state_id, name) VALUE (1,1,'San Francisco'),
(2,1,'San Jose'),
(4,2,'Page'),
(6,3,'Paris'),
(7,3,'Houston'),
(8,3,'Dallas');
