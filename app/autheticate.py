   """ This module contains the login and rester feature """ 
import re


class BaseValidator():
    def __init__():
        self.has_numbers = re.compile('[0-9]')
        self.has_special = re.compile('[^\w\s]')

    def empty_prop(self, props):
        for prop in props:
            if prop not in self.obj or self.obj.prop.strip() == "":
                return {"message":f"please provide {prop}"}
    def has_numbers

        
    

class RideValidator(BaseValidator):
    """This class contains validators for offer and request a ride  inputs"""
    def __init__(self, obj, prop):
        self.ride_offer_props = ['ride_owner', 'ride_route', 'price','depature_time', 
                                'current_location', 'final_destination','available_seats']

        self.ride_request_props = [' requested_by' , 'phone',  'ride_offer_id',
                                   'current_location', 'final_destination']
        self.prop = prop