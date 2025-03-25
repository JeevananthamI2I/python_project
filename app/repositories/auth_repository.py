import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')
from db.database import Database

class AuthRepository():
    def __init__(self):
        self.db = Database()
        self.table = "admin"
        self.columns = ["login_id", "password"]

    def create_table_admin(self):
        query = """
        CREATE TABLE admin (
            id SERIAL PRIMARY KEY,
            login_id VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        """
        return self.db.execute(query)
    
    def add_admin(self, login_id, password):
        query = "INSERT INTO admin (login_id, password) VALUES (%s, %s);"
        return self.db.execute(query, (login_id, password))

    def admin_login(self, login_id, password):
        query = "SELECT * FROM admin WHERE login_id=%s AND password=%s;"
        self.db.execute(query, (login_id, password))
        return self.db.fetch_one()
    
    

    def close(self):
        self.db.close()

# ar= AuthRepository()
# ar.create_table_admin()
# ar.create_admin("admin", "admin123")
# print()