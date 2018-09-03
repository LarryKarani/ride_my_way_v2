import os
from app.app import create_app
from app.models.db import Db

environment = os.getenv('config_name')
app = create_app(environment)
#creates database tables if they don't exist
Db.create_tables()

if __name__ == '__main__':
    app.run()