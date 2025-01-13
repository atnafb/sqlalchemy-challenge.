# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, request
# Creating the flask app
app = Flask(__name__)
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# Establishing home route 
@app.route("/")
def home():
    return (
        # This block generates HTML content for the home page of the Flask application.
        # It includes clickable links for the API routes and a form to input start and end dates for temperature analysis.

        f"<center><h3><u>This is a Climate Analysis Local API for Hawaii</u></h3></center>"
        f"<center><h4>Click the below routes:</h4></center>"

        f"<center><a href='/api/v1.0/precipitation'>Precipitation API Route</a></center><br>"
        f"<center><a href='/api/v1.0/stations'>List of Stations API Route</a></center><br>"
        f"<center><a href='/api/v1.0/tobs'>Observed Temperature and Dates API Route</a></center><br>"
        f"<center><h4>Enter Start and End Dates for Temperature Analysis:</h4></center>"
        # NOTE: The inpute can be performed from the URL using this 
        # methode http://127.0.0.1:5000/api/v1.0/start_end?start=2025-01-06&end=2025-01-15
        # only change the numeric start date and end date with YYYY-MM-DD format 

        # for user freindly eqperiance follow a form is avialble to interact with 
        # Creating a form to enter a desired dates to diplay the Min, Max, and Avg Temperature
        # Form starts, it will send data to '/api/v1.0/start_end'
        f"<form action='/api/v1.0/start_end' method='GET' style='text-align: center;'>"

        # Input for the start date. This a required field
        f"Start Date: <input type='date' name='start' placeholder='YYYY-MM-DD' required><br><br>"

        # Inpute the end date. an optional field 
        f"End Date: <input type='date' name='end' placeholder='YYYY-MM-DD'><br><br>"
        f"<input type='submit' value='Get Temperature Data'>"
        f"</form>"
    )

# Precipitation API Route
@app.route("/api/v1.0/precipitation")
def precip(): 
    # Calculate the date one year from the last date in data set.
    previous_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    data_preci_score = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= previous_year_date).\
        all()
    session.close()
    # dictionary with the date as the key and the precipitation (pre) as the value
    Precipitation = {date: prcp for date, prcp in data_preci_score} 

    # converting to JSONs
    return jsonify(Precipitation)


# Stations Route 
@app.route("/api/v1.0/stations")
def station():
    # Show a list of station 
    #query to retrieve the names of the stations 

    stationList = session.query(Station.station).all()
    session.close()

    ravelStationList = list(np.ravel(stationList))
    # converting to JSONs >> this will siplay the 9 staitons in JSON format 
    return jsonify(ravelStationList)

# API route for dates and temperature observations of the most-active station for the previous year of data

@app.route("/api/v1.0/tobs")
def tobs(): 
    # the prvious year tempreture from the last date in the data set
    previous_year_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # a query to retrieve the tempratures from the most active satation from the previou year 
    Last12tobs = session.query(Measurement.tobs, Measurement.date).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previous_year_date).all()
    session.close()

    temp_list = list (np.ravel(Last12tobs))

    # disply jusonify list of tempreture 
    return jsonify(temp_list)


# The SON list of the minimum temperature, the average temperature, and the maximum temperature 
# for a specified start or start-end range.
@app.route("/api/v1.0/start_end")
def dateStates():
    # request.args.get() gets the value associated with the key ('start' or 'end') in the URL query string
    # request is imported from flask
    # Get the start date from the URL query parameters
    start = request.args.get('start')
    # Get the end date from the URL query parameters
    end = request.args.get('end')

    # Validate the start date
    if not start:
        # this messaging appear if a suer is using a URL to inpute dates and missing a starting date
        # the URL looks like this for mac users: http://127.0.0.1:5000/api/v1.0/start_end?start=2025-01-06&end=2025-01-15
        return jsonify({"error": "Please provide a start date in the format YYYY-MM-DD"}), 400

    # Extract the min, max, and average temperatures
    TempFunc = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    if not end:
        startDate = dt.datetime.strptime(start, "%Y-%m-%d")
        dateResult = session.query(*TempFunc).filter(Measurement.date >= startDate).all()
    else:
        startDate = dt.datetime.strptime(start, "%Y-%m-%d")
        endDate = dt.datetime.strptime(end, "%Y-%m-%d")
        dateResult = session.query(*TempFunc).filter(Measurement.date >= startDate).filter(Measurement.date <= endDate).all()

    session.close()

    # Convert query result to a list and return JSON response
    temp_list = list(np.ravel(dateResult))
    return jsonify(temp_list)




# app louncher 
if __name__ == '__main__':
    app.run(debug=True)
