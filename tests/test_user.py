import json
from .base_test import BaseTestCase


class TestRegesterUser(BaseTestCase):
    def test_user_register(self):
        response = self.client.post('api/auth/v1/register', data=json.dumps(
            self.registerdata), content_type='application/json')
        self.assertTrue(json.loads(response.data) == {
                        "message": "user successfully registered"})
        self.assertTrue(response.status_code == 201)

    def test_register_empty_username(self):
        response = self.client.post('api/auth/v1/register', data=json.dumps(
            self.registerdata_no_username), content_type='application/json')
        self.assertTrue(json.loads(response.data) == {
                        "message": "username cannot be empty"})
        self.assertTrue(response.status_code == 400)

    def test_user_invalid_email(self):
        response = self.client.post('api/auth/v1/register', data=json.dumps(
            self.data_with_invalid_email), content_type='application/json')
        self.assertTrue(json.loads(response.data) == {
                        "message": "Not a valid email address."})
        self.assertTrue(response.status_code == 400)

    def test_user_short_Password(self):
        response = self.client.post('api/auth/v1/register', data=json.dumps(
            self.short_password), content_type='application/json')
        self.assertTrue(json.loads(response.data) == {
                        "message": "password should be atlist 8 characters long"})
        self.assertTrue(response.status_code == 400)

    def test_wrong_designation(self):
        response = self.client.post('api/auth/v1/register', data=json.dumps(
            self.wrong_designation), content_type='application/json')
        self.assertTrue(json.loads(response.data) == {
                        "message": "designation can only be driver or passenger"})
        self.assertTrue(response.status_code == 400)

    def test_register_user_twice(self):
        default_user = {"username": "james",
                        "password": "hardpassword#",
                        "email": "james@gmail.com",
                        "designation": "driver"}
        response = self.client.post(
            'api/auth/v1/register', data=json.dumps(default_user), content_type='application/json')
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(
            data == {"message": "username james already exist"})

    def test_register_email_twice(self):
        default_user = {"username": "pinto",
                        "password": "hardpassword#",
                        "email": "james@gmail.com",
                        "designation": "driver"}

        new_user =  {    "username": "octo",
                        "password": "hardpassword#",
                        "email": "james@gmail.com",
                        "designation": "driver"}

        self.client.post(
            'api/auth/v1/register', data=json.dumps(default_user), content_type='application/json')
        response = self.client.post(
            'api/auth/v1/register', data=json.dumps(new_user), content_type='application/json')
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        print(json.loads(response.data))
        self.assertTrue(
            data == {"message": "james@gmail.com is already registered"})
