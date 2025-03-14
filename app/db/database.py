import os
import psycopg2
from psycopg2 import sql

class Database:
    
    def __init__(self, dbname=None, user=None, password=None, host=None, port=5432):
        
        self.dbname = dbname or os.getenv("DB_NAME")
        self.user = user or os.getenv("DB_USER")
        self.password = password or os.getenv("DB_PASSWORD")
        self.host = host or os.getenv("DB_HOST")
        self.port = port or int(os.getenv("DB_PORT", 5432))  # Default to 5432

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
            print("Database connected successfully.")
        except psycopg2.OperationalError as e:
            print(f"Connection failed: {e}")
            self.connection = None

    def close(self):        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("🔌 Database connection closed.")

    def commit(self):
        if self.connection:
            self.connection.commit()

    def rollback(self):
        if self.connection:
            self.connection.rollback()

    def execute(self, query, params=None):
        try:
            if not self.connection:
                print("No active database connection.")
                return False

            self.cursor.execute(query, params or ())
            self.commit()
            return True
        except psycopg2.Error as e:
            print(f"Query execution failed: {e}")
            self.rollback()
            return False

    def fetch_all(self):
        return self.cursor.fetchall() if self.cursor else None

    def fetch_one(self):
        return self.cursor.fetchone() if self.cursor else None

    def create_table(self, table_name, columns):
        try:
            query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
                sql.Identifier(table_name),
                sql.SQL(", ").join([sql.SQL(col) for col in columns])
            )
            return self.execute(query)
        except psycopg2.Error as e:
            print(f"Table creation failed: {e}")
            return False
