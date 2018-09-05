import json
import flask

from.base_test import BaseTestCase


class TestLogin(BaseTestCase):
    def test_user_login(self):
        response = self.client.post('api/auth/v1/login', data=self.login)
        self.assertTrue(response.status_code == 200)
        data = json.loads(response.data)
        self.assertTrue(response.content_type == "application/json")
        self.assertTrue(data == {"msg": "login succesfull"})

    def test_user_wrong_password(self):
        response = self.client.post(
            'api/auth/v1/login', data=dict(email="karanilarry@gmail.com", password="234password"))
        self.assertTrue(response.status_code == 400)
        data = json.loads(response.data)
        self.assertTrue(response.content_type == "application/json")

     def test_user_invalid_email(self):
            response = self.client.post(
            'api/auth/v1/login', data=dict(email="karanilarry@gmail.com", password="234password"))
        self.assertTrue(response.status_code==400)
        data = json.loads(response.data)
        self.assertTrue(response.content_type == "application/json")

    def test_empty_credetials(self):
        response = self.client.post(
            'api/auth/v1/login', data=dict())
        self.assertTrue(response.status_code==400)
        data = json.loads(response.data)
        self.assertTrue(response.content_type == "application/json")
    def test_wrong_login_url(self):
        response = self.client.post("/auth/login", data=dict(email="karanilarry@gmail.com", password="password#"))
        self.assertTrue(response.status_code == 404)

    def test_login_nonexisting_user(self):
        response = self.client.post('api/auth/v1/login', data=(
            email="unregestered@gmail.com", password="n1hhyeye667"
        ))
        self.assertTrue(response.status_code==401)
        data = json.loads(response.data)
        self.assertTrue(response.conten_type=="application/json")
      
