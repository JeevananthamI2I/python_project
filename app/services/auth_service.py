import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from repositories.auth_repository import AuthRepository

class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    def admin(self, login_id, password):
        return self.repo.admin_login(login_id, password)
        
    def create_admin(self, login_id, password):
        return self.repo.add_admin(login_id, password)
    
    def close(self):
        self.repo.close()
