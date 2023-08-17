-- script that lists all the cities of database

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id;
