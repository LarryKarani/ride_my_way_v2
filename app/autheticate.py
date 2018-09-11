import json
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import create_access_token
from .validators.validate_users import UserSchema, LoginSchema
from werkzeug.security import check_password_hash

from .models.users import User


"""This module contains the authetication feature"""

autheticate = Namespace(
    "api", description="authentication related opperations")

registration_data = autheticate.model('Regestration', {
    "username": fields.String(description='username'),
    "password": fields.String(description='8 character long'),
    "email": fields.String(description='email'),
    "designation": fields.String(description='passager')})

Login_data = autheticate.model('Login', {
    'username': fields.String(description='username'),
    'password': fields.String(description='password')
})


@autheticate.route('/auth/v1/register')
class Register(Resource):
    @autheticate.doc('list users')
    def get(self):
        all_users = User.get_all_usesrs()

        return all_users

    @autheticate.expect(registration_data)
    def post(self):
        data = autheticate.payload
        schema = UserSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['username', 'email', 'password', 'designation']
        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400

        new_user = User(data['username'], data['email'],
                        data['password'], data['designation'])

        user_exist = new_user.check_user(data['username'])
        email_exist = new_user.check_email(data['email'])
        if user_exist:
            user = user_exist[1]
            return {'message': f'username {user} already exist'}, 400

        if email_exist:
            email = email_exist[3]
            return {'message': f'{email} is already registered'}, 400

        new_user.register_user()

        return {'message': 'user successfully registered'}, 201


@autheticate.route('/auth/v1/login')
class Login(Resource):
    """Logs in a user"""
    @autheticate.expect(Login_data)
    def post(self):
        data = autheticate.payload
        schema = LoginSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['username', 'password']

        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400

        current_user = User.check_user(data['username'])

        if not current_user:
            return {'message': f'username does not exist'}, 400

        # remember to use hashed password
        if not check_password_hash(current_user[2] , data['password'].strip()):
            print(current_user[2])
            return {'message': f'invalid username or password'}, 400

        access_token = create_access_token(identity=data['username'])

        return {'message': 'logged in as {}'.format(data['username']),
                'access_token': access_token}, 200
