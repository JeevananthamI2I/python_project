import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv() 
class Database:
    def __init__(self, dbname=None, user=None, password=None, host=None, port=5432):
        self.dbname = dbname or os.getenv("DB_NAME")
        self.user = user or os.getenv("DB_USER")
        self.password = password or os.getenv("DB_PASSWORD")
        self.host = host or os.getenv("DB_HOST")
        self.port = port or int(os.getenv("DB_PORT", 5432))

        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Database connected.")
        except psycopg2.OperationalError as e:
            print(f"Connection failed: {e}")
            self.connection = None

    def execute(self, query, params=None):
        try:
            if not self.connection:
                print("No DB connection.")
                return False
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except psycopg2.Error as e:
            print(f"Query failed: {e}")
            self.connection.rollback()
            return False
        
    def execute_and_return(self, query, params):
        self.cursor.execute(query, params)
        result = self.cursor.fetchone()
        self.connection.commit()
        return result

    def fetch_one(self):
        return self.cursor.fetchone() if self.cursor else None

    def fetch_all(self):
        return self.cursor.fetchall() if self.cursor else None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("DB connection closed.")

# Database()

# db= Database(dbname="mytest", user="postgres", password="jeeva", host="localhost")