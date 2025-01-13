# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify
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
        f"<center><h3><u>This is a Climate Analysis Local API for Hawaii</u></h3></center>"
        f"<center><h4>Click the below routes:</h4></center>"
        f"<center><a href='/api/v1.0/precipitation'>Precipitation API Route</a></center><br>"
        f"<center><a href='/api/v1.0/stations'>List of Stations API Route</a></center><br>"
        f"<center><a href='/api/v1.0/tobs'>Observed Temperature and Dates API Route</a></center><br>"
        f"<center><a href='/api/v1.0/start/end'>Min, Max, and Avg Temperature API Route</a></center>"
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


# app louncher 
if __name__ == '__main__':
    app.run(debug=True)
