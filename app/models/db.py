import os
import psycopg2


class Db():
    """This class handles all the initial db transactions"""
    @staticmethod
    def db_connection():
        """creates a connection to the postgres db"""

        conn = psycopg2.connect(
            dbname=os.environ.get("db_name"),
            user="postgres",
            password=os.environ.get('db_password')
        )
        print(conn)
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
        return conn

    @staticmethod
    def create_tables():
        """creates all the tables and the relationships"""
        commands = (
            # creates users table
            """CREATE TABLE IF NOT EXISTS users( 
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                pass_word VARCHAR(255) NOT NULL,
                email_adress VARCHAR(255) NOT NULL,
                user_type VARCHAR(255) NOT NULL
            )""",
            # creates ride_offer table
            """CREATE TABLE IF NOT EXISTS ride_offer(
                ride_owner VARCHAR(255) NOT NULL,
                id SERIAL PRIMARY KEY,
                ride_route VARCHAR(255) NOT NULL,
                price VARCHAR(255) NOT NULL,
                departure_time VARCHAR(255) NOT NULL,
                current_location VARCHAR(255) NOT NULL,
                final_destination VARCHAR(255) NOT NULL,
                available_seats INTEGER NOT NULL,
                date_created VARCHAR(255) NOT NULL
            )""",
            # creates ride_request table
            """CREATE TABLE IF NOT EXISTS ride_request(
                requested_by VARCHAR(255) NOT NULL,
                id SERIAL PRIMARY KEY,
                ride_id INTEGER NOT NULL,
                phone VARCHAR(255) NOT NULL,
                current_location VARCHAR(255) NOT NULL,
                final_destination VARCHAR(255) NOT NULL,
                FOREIGN KEY(ride_id) REFERENCES ride_offer(id)
            )"""
        )

        con = Db.db_connection()
        print(con)
        cur = con.cursor()
        for command in commands:
            cur.execute(command)
            con.commit()

    @staticmethod
    def drop_all_tables():
        con = Db.db_connection()
        command = (
            'drop table if exists "' | | users | | '" cascade;' from pg_tables
            'drop table if exists "' | | ride_request | | '" cascade;' from pg_tables
            'drop table if exists "' | | ride_offer | | '" cascade;' from pg_tables
        )

        for command in commands:
            cur.execute(command)
            con.commit()
