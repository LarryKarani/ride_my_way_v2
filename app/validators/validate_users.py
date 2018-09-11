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
    """Schema for validating login data"""
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


class RideSchema(Schema):
    start_point = fields.String(required=True)
    destination = fields.String(required=True)
    seats_available = fields.Integer(required=True)
    date = fields.String(required=True)
    time = fields.String(required=True)

    @validates("start_point")
    def validate_start_point(self,start_point):
        if start_point.strip == "":
            raise ValidationError("start point cannot be blank")
        elif len(start_point)<3:
            raise ValidationError("start point should be at least 3 characters long")

    @validates("destination")
    def validate_destination(self,destination):
        if destination.strip == "":
            raise ValidationError(" destination cannot be blank")
        elif len(destination)<3:
            raise ValidationError("destination should be at least 3 characters long")

    @validates("seats_available")
    def seats_available(self, seats_available):
        if seats_available<1:
            raise ValidationError(" seats_available cannot be less than one")