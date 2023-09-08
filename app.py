# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base  # Import automap_base

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#################################################


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect the tables

# Save references to each table
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app = Flask(__name__)
#################################################




#################################################
# Flask Routes
if __name__ == "__main__":
    app.run(debug=True)
#################################################
