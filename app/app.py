import psycopg2
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api

from config import config
from .autheticate import autheticate as autheticate_api
from .ride_offer import rideoffer as rideoffer_api

# authentication manager


def create_app(config_name):
    #app factory create the instance of the app
    app = Flask(__name__)
    jwt = JWTManager(app)
    api = Api(
        app=app, 
        description="""a carpooling application that allows users to  create and join ride offers""",
        title="Ride my way",
        version="2",
        license="MIT",
        contact ='karanilarry@gmail.com')

    api.add_namespace(autheticate_api)
    api.add_namespace(rideoffer_api)
    app.config.from_object(config[config_name])

    return app
