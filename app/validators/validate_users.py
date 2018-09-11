from marshmallow import Schema, fields,  validates, ValidationError


class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    designation = fields.String(required=True)

    @validates('password')
    def validates_password(self, password):
        if password.strip() == '':
            raise ValidationError('password cannot be empty')
        elif len(password) < 8:
            raise ValidationError(
                'password should be atlist 8 characters long')

    @validates('designation')
    def validates_designation(self, designation):
        if (designation != 'driver') and (designation != 'passenger'):
            raise ValidationError(
                'designation can only be driver or passenger')

        elif designation.strip() == '':
            raise ValidationError('designation cannot be empty')

    @validates('username')
    def validates_username(self, username):
        if username.strip() == '':
            raise ValidationError('username cannot be empty')

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    @validates('username')
    def validates_username(self, username):
        if username.strip() == '':
            raise ValidationError('username cannot be empty')

    @validates('password')
    def validates_password(self, password):
        if password.strip() == '':
            raise ValidationError('password cannot be empty')