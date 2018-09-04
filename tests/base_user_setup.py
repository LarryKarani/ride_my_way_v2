import sys
sys.path.append('../')
from unnittest import TestCase
from app.app import create_app
from app.models import db


class BaseUserAccount(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.conn = db.Db.db_connection()

        self.details_with_invalid_password = {
            "email": "karanilarry@gmail.com",
            "password": "hardpassword#"
        }
        self.user_not_exist = {
            "email": "karanilarry@gmail.com",
            "password": "hardpassword#"
        }

        self.data_with_invalid_email ={
            "username": "Larry Karani",
            "email": "karanilarrygmail.com",
            "password": "hardpass455#"
        }

        self.data_with_empty_password ={
            "username": "Larry Karani",
            "email": "karanilarry@gmail.com",
            "password": " "}

        self.data_with_short_password={
            "username": "Larry Karani",
            "email": "karanilarry@gmail.com",
            "password": "har"
        }
        def tearDown():
            """clean Db"""
            db.Db.drop_all_tables()
            self.client = None

        
