import numpy as np
import datetime as dt

import sqlathanor
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

# Database Setup
Base = automap_base()
engine = create_engine("postgresql://postgres:postgres@localhost:5433/henrigaspard")
Base.prepare(engine, reflect=True)
session = Session(engine)
covidData = Base.classes

# Flask Setup
app = Flask(__name__)

@app.route("/")
def welcome():
    db_list = session.query(covidData).all()
    result = [d.__dict__ for d in db_list]
    for r in result:
        r.pop('_sa_instance_state')
    print (result)
    return jsonify(result=result)

@app.route("/home")
def main():
    return render_template('main.html')

@app.route("/inpatients_per_date")
def graphinpatients():
    return render_template('inpatients_per_date.html')

@app.route("/deaths_per_date")
def graphdeaths():
    return render_template('deaths_per_date.html')

@app.route("/subjects_per_state")
def mexicomap():
    return render_template('subjects_per_state.html')

if __name__ == '__main__':
    app.run(debug=True)