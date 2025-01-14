# Hawaii Climate Analysis API

This repository contains the **Hawaii Climate Analysis API**, a Flask-based web application that provides an easy-to-use interface to access climate data for Hawaii. The API exposes several endpoints for analyzing different types of climate data, including precipitation, weather station information, and temperature observations. The app is designed to help users explore historical climate data and retrieve insights such as daily precipitation, station data, and temperature trends over a specified range of dates.

Additionally, users can manually input the start and end dates for temperature analysis directly via the URL or use the provided web form to get temperature data for a specific range.

## Project Structure

- **`app.py`**: Contains the Flask web application and routes for the API. This file includes the logic for querying the database, handling HTTP requests, and returning JSON responses.
    ** Important!! `import request from flask` to access the date selection form  
    - **Imports in `app.py`**:
    ```python
    import datetime as dt
    import numpy as np
    import pandas as pd
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine, func
    from flask import Flask, jsonify, request
    ```

- **`climate_starter.ipynb`**: Contains exploratory analysis of precipitation and weather stations. This Jupyter notebook includes visualizations, such as graphs showing precipitation trends and temperature histograms.

- **`Hawaii.sqlite`**: An SQLite database that contains the Hawaii climate data, which is used to populate the API routes.


- **`precipitation_analysis.png`**: Image file containing the graph of precipitation data for the past year, generated by the analysis.

- **`temperature_histogram.png`**: Image file containing a histogram of temperature observations from the most active weather station.

- **`homepage.png`**: Screenshot of the homepage of the Hawaii Climate Analysis API, which displays the available routes and forms for interacting with the data.

## API Routes

### 1. **Precipitation Data API (`/api/v1.0/precipitation`)**
   - **Description**: Displays daily precipitation data for the past year.
###2 **Weather Station API (`/api/v1.0/stations`)**
   - **Description**: Lists all available weather stations in Hawaii
### 3. ** Temperature Observations `/api/v1.0/tobs`)**
   - **Description**: Displays temperature observations for the most active weather station.
### 3. ** A date form to Get Temperature Data `/api/v1.0/start_end`)**



## Tools used: 
-	Python
-	Visual Studio Code
-	Jupyter Notebook
-	Terminal 

![image](https://github.com/user-attachments/assets/ce357fdd-1282-4910-b341-d6a177578b87)
