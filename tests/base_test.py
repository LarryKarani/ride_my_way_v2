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
            "password": "hardpassword#"
        }

        self.registerdata_no_username = {
            "username": " ",
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

        self.wrong_request = {
            "requested_by": "jacob",
            "phone": "0701043047",
            "ride_offer_id": 1,
            "depature_time": "12/45/2018 12:30",
            "current_location": "railways",
            "final_destination": "  ",
        }
        self.wrong_date_request = {
            "requested_by": "jacob",
            "phone": "0701043047",
            "ride_offer_id": 1,
            "depature_time": "12452018 12:30",
            "current_location": "railways",
            "final_destination": "kigali",
        }
        self.wrong_ride = {

            "ride_owner": "mary",
            "ride_route": "mombasa road",
            "price": "$56",
            "depature_time": "12/45/2018 12:30",
            "current_location": "railways",
            "final_destination": "syokimau",
            "available_seats": 'twenty'
        }

        self.wride_with_wrong_date = {
            "ride_owner": "mary",
            "ride_route": "mombasa road",
            "price": "$56",
            "depature_time": "12/45/2018 12:30",
            "current_location": "railways",
            "final_destination": "syokimau",
            "available_seats": 4
        }

        self.request_invalid_id = {
            "requested_by": "jacob",
            "phone": "0701043047",
            "ride_offer_id": 50,
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
        self.default_user.register_user()
        # login details
        self.login = {
            "email": "james@gmail.com"
            "password": "hardpassword#"
        }

        response = self.client.post('api/v1/auth/login', data=self.login)
        self.token = json.loads(response.data)["token"]
        self.headers = {
            'Authorization': 'Bearer' + self.token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.invalid_token = {
            'Authorization': 'Bearer' + self.token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def tearDown():
        """clean Db"""
        db.Db.drop_all_tables()
        self.client = None
