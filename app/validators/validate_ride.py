from marshmallow import Schema, fields,  validates, ValidationError


class RideSchema(Schema):
    """Validates ride offer data"""
    
    route = fields.String(required=True)
    price = fields.String(required=True)
    departure = fields.String(required=True)
    location = fields.String(required=True)
    destination = fields.String(required=True)
    seats= fields.Integer(required=True)

    
    @validates('route')
    def validates_route(self, route):
        if route.strip() == '':
            return {'message': 'route cannot be empty'}
    
    @validates('price')
    def validates_price(self, price):
        if price.strip() == '':
            return {'message': 'owner cannot be empty'}

    @validates('departure') 
    def validates_depature(self, departure):
        if departure.strip() == '':
            return {'message': 'depature cannot be empty'} 

    @validates('location') 
    def validates_location(self, location):
        if location.strip() == '':
            return {'message': 'location cannot be empty'} 

    @validates('destination') 
    def validates_location(self, destination):
        if destination.strip() == '':
            return {'message': 'destination cannot be empty'} 

    @validates('seats') 
    def validates_location(self, seats):
        if seats < 1:
            return {'message': 'seats should atlist 1'} 
