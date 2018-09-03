import psycopg2
from flask import Flask
from config import config
def create_app(config_name):
    """returns the configured app and the db connection to postgres"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
   
    

    return app

      