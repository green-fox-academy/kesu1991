--! set up the enviorment
cqlsh> DESCRIBE keyspaces;
system_traces  system_schema  system_auth  system  system_distributed

source 'load-timeseries.cql';

COPY raw_weather_data (wsid, year, month, day, hour, temperature, dewpoint, pressure, wind_direction, wind_speed, sky_condition, one_hour_precip, six_hour_precip)
FROM 'C:\Users\Ke_Su\greenfox\kesu1991\week-05\day02-cassandra\2014.csv';






--! Questions station ID 724940:23234

--! Q1 Where is this weather station?
SELECT * FROM weather_station WHERE id = '724940:23234';

 id           | call_sign | country_code | elevation | lat    | long   | name                  | state_code
--------------+-----------+--------------+-----------+--------+--------+-----------------------+------------
 724940:23234 |      KSFO |           US |       2.4 | 37.617 | -122.4 | SAN FRANCISCO INTL AP |         CA


 --! Q2 Show the temperature for June 1st, 2008.
 SELECT temperature 
 FROM raw_weather_data 
 WHERE wsid = '724940:23234'
 AND year = 2008
 AND month = 6
 AND day = 1;

  temperature
-------------
          15
          15
        15.6
          15
          15
        14.4
        13.3
        12.2
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1
           0
        11.7
        11.7
        11.7
        11.7
        11.7
        12.2
        12.8
        13.3

(24 rows)


--! Q3 Show the temperatures for June 1st, 2008 from 9AM to 3PM.
SELECT temperature 
FROM raw_weather_data 
WHERE wsid = '724940:23234'
AND year = 2008
AND month = 6
AND day = 1
AND hour IN (9,10,11,12,13,14,15);

 temperature
-------------
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1

(7 rows)


--! Q4 What is the average elevation of the weather stations in Indiana?
SELECT state_code, avg(elevation) 
FROM weather_station 
WHERE id = '724940:23234'
AND state_code = 'IA'
ALLOW FILTERING;

 name | system.avg(elevation)
------+-----------------------
 null |                     0





