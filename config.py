import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '@#$%^&*'


class DevelopmentConfig(Config):
    DEBUG = True

    Database = {
        'password':  os.environ.get('db_password'),
        'user':  'postgres',
        'database': 'Drive',
        'host':  'localhost'
    }


class TestingConfig(Config):
    Testing = True
    DEBUG = True
    Database = {

        'password':  os.environ.get('db_password'),
        'database':  os.environ.get('testing_db'),
        'host':  'localhost',
        'user':  'postgres'
    }


class ProductionConfig(Config):

    Database = {

        'PASSWORD':  os.environ.get('db_password'),
        'database':  os.environ.get('production_db'),
        'user':  'postgres',
        'host':  'localhost'
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
