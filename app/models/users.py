"""This module contains the user model that regesters a new user """
import os
import datetime
from db import Db


class User():
    def __init__(self, user_name, email, password, user_type):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.user_type = user_type

    def check_user(self):
        """checks if a user has already been register"""
        sql = f"SELECT FROM users WHERE users.username= \'{self.user_name}\'"
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchone()
        return output

    def register_user(self):
        """Regesters a new user into the database"""

        user = self.check_user()

        if len(user) == 0:
            print(f'user {self.user_name} already exist')
        else:
            sql = 'INSERT INTO users (username,\
                                      pass_word,\
                                      email_adress,\
                                      user_type)\
                            VALUES(\'%s\', \'%s\', \'%s\',\'%s\');' % (
                self.user_name,
                # hash password
                self.password,
                self.email,
                self.user_type
            )
            conn = Db.db_connection()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print(f'user {self.user_name} added succesfully')

    @staticmethod
    def get_a_user(id):
        sql = f"SELECT FROM users WHERE users.id= {id}"
        conn = Db.db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        output = cur.fetchone()
        print(f"users with {id} is {output}")

    @staticmethod
    def update_user(id, username, email, user_type):
        sql = f"UPDATE  users SET username = \'{username}\',\
                                 email_adress =\'{email}\',\
                                 user_type =\'{user_type}\'\
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
