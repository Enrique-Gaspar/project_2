import numpy as np
import datetime as dt

import sqlathanor
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Database Setup
Base = automap_base()
engine = create_engine("postgresql://postgres:postgres@localhost:5432/covid19")
Base.prepare(engine, reflect=True)
session = Session(engine)
covidData = Base.classes.covid19

@app.route("/")
def welcome():
    db_list = session.query(covidData).all()
    result = [d.__dict__ for d in db_list]
    for r in result:
        r.pop('_sa_instance_state')
    print (result)
    return jsonify(result=result)

@app.route("/inpatients_per_date")
def barchart():
    return render_template('inpatients_per_date.html')

@app.route("/deaths_per_date")
def barchart():
    return render_template('deaths_per_date.html')

@app.route("/subjects_per_state")
def barchart():
    return render_template('subjects_per_state.html')

if __name__ == '__main__':
    app.run(debug=True)