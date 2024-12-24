CREATE TABLE bus_routes (
id INT AUTO_INCREMENT PRIMARY KEY,
state TEXT,
route_name TEXT,
route_link TEXT,
busname TEXT,
bustype TEXT,
departing_time TIME,
duration TEXT,
reaching_time TIME,
star_rating FLOAT,
price DECIMAL,
seats_available INT);

SHOW TABLES;

SELECT * FROM bus_routes LIMIT 10;

DESCRIBE bus_routes;

SELECT COUNT(*) FROM bus_routes;

SELECT * FROM bus_routes;

SELECT route_name, price FROM bus_routes;

SELECT * FROM bus_routes WHERE state = 'Goa';

SELECT * FROM bus_routes WHERE seats_available > 10;

SELECT * FROM bus_routes ORDER BY price DESC;

SELECT * FROM bus_routes WHERE star_rating > 4;

SELECT * FROM bus_routes WHERE departing_time > '18:00:00';

SELECT state, COUNT(*) AS number_of_buses
FROM bus_routes
GROUP BY state;

SELECT * FROM bus_routes WHERE price BETWEEN 500 AND 1500;








