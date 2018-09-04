import os
import datetime
from db import Db

"""This module containts the request ride feature"""


class RideRequest():
    def __init__(self, requested_by, phone,  ride_offer_id, current_location, final_destination):
        self.requested_by = requested_by
        self.phone = phone
        self.ride_offer_id = ride_offer_id
        self.current_location = current_location
        self.final_destination = final_destination

    # get requested_by from jwt current user
    def request_ride(self):
        sql = 'INSERT INTO ride_request(requested_by,\
                                      phone,\
                                      ride_id,\
                                      current_location,\
                                      final_destination)\
                            VALUES(\'%s\', \'%s\', \'%s\', \'%s\',\'%s\');' % (
                              self.requested_by,
                              self.phone,
                              self.ride_offer_id,
                              self.current_location,
                              self.final_destination
                            )

        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print(f'request for ride_id {self.ride_offer_id} added succesfully')

    @staticmethod
    def delete_ride_request(id):
        sql = f"DELETE FROM ride_request WHERE ride_request.id ={id}"
        conn = Db.db_connection(os.environ.get()
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        print('succesfuly deleted ride offer')

    @staticmethod
    def get_a_ride_request(id):
        sql=f"SELECT * FROM ride_request WHERE ride_request.id={id}"
        conn=Db.db_connection()
        cur=conn.cursor()
        cur.execute(sql)
        output=cur.fetchone()
        if output:
            print(f'this is your output {output}')
        else:
            print(f'request for  id {id} does not exist')

    @staticmethod
    def get_users_all_request(current_user):
        sql=f"SELECT * FROM ride_request WHERE ride_request.requested_by=\'{current_user}\'"
        conn=Db.db_connection()
        cur=conn.cursor()
        cur.execute(sql)
        output=cur.fetchall()

        if output:

            print(f'this is your output {output}')
        else:
            print(f'request for  id {current_user} does not exist')

    @staticmethod
    def get_all_ride_request_for_specific_ride_offer(offer_id):
        sql=f"SELECT * FROM ride_request WHERE ride_request.ride_offer_id={offer_id}"
        conn=Db.db_connection()
        cur=conn.cursor()
        cur.execute(sql)
        output=cur.fetchall()
        if output:
            print(f'this is your output {output}')
        else:
            print(f'request for  id {id} does not exist')


    @staticmethod
    def update_a_ride_request(id, phone, current_location, final_destination):
        sql=f"UPDATE  ride_request SET phone = \'{phone}\',\
                                           current_location = \'{ current_location}\',\
                                           final_destination= \'{final_destination}\'\
                                           WHERE ride_request.id = {id}"
        conn=Db.db_connection()
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        print(" request update  successful")

# refactor to check if id exist
# refactor to check if current user exist
