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
        f"<center><h4>Select from one of the available routes:</h4></center>"
        f"<center><a href='http://127.0.0.1:5000/api/v1.0/precipitation'>Precipitation API Route</a></center><br>"
        f"<center><a href='http://127.0.0.1:5000/api/v1.0/stations'>List of Stations API Route</a></center><br>"
        f"<center><a href='http://127.0.0.1:5000/api/v1.0/tobs'>Observed Temperature and Dates API Route</a></center><br>"
        f"<center><a href='http://127.0.0.1:5000/api/v1.0/<start>/<end>'>Min, Max, and Avg Temperature API Route</a></center>"
    )

# Precipitation API Rout
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
    Precipitaitons = {date: prcp for date, prcp in data_preci_score} 

    # converting to JSONs
    return jsonify(Precipitaitons)





# app louncher 
if __name__ == '__main__':
    app.run(debug=True)


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
