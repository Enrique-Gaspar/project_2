import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup

engine = create_engine("postgresql://admin:postgress@localhost:5432/covid19")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Flask Setup
app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
