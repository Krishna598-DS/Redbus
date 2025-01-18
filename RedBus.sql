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

SELECT * 
FROM bus_routes
WHERE state = 'Andhra Pradesh';

-- Check available buses for a specific state and route:
SELECT busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available 
FROM bus_routes
WHERE state = 'Andhra Pradesh' 
  AND route_name = 'Hyderabad to Vijayawada'
  AND seats_available > 0;

-- Find the cheapest bus for a specific route:
SELECT busname, bustype, price, seats_available 
FROM bus_routes
WHERE route_name = 'Hyderabad to Vijayawada'
ORDER BY price ASC
LIMIT 1;


-- List the highest-rated buses for a specific state:
SELECT busname, route_name, bustype, star_rating 
FROM bus_routes
WHERE state = 'Kerala'
ORDER BY star_rating DESC
LIMIT 5;

--  Find buses with fast travel durations for a route:
SELECT busname, route_name, duration, price, star_rating 
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore'
ORDER BY duration ASC
LIMIT 5;

-- Check the number of routes available in each state:
SELECT state, COUNT(DISTINCT route_name) AS total_routes 
FROM bus_routes
GROUP BY state
ORDER BY total_routes DESC;

-- Find buses arriving at or before a specific time:
SELECT busname, route_name, departing_time, reaching_time, price 
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore' 
  AND reaching_time <= '06:00';
  
--   Find buses with no seats available:
SELECT busname, route_name, state, bustype 
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore' 
AND seats_available = 5;

--  List all available buses for a specific bustype in a state:
SELECT busname, route_name, departing_time, duration, price, seats_available 
FROM bus_routes
WHERE state = 'Telangana' 
  AND bustype = 'Rajdhani (AC Semi Sleeper 2+2)'
  AND seats_available > 0;
