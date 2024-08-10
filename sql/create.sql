CREATE DATABASE airpollution;

\c airpollution

CREATE TABLE geographic (
    id SERIAL PRIMARY KEY,  
    location VARCHAR(255) NOT NULL, 
    altitude INTEGER NOT NULL,  
    proximity_to_industry DECIMAL(5, 2) NOT NULL  
);

CREATE TABLE demographic (
    id SERIAL PRIMARY KEY, 
    location VARCHAR(255) NOT NULL,  
    population INTEGER NOT NULL, 
    density DECIMAL(10, 2) NOT NULL,  
    urbanization DECIMAL(5, 2) NOT NULL, 
    average_income DECIMAL(10, 2) NOT NULL, 
    education_level DECIMAL(5, 2) NOT NULL
);

CREATE TABLE air_pollution (
    id SERIAL PRIMARY KEY,
    location VARCHAR(255),
    date TIMESTAMP,
    aqi INTEGER,
    co DECIMAL,
    no DECIMAL,
    no2 DECIMAL,
    o3 DECIMAL,
    so2 DECIMAL,
    pm2_5 DECIMAL,
    pm10 DECIMAL,
    nh3 DECIMAL,
    demographic_id INTEGER REFERENCES Demographic(id),
    geographic_id INTEGER REFERENCES Geographic(id)
);
