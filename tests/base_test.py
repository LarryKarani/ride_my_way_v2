from unittest import TestCase

from app.app import create_app
from app.models import request, ride_offer, users, db


class BaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.conn = db.Db.db_connection()

        db.Db.drop_all_tables()
        db.Db.create_tables()

        self.registerdata = {
            "username": "Larry Karani",
            "email": "karanilarry@gmail.com",
            "password": "hardpassword#"
        }
        self.rideoffer_data = {
            "ride_owner": "mary",
            "ride_route": "mombasa road",
            "price": "$56",
            "depature_time": "12/45/2018 12:30",
            "current_location": "railways",
            "final_destination": "syokimau",
            "available_seats": 6
        }
        self.riderequest_data = {
            "requested_by": "jacob",
            "phone": "0701043047",
            "ride_offer_id": 1,
            "depature_time": "12/45/2018 12:30",
            "current_location": "railways",
            "final_destination": "syokimau",
        }
        self.default_ride_request = ride_offer.RideOffer(
            'james', '0701043047', 1, "12/45/2018 12:30", "mbagathi", "juja", 8)
        self.default_ride_offer = ride_offer.RideOffer(
            'james', 'jogoo road', "$50", "12/45/2018 12:30", "mbagathi", "juja")
        self.default_user = users.User(
            'james', 'hardpassword#', 'james@gmail.com')
        self.login = {
            "email": "james@gmail.com"
            "password": "hardpassword#"
        }
        self.default_user.register_user()
        self.client = self.app.test_client()

    def tearDown():
        db.Db.drop_all_tables()
