from app.repositories.auth_repository import AuthRepository

class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    def admin(self, login_id, password):
        print(login_id,password,"service")
        if login_id != None and password != None:
            result = self.repo.admin_login(login_id, password)
            print("login::::",result)
            return result is not None
        else:
            return False
        
    def create_admin_user(self, login_id, password):
        return self.repo.create_user(login_id, password)

    def close(self):
        self.repo.close()
