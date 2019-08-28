import os

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///output_data/gdpChange.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
gdp_table = Base.classes.gdp_table


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/barchart/<state>/<state2>")//flask_route//
def barchart(state,state2):
    """Return the MetaData for a given sample."""
    sel = [
        gdp_table.Quarter,
        gdp_table.State,
        gdp_table.GDP_Change,
        
    ]

    results = db.session.query(*sel).filter(gdp_table.State == state).all()

    results2 = db.session.query(*sel).filter(gdp_table.State == state2).all()

     # Create a dictionary entry for each row of metadata information
    state_results = {}
    for result in results:
        state_results["Quarter"] = result[0]
        state_results["State"] = result[1]
        state_results["GDP_Change"] = result[2]

    for result in results2:
        state_results["Quarter2"] = result[0]
        state_results["State2"] = result[1]
        state_results["GDP_Change2"] = result[2]
       

    print(state_results)
    return jsonify(state_results)

if __name__ == "__main__":
    app.run()
