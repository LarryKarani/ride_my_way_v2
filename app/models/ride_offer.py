import os
import datetime
from db import Db



class RideOffer():
    def __init__(self, ride_owner, ride_route, price, depature_time,
                 current_location, final_destination, available_seats,
                 ):
        self.ride_owner = ride_owner
        self.ride_route = ride_route
        self.price = price
        self.depature_time =depature_time
        self.current_location = current_location
        self.final_destination = final_destination
        self.available_seats = available_seats
        self.date_created = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    
    def create_ride(self):
        sql = 'INSERT INTO ride_offer(ride_owner,\
                                      ride_route,\
                                      price,\
                                      departure_time,\
                                      current_location,\
                                      final_destination,\
                                      available_seats,\
                                      date_created)\
                            VALUES(\'%s\', \'%s\', \'%s\', \'%s\',\'%s\',\'%s\',\'%s\',\'%s\');' %(
                              self.ride_owner,
                              self.ride_route ,
                              self.price,
                              self.depature_time,
                              self.current_location,
                              self.final_destination,
                              self.available_seats,
                              self.date_created  
                            )

                                      
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print('added succesfully')
    @staticmethod
    def delete_ride_offer(id):
        sql = f"DELETE FROM ride_offer WHERE ride_offer.id ={id}"
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print('succesfuly deleted ride offer')

    @staticmethod
    def get_a_ride_offer(id):
        sql = f"SELECT * FROM ride_offer WHERE ride_offer.id={id}"
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchone()
        if output:
            print(f'this is your output {output}')
        else:
            print(f'ride offer for id {id} does not exist')

    @staticmethod
    def get_all_ride_offers():
        sql = f"SELECT * FROM ride_offer"
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        if output:
            print(f'this is your output {output}')
        else:
            print('no ride offers yet')

    @staticmethod                             
    def update_a_ride_offer(id, ride_route, price,depature_time,
                            current_location,
                            final_destination,
                            available_seats):
        sql = f"UPDATE  ride_offer SET ride_route = \'{ride_route}\',\
                                           price = {price},\
                                           departure_time = \'{depature_time}\',\
                                           current_location = \'{ current_location}\',\
                                           final_destination = \'{final_destination}\',\
                                           available_seats = \'{available_seats}\'\
                                           WHERE ride_offer.id = {id}"
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("update  successful")
         

   

    