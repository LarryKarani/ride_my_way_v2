from unittest import TestCase

from app.app import create_app
from app.models import request, ride_offer, users, db


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.conn = db.Db.db_connection()

        db.Db.drop_all_tables()
        db.Db.create_tables()

        self.client = self.app.test_client()

        self.registerdata = {
            "username": "Larry Karani",
            "email": "karanilarry@gmail.com",
            "password": "hardpassword#",
            "designation": 'driver'
        }
        self.data_with_invalid_email = {
            "username": "Larry Karani",
            "email": "karani.com",
            "password": "hardpassword#",
            "designation": 'driver'
        }
        self.registerdata_no_username = {
            "username": " ",
            "email": "karanilarry@gmail.com",
            "password": "hardpassword#",
            "designation": "driver"
        }

        self.short_password = {
            "username": "elvis ",
            "email": "karanilarry@gmail.com",
            "password": "hard",
            "designation": "driver"
        }

        self.wrong_designation = {
            "username": "elvis",
            "email": "karanilarry@gmail.com",
            "password": "hard33333444",
            "designation": "pilot"
        }

        self.login_data = {
            "username": "Larry Karani",
            "password": "hardpassword#"
        }
        self.wrong_password = {
            "username": "Larry Karani",
            "password": "hardpass777#"
        }

        self.empty_username = {
            "username": " ",
            "password": "hardpass777#"
        }

        self.empty_password = {
            "username": "kapiyo ",
            "password": " "
        }

        self.default_user = users.User(
            'james', 'hardpassword#', 'james@gmail.com', 'driver')
        self.default_user.register_user()

    def tearDown(self):
        """clean Db"""
        db.Db.drop_all_tables()
        self.client = None
