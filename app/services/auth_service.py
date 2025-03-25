from repositories.auth_repository import AuthRepository
import logging

logger = logging.getLogger(__name__)

class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    def admin(self, login_id: str, password: str):
        """
        Validates admin credentials.
        """
        result = self.repo.admin_login(login_id, password)
        logger.info(f"Admin login {'successful' if result else 'failed'} for {login_id}.")
        return result

    def create_admin(self, login_id: str, password: str):
        """
        Creates a new admin user.
        """
        result = self.repo.add_admin(login_id, password)
        logger.info(f"Admin {login_id} creation {'successful' if result else 'failed'}.")
        return result

    def close(self):
        """
        Closes the repository's database connection.
        """
        self.repo.close()
        logger.info("AuthService closed repository connection.")
