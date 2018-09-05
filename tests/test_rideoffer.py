import json
from .base_test import BaseTestCase


class TestCreateRide(BaseTestCase):
    def test_request_ride(self):
        response = self.client.post(
            'api/v1/createride', data=self.riderequest_data)
        self.assertTrue(response.status_code == 201)

        data = json.loads(response.data)
        self.assertTrue(data == {"request created succesfully"})
        self.assertTrue(response.content_type='application/json')

    def test_request_ride_with_incomplete_details(self):
        response = self.client.post(
            'api/v1/create_ride', hearders=self.headers, data=self.incomplete_rideoffer)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(response.content_type='application/json')

    def test_create_ride_invalid_email(self):
        response = self.client.post(
            'api/v1/create_ride', headers=self.headers, data=self.invalid_email)
        self.assertTrue(response.status_code == 400)
        data = json.loads(reaponse.data)
        self.assertTrue(data, {'msg': 'created successfully'})

    def test_create_ride_invalid_date_format(self):
        response = self.client.post(
            'api/v1/create_ride', headers=self.headers, data=self.invalid_date_format)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data, {'msg': 'invalid date format (dd/mm/year H:MIN)'})

    def test_create_ride_invalid_token(self):
        response = self.client.post(
            'api/v1/create_ride', headers=self.invalid_token, data=self.invalid_date_format)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data, {'msg': 'invalid token'})

    def test_create_ride_no_token(self):
        response = self.client.post(
            'api/v1/create_ride', headers=self.no_token, data=self.invalid_date_format)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data, {'msg': 'invalid token'})

    def test_create_ride_with_empty_value(self):
        response = self.client.post(
            'api/v1/create_ride', headers=self.headers, data=self.invalid_date_format)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data, {'msg': 'please provide the missing value'})
    