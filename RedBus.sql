use redbus_data;

-- CREATE TABLE Redbus_Data (
-- id INT AUTO_INCREMENT PRIMARY KEY,
-- state TEXT,
-- route_name TEXT,
-- route_link TEXT,
-- busname TEXT,
-- bustype TEXT,
-- departing_time TIME,
-- duration TEXT,
-- reaching_time TIME,
-- star_rating FLOAT,
-- price DECIMAL,
-- seats_available INT);

SHOW TABLES;

SELECT DATABASE();

SELECT * FROM bus_routes LIMIT 10;

DESCRIBE bus_routes;

SELECT COUNT(*) FROM bus_routes;
SELECT * FROM bus_routes;

SELECT * FROM bus_routes WHERE seats_available > 10;

SELECT * FROM bus_routes ORDER BY price DESC;

SELECT * FROM bus_routes WHERE star_ratings > 4;

SELECT * FROM bus_routes WHERE departing_time > '18:00:00';

SELECT route_name, COUNT(*) AS number_of_buses
FROM bus_routes
GROUP BY route_name;

SELECT * FROM bus_routes WHERE price BETWEEN 500 AND 1500;

SELECT * 
FROM bus_routes
WHERE route_name = 'APSRTC';

-- Check available buses for a specific route:
SELECT busname, bustype, departing_time, duration, reaching_time, star_ratings, price, seats_available
FROM bus_routes
WHERE route_name = 'Hyderabad to Vijayawada'
  AND seats_available > 0;


-- List the highest-rated buses for a specific route:
SELECT busname, route_name, bustype, star_ratings
FROM bus_routes
WHERE route_name = 'Kerala to Bangalore'
ORDER BY star_ratings DESC
LIMIT 5;

-- Find buses with fast travel durations for a route:
SELECT busname, route_name, duration, price, star_ratings
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore'
ORDER BY duration ASC
LIMIT 5;

-- Check the number of routes available:
SELECT route_name, COUNT(DISTINCT route_name) AS total_routes 
FROM bus_routes
GROUP BY route_name
ORDER BY total_routes DESC;

-- Find buses arriving at or before a specific time:
SELECT busname, route_name, departing_time, reaching_time, price 
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore' 
  AND reaching_time <= '06:00';
  
-- Find buses with no seats available:
SELECT busname, route_name, bustype, seats_available
FROM bus_routes
WHERE route_name = 'Kozhikode to Bangalore' 
AND seats_available > 2;

-- List all available buses for a specific bustype:
SELECT busname, route_name, departing_time, duration, price, seats_available 
FROM bus_routes
WHERE bustype = 'Rajdhani (AC Semi Sleeper 2+2)'
  AND seats_available > 0;

SELECT DISTINCT route_name FROM bus_routes;

-- Buses between two cities 
SELECT * FROM bus_routes WHERE Route_Name LIKE '%Goa%' AND Route_Name LIKE '%Mumbai%';

-- Buses by departure time and route name
SELECT * 
FROM bus_routes
WHERE Departing_Time >= '18:00:00' AND Departing_Time <= '23:59:59'
and route_name = 'Hyderabad to vijayawada';

-- Buses by seat availability
SELECT * 
FROM bus_routes
WHERE seats_available > 0
and route_name='Hyderabad to vijayawada'
and bustype like '%Super Luxury%';

-- Price filter from low to high
SELECT * 
FROM bus_routes
WHERE seats_available > 0
ORDER BY Price ASC;

-- buses by bus type
SELECT * 
FROM bus_routes
WHERE BusType LIKE '%Sleeper%'
  OR BusType LIKE '%AC%';

SELECT * 
FROM bus_routes
WHERE Route_Name LIKE '%Goa%' AND Route_Name LIKE '%Mumbai%'
  AND BusType LIKE '%AC%'
  AND seats_available > 0
  AND Price BETWEEN 1000 AND 2000
ORDER BY Price ASC;

select distinct Route_Name from bus_routes where state='assam';
