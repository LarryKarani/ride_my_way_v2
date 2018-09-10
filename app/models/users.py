"""This module contains the user model that regesters a new user """
import os
import datetime
from .db import Db


class User():
    def __init__(self, username, email, password, designation):
        self.username = username
        self.email = email
        self.password = password
        self.designation = designation

    def __repr__(self):
        return {'username': self.username,
                'email': self.email,
                'password': self.password,
                'designation': self.designation}
    @staticmethod
    def check_user(username):
        """checks if a user has already been register"""
        sql = "SELECT * FROM users WHERE users.username=\'%s\' "%(username)
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchone()
        return output
    @staticmethod
    def check_email(email):
        """checks if a user has already been register"""
        sql = "SELECT * FROM users WHERE users.email_adress=\'%s\' "%(email)
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchone()
        return output
    def register_user(self):
        """Regesters a new user into the database"""

       
        
        sql = 'INSERT INTO users (username,\
                                    pass_word,\
                                    email_adress,\
                                    user_type)\
                        VALUES(\'%s\', \'%s\', \'%s\',\'%s\');' % (
            self.username,
            # hash password
            self.password,
            self.email,
            self.designation
            )
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    

    @staticmethod
    def get_a_user(id):
        sql = f"SELECT * FROM users WHERE users.id={id}"
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        print(f"users with {id} is {output}")

    @staticmethod
    def update_user(id, username, email, designation):
        sql = f"UPDATE  users SET username = \'{username}\',\
                                 email_adress =\'{email}\',\
                                 user_type =\'{designation}\'\
                                 WHERE ride_offer.id = {id}"
        conn = Db.db_connection(os.environ.get('config_name'))
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("update  successful")

    @staticmethod
    def delete_user(id):
        sql = f"DELETE FROM ride_offer WHERE users.id ={id}"
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print(f'succesfuly deleted user with id {id}')

    @staticmethod
    def get_all_usesrs():
        sql = f"SELECT * FROM users"
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchall()
        print(f'output is {output}')
        return output
        

