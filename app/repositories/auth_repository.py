import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')
# print(sys.path)
from db.database import Database

class AuthRepository:
    def __init__(self):
        self.db = Database()
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS login_details (
            id SERIAL PRIMARY KEY,
            login_id VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        """
        return self.db.execute(query)
    
    def create_user(self, login_id, password):
        query = "INSERT INTO login_details (login_id, password) VALUES (%s, %s);"
        return self.db.execute(query, (login_id, password))

    def admin_login(self, login_id, password):
        print(login_id,password,"repos")
        query = "SELECT * FROM login_details WHERE login_id=%s AND password=%s;"
        self.db.execute(query, (login_id, password))
        return self.db.fetch_one()
    
    

    def close(self):
        self.db.close()

# ar= AuthRepository()
# print(ar.login_user("admin", "admin"))