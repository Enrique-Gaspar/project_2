import numpy as np
import datetime as dt

import sqlathanor
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
Base = automap_base()
engine = create_engine("postgresql://postgres:postgres@localhost:5433/henrigaspard") 
Base.prepare(engine, reflect=True)
session = Session(engine)
covidData = Base.classes 
#print (engine.table_names())

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

if __name__ == '__main__':
    app.run(debug=True)

