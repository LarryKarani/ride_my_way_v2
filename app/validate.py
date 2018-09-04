""" This module contains the login and rester feature """
import re


class Validator():
    """Validates the input data"""

    def __init__(self, obj, prop):
        self.prop = prop
        self.obj = obj
        self.has_numbers = re.compile('[0-9]')
        self.has_special = re.compile('[^\w\s]')
        self.ride_offer_props = ['ride_owner', 'ride_route', 'price', 'depature_time',
                                 'current_location', 'final_destination', 'available_seats']

        self.ride_request_props = [' requested_by', 'phone',  'ride_offer_id',
                                   'current_location', 'final_destination']

        self.regester_user_props = ['username',
                                    'password', 'email', 'designation']
        self.login_props = ["username", "password"]

    def valid_email(self):
        return re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", self.obj.email)

    def has_numbers(self, input):
        return self.has_numbers.search(self.obj.input)

    def empty_prop(self, props):
        for prop in props:
            if prop not in self.obj or self.obj.prop.strip() == "":
                return {"message": f"please provide {prop}"}

    def valid_date_format(self):
        return re.search(
            "^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$", self.obj.depature_time)

    def password_len(self):
        return len(self.obj.password) >= 8
