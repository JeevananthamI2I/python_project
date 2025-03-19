from app.repositories.auth_repository import AuthRepository

class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    def admin(self, login_id, password):
        if login_id != None and password != None:
            result = self.repo.admin_login(login_id, password)
            return result is not None
        else:
            return False
        
    def create_admin(self, login_id, password):
        return self.repo.add_admin(login_id, password)

    def close(self):
        self.repo.close()
