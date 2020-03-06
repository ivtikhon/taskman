from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, LOGGING_CONFIG
import logging
import logging.handlers
from logging.config import dictConfig

# Configure logging
dictConfig(LOGGING_CONFIG)

# Create app and db objects
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import routing
import views

@app.before_first_request
def create_tables():
    db.create_all()
