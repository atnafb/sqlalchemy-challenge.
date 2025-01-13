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


# Establishing route 
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
