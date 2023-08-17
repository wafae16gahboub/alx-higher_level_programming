-- a
use hbtn_0d_usa;
DROP table cities,states;
use hbtn_0d_usa
CREATE TABLE states(name VARCHAR(200), id INT auto_increment PRIMARY KEY);
INSERT INTO states(name) VALUE ('California'),
('Arizona'),
('Texas'),
('blarj'),
('Utah');

CREATE TABLE cities(id INT auto_increment PRIMARY KEY, state_id INT , name VARCHAR(200),FOREIGN KEY (state_id) REFERENCES states(id));
INSERT INTO cities(state_id, name) VALUE(1,'San Francisco'),
(1,'San JosePage'),
(3,'Paris'),
(2,'Page'),
(4,'Houston'),
(3,'Dallas');
