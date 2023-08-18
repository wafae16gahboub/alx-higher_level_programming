-- script that lists all the cities of California that
-- can be found in the database

use hbtn_0d_usa
SELECT id, name FROM cities where state_id = ( SELECT id FROM states WHERE name = '
California'); 
