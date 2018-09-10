import json
from flask_restplus import Resource, fields, Namespace
from .validators.validate_users import UserSchema

from .models.users import User


"""This module contains the authetication feature"""

autheticate = Namespace(
    "api", description="authentication related opperations")

registration_data = autheticate.model('Regestration', {
    "username": fields.String(description='username'),
    "password": fields.String(description='8 character long'),
    "email": fields.String(description='email'),
    "designation": fields.String(description='passager')})


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

        new_user = User(data['username'], data['email'],data['password'],data['designation'])
        
        user_exist = new_user.check_user(data['username'])
        email_exist = new_user.check_email(data['email'])
        if user_exist:
            user =user_exist[1]
            return {'message': f'username {user} already exist'}, 400

        if email_exist:
            email = email_exist[3]
            return {'message': f'{email} is already registered'}, 400
          
        new_user.register_user()

        return {'message': 'user successfully registered'}, 201