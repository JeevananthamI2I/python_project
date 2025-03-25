import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

import logging
from services import AuthService

logger = logging.getLogger(__name__)

class AuthController:
    def __init__(self, auth_service=None):
        self.auth_service = auth_service or AuthService()

    def create_admin(self, admin_id, password):
        try:
            result = self.auth_service.create_admin(admin_id, password)
            logger.info(f"Admin created: {admin_id}")
            return result
        except Exception as e:
            logger.error(f"Error creating admin: {e}")
            raise Exception("Failed to create admin.") from e

    def admin_login(self, admin_id, password):
        try:
            is_admin = self.auth_service.admin(admin_id, password)
            logger.info(f"Admin login attempted: {admin_id}")
            return is_admin
        except Exception as e:
            logger.error(f"Admin login failed: {e}")
            raise Exception("Admin login failed.") from e
