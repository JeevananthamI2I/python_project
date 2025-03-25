import sys
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from datetime import datetime, date
from db.database import Database
import logging
from logs.logging_config import setup_logging
logger = logging.getLogger(__name__)

class CustomerRepository:
    def __init__(self):
        self.db = Database()
        self.table = "customers"

    def get_all_customers(self):
        columns = ["customer_id", "name", "mobile", "address","age", "dob"]
        query = f"SELECT {', '.join(columns)} FROM {self.table} WHERE is_deleted = FALSE"
        try:
            self.db.execute(query)
            results = self.db.fetch_all()
            customer_list = [dict(zip(columns, row)) for row in results]
            return customer_list
        except Exception as e:
            logger.error(f"Failed to fetch all customers: {e}")
            return []

    def add_customer(self, customer):
        query = f"""
        INSERT INTO {self.table} (name, mobile, address, dob, password, age)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING customer_id;
        """
        try:
            result = self.db.execute_and_return(query, (
                customer.customer_name,
                customer.mobile_number,
                customer.address,
                customer.dob,
                customer.password,
                customer.age
            ))
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Failed to add customer: {e}")
            return None

    def update_register_customer(self, customer_data):
        try:
            if isinstance(customer_data.dob, str):
                customer_dob = datetime.strptime(customer_data.dob.strip(), "%d/%m/%Y").date()
            else:
                customer_dob = customer_data.dob

            query = f"""
            UPDATE {self.table} SET password = %s 
            WHERE customer_id = %s AND dob = %s RETURNING customer_id
            """
            result = self.db.execute_and_return(query, (
                customer_data.password, customer_data.customer_id, customer_dob
            ))
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error during update_register_customer: {e}")
            return None

    def check_login(self, customer_data):
        query = f"SELECT password FROM {self.table} WHERE customer_id = %s AND is_deleted = FALSE"
        try:
            self.db.execute(query, (customer_data.customer_id,))
            result = self.db.fetch_one()
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Login check failed: {e}")
            return None

    def get_account_details_by_customer_id(self, customer_id):
        query = """
        SELECT 
            c.customer_id, c.name, c.mobile, c.dob, c.address,
            a.account_id, a.account_number, a.account_type, a.balance
        FROM customers c
        LEFT JOIN accounts a ON c.customer_id = a.customer_id
        WHERE c.customer_id = %s AND c.is_deleted = FALSE;
        """
        try:
            self.db.execute(query, (customer_id,))
            result = self.db.fetch_one()
            if result:
                columns = [
                    "customer_id", "name", "mobile", "dob", "address",
                    "account_id", "account_number", "account_type", "balance"
                ]
                return dict(zip(columns, result))
            return None
        except Exception as e:
            logger.error(f"Error fetching account details: {e}")
            return None

    def update(self, customer_id, customer):
        query = f"""
        UPDATE {self.table} SET name = %s, mobile = %s, address = %s
        WHERE customer_id = %s RETURNING customer_id
        """
        try:
            result = self.db.execute_and_return(query, (
                customer.name, customer.mobile, customer.address, customer_id
            ))
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Failed to update customer: {e}")
            return None

    def soft_delete_customer(self, customer_id):
        query = f"UPDATE {self.table} SET is_deleted = TRUE WHERE customer_id = %s"
        try:
            self.db.execute(query, (customer_id,))
            logger.info(f"Customer ID {customer_id} soft-deleted successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to soft delete customer: {e}")
            return False

    def add_register_password(self, customer_id, password):
        query = f"UPDATE {self.table} SET password = %s WHERE customer_id = %s"
        try:
            self.db.execute(query, (password, customer_id))
            logger.info(f"Password updated for customer ID {customer_id}.")
            return True
        except Exception as e:
            logger.error(f"Failed to update password: {e}")
            return False
