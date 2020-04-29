import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup

Base = automap_base()
engine = create_engine("postgresql://postgres:postgres@localhost:5432/covid19")
Base.prepare(engine, reflect=True)
session = Session(engine)
covidData = Base.classes.covid19
#print (engine.table_names())

# Flask Setup
app = Flask(__name__)

@app.route("/")
def welcome():
    
    return (session, covidData)


if __name__ == '__main__':
    app.run(debug=True)
