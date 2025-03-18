from app.services import AuthService

class AuthController():
    def __init__(self, auth_service=None):
        self.auth_service = auth_service or AuthService()

    def user_login(self, customer_id, password):
        # data = request.get_json()
        is_user = self.auth_service.login(customer_id, password)
        return is_user
    
    def admin_login(self, admin_id, password):
        # data = request.get_json()
        is_admin = self.auth_service.admin(admin_id, password)
        return is_admin
    
    def user_register(self, customer_id, password, account_number, date_of_birth):
        return self.auth_service.admin_user(customer_id, password, account_number, date_of_birth)