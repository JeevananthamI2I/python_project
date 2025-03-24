import sys
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from db.database import Database
from models.bank_account import BankAccount
from models.customer import Customer

import logging
from logs.logging_config import setup_logging
logger = logging.getLogger(__name__)

class BankAccountRepository:
    def __init__(self):
        self.db = Database()
        self.table = "accounts"

    def create_enum(self):
        query = """
        CREATE TYPE bank_account_enum AS ENUM ('Savings Account', 'Current Account');
        """
        try:
            self.db.execute(query)
            logger.info("Enum type 'bank_account_enum' created successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to create enum type: {e}")
            return False

    def create_table(self):
        query = """
        CREATE TABLE accounts (
            account_id SERIAL PRIMARY KEY,
            customer_id INT NOT NULL,
            account_number INT NOT NULL UNIQUE,
            account_type bank_account_enum NOT NULL,
            balance NUMERIC DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_deleted BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                ON DELETE CASCADE
        );
        """
        try:
            self.db.execute(query)
            logger.info("Table 'accounts' created successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to create table: {e}")
            return False

    def alter_accounts_table(self):
        query = "ALTER TABLE accounts ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN DEFAULT FALSE"
        try:
            self.db.execute(query)
            logger.info("Table 'accounts' altered successfully.")
            return True
        except Exception as e:
            logger.error(f"Failed to alter table: {e}")
            return False

    def add_bank_account(self, account_data: BankAccount):
        query = f"""
        INSERT INTO {self.table} (account_number, customer_id, balance, account_type)
        VALUES (%s, %s, %s, %s) RETURNING account_id
        """
        try:
            result = self.db.execute_and_return(query, (
                account_data.account_number,
                account_data.customer_id,
                account_data.balance,
                account_data.account_type
            ))
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error adding bank account: {e}")
            return None

    def update_account_number(self, account_data: BankAccount):
        query = f"""
        UPDATE {self.table} SET account_number = %s WHERE account_id = %s RETURNING account_number
        """
        try:
            result = self.db.execute_and_return(query, (
                account_data.account_number, account_data.account_id
            ))
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error updating account number: {e}")
            return None

    def retrieve_balance(self, account_number):
        query = f"""
        SELECT a.account_number, a.balance, COALESCE(SUM(t.amount), 0)
        FROM {self.table} a
        LEFT JOIN transaction t ON a.account_number = t.account_number AND t.transaction_type = 'DEPOSIT'
        WHERE a.account_number = %s
        GROUP BY a.account_number, a.balance
        """
        try:
            self.db.execute(query, (account_number,))
            result = self.db.fetch_one()
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error retrieving balance for Account Number {account_number}: {e}")
            return None

    def deposit(self, bank_account_data):
        query = f"""
        UPDATE {self.table} SET balance = balance + %s WHERE account_id = %s RETURNING balance
        """
        try:
            result = self.db.execute_and_return(query, (
                bank_account_data.balance, bank_account_data.account_id
            ))
            return result if result else None
        except Exception as e:
            logger.error(f"Deposit error: {e}")
            return None

    def withdraw(self, bank_account_data):
        query = f"""
        UPDATE {self.table} SET balance = balance - %s WHERE account_id = %s RETURNING balance
        """
        try:
            result = self.db.execute_and_return(query, (
                bank_account_data.balance, bank_account_data.account_id
            ))
            return result if result else None
        except Exception as e:
            logger.error(f"Withdraw error: {e}")
            return None

    def get_balance(self, customer_id):
        query = f"""
        SELECT balance FROM {self.table} WHERE customer_id = %s AND is_deleted = FALSE
        """
        try:
            self.db.execute(query, (customer_id,))
            result = self.db.fetch_one()
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            return None

    def account_exists(self, account_id):
        query = f"SELECT 1 FROM {self.table} WHERE account_id = %s"
        try:
            self.db.execute(query, (account_id,))
            result = self.db.fetch_one()
            return result is not None
        except Exception as e:
            logger.error(f"Error checking account existence: {e}")
            return False
