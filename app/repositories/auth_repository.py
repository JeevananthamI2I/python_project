from db.database import Database
import logging

logger = logging.getLogger(__name__)

class AuthRepository:
    def __init__(self):
        self.db = Database()
        self.table = "admin"

    def add_admin(self, login_id, password):
        """
        Inserts a new admin into the admin table.
        """
        query = "INSERT INTO admin (login_id, password) VALUES (%s, %s);"
        try:
            self.db.execute(query, (login_id, password))
            logger.info(f"Admin '{login_id}' added successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to add admin '{login_id}': {e}")
            return False

    def admin_login(self, login_id, password):
        """
        Validates admin login credentials.
        """
        query = "SELECT * FROM admin WHERE login_id = %s AND password = %s;"
        try:
            self.db.execute(query, (login_id, password))
            result = self.db.fetch_one()
            if result:
                logger.info(f"Admin login successful for '{login_id}'.")
            else:
                logger.warning(f"Admin login failed for '{login_id}'.")
            return result
        except Exception as e:
            logger.error(f"Failed to login admin '{login_id}': {e}")
            return None

    def close(self):
        """
        Closes the database connection.
        """
        try:
            self.db.close()
            logger.info("Database connection closed successfully.")
        except Exception as e:
            logger.error(f"Failed to close database connection: {e}")
