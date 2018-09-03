   """ This module contains the login and rester feature """ 
import re


class Validator():
    """Validates the input data"""
    def __init__(self , obj, prop):
        self.has_numbers = re.compile('[0-9]')
        self.has_special = re.compile('[^\w\s]')
        self.ride_offer_props = ['ride_owner', 'ride_route', 'price','depature_time', 
                                'current_location', 'final_destination','available_seats']
                                
        self.ride_request_props = [' requested_by' , 'phone',  'ride_offer_id',
                                   'current_location', 'final_destination']

        self.regester_user_props = ['username', 'password', 'email', 'designation' ]
        self.login_props = ["username", "password"]
        self.prop = prop

    def empty_prop(self, props):
        for prop in props:
            if prop not in self.obj or self.obj.prop.strip() == "":
                return {"message":f"please provide {prop}"}

    def invalid_email(self):
        #check email if valid
        pass
    
    def has_numbers(self):
        #check if data containts numbers
        pass
    