from app.services import AuthService

class AuthController():
    def __init__(self, auth_service=None):
        self.auth_service = auth_service or AuthService()

    def user_login(self, customer_id, password):
        is_user = self.auth_service.login(customer_id, password)
        return is_user
    
    def user_register(self, customer_id, password, account_number, date_of_birth):
        return self.auth_service.admin_user(customer_id, password, account_number, date_of_birth)
    
    #admin create and login for accounts
    def create_admin(self, admin_id, password):
        result = self.auth_service.create_admin(admin_id, password)
        return result
    
    def admin_login(self, admin_id, password):
        is_admin = self.auth_service.admin(admin_id, password)
        return is_admin
    