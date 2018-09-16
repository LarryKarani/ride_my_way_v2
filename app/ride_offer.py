import json
from flask import request
from flask_restplus import Resource, fields, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

from .validators.validate_ride import RideSchema
from .models.ride_offer import RideOffer

"""This module contains the ride offer feature"""


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}


rideoffer = Namespace(
    'Ride', description='ride offer related opperations', path='/api/v1/rides', authorizations=authorizations, security='apikey'
)

ride_data = rideoffer.model(
    'RideOffer', {
        'route': fields.String(description='route taken'),
        'price': fields.String(description='cost of the ride'),
        'departure': fields.String(description='departure time'),
        'location': fields.String(description='current location'),
        'destination': fields.String(description='current location'),
        'seats': fields.Integer(description='the availabe seats on the ride'),
    }
)


keys = ['owner', 'id', 'route', 'price', 'departure',
                'location', 'destination', 'seats', 'date_created']


@rideoffer.header("Authorization", "Access tokken", required=True)
@rideoffer.route('/', endpoint='rides')
class Rides(Resource):
    @rideoffer.expect(ride_data)
    @rideoffer.doc(security='apikey')
    @jwt_required
    def post(self):
        data = rideoffer.payload
        schema = RideSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['route', 'price', 'depature',
                       'location', 'destination', 'seats']

        # check if there's any error in the errors dict
        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400

        current_user = get_jwt_identity()

        new_ride = RideOffer(current_user, data['route'], data['price'],
                             data['departure'], data['location'], data['destination'], data['seats'])

        new_ride.create_ride()

        return {'message': 'ride offer created successfully'}

    @rideoffer.doc('list all rides', security='apikey')
    @jwt_required
    def get(self):

        result = RideOffer.get_all_ride_offers()

        if not result:
            return {'message': 'no ride offer available'}
        output = []

        for values in result:
            output.append(dict(zip(keys, values)))

        return output, 200


@rideoffer.header("Authorization", "Access tokken", required=True)
@rideoffer.route('/<int:ride_id>', endpoint='ride_opperations')
class Rides(Resource):
    @rideoffer.doc('single ride', security='apikey')
    @jwt_required
    def get(self, ride_id):

        results = RideOffer.get_a_ride_offer(ride_id)
        if results is None:
            return {"message": "ride offer not found"}, 404

        return dict(zip(keys, results)), 200


@rideoffer.header("Authorization", "Access tokken", required=True)
@rideoffer.route('/update/<int:ride_id>', endpoint='ride_update')
class UpdateRides(Resource):
    @rideoffer.expect(ride_data)
    @rideoffer.doc(security='apikey')
    @jwt_required
    def put(self, ride_id):
        
        data = rideoffer.payload
        print(data)
        schema = RideSchema()
        schema_data = schema.load(data)
        errors = schema_data.errors
        error_types = ['route', 'price', 'depature',
                       'location', 'destination', 'seats']

    # checks if theres any errors
        for e in error_types:
            if e in errors.keys():
                return {'message': errors[e][0]}, 400

    # updates ride offer
        RideOffer.update_a_ride_offer(ride_id, data['route'], data['price'],
                                      data['departure'], data['location'], data['destination'], data['seats'])
        
        update = RideOffer.get_a_ride_offer(ride_id)

        return {'message':'update successful', 'data':dict(zip(keys, update)) }, 200

@rideoffer.header("Authorization", "Access tokken", required=True)
@rideoffer.route('/delete/<int:ride_id>', endpoint='delete_ride')
class Rides(Resource):
    @rideoffer.doc('delete a ride', security='apikey')
    @jwt_required
    def delete(self, ride_id):
        current_user = get_jwt_identity()

        delete_data = RideOffer.get_a_ride_offer(ride_id)
        if delete_data == None:
            return {'message': 'ride offer does not exist'}, 400

        #user cant delete a ride they dint create
       
        if current_user != delete_data[0]:
            return {'message': f'smh {current_user} you cant delete this ride'}, 422

        RideOffer.delete_ride_offer(ride_id)

        return {'message': 'successffully deleted',
                 'data'  : dict(zip(keys,delete_data))
        
        },200