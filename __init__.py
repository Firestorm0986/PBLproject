from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model_jokes import initJokes
from model_SATquiz import initSAT
from model_rankings import initRankings
from model_generaters import initfact

"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# Setup of key Flask object (app)
app = Flask(__name__)
# Setup SQLAlchemy object and properties for the database (db)
dbURI = 'sqlite:///volumes/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)

@app.before_first_request
def activate_job():
    initJokes()

@app.before_first_request
def activate_thing():
    initSAT()

@app.before_first_request
def activate_thing():
    initRankings()

@app.before_first_request
def activate_thing():
    initfact()