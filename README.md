# Dataset Generation with LoPy + Pysense. 
An example dataset generation via Pycom modules.

## Features

- Contains **timestamp**, **temperature**, **humidity**, and **power consumption** data in order.
- Environment is 25 m2 studio room contains 2 people.
- Data might be considered as normal, there are no anomalies created on purpose. 

## My Observations Regarding Sensor Qualities

- The temperature and humidity values are pretty accurate.
- The real time is fetch from https://www.pool.ntp.org/zone/uk. 
- The data is generated with floating points, hence useful for machine learning purposes.
- The module cannot save data for 24 hours. It does generate an error after around 18 hours. While I was not able to locate the exact reason (the error messages are too generic, hence most of the time pretty useless.) My only guess is, it due to dropping WiFi connection.
