import json
from .base_test_setup import BaseTestCase


class TestRegesterUser(BaseTestCase):
    def test_user_regester(self):
        response = self.client.post('api/v1/register', data=self.regesterdata)
        self.assertTrue(response.status_code == 200)
        data = json.loads(response.data)
        self.assertTrue(data == {"msg": "user created succesfully"})

    def test_user_invalid_email(self):
        response = self.client.post(
            'api/v1/register', data=self.data_with_invalid_email)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(data == {"msg": "please provide a valid email"})

    def test_user_short_Password(self):
        response = self.client.post(
            'api/v1/register', data=self.data_with_short_password)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data == {"msg": "password should be a minimum of 8 charaters"})

    def test_user_with_empty_password(self):
        response = self.client.post(
            'api/v1/register', data=self.data_with_empty_password)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data == {"msg": "please provide password"})

    def test_regester_user_twice(self):
        default_user = {"name": "james",
                        "password": "hardpassword#",
                        "email": "james@gmail.com"}
        response = self.client.post(
            'api/v1/register', data=self.data_with_empty_password)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data == {"msg": "user already registered"})

    def test_user_with_invalid_username(self):
        response = self.client.post(
            'api/v1/register', data=self.registerdata_no_username)
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data == {"msg": "please provide a valid username"})
