import sys
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from app.db.database import Database
import logging
from logs.logging_config import setup_logging

logger = logging.getLogger(__name__)

class TransactionRepository:
    def __init__(self):
        self.db = Database()
        self.table = "transactions"

    def create_transaction(self, transaction_data):
        query = f"""
            INSERT INTO {self.table} 
            (account_id, transaction_type, amount, transaction_date)
            VALUES (%s, %s, %s, CURRENT_DATE)
            RETURNING transaction_id;
        """
        try:
            result = self.db.execute_and_return(query, (
                transaction_data.account_id,
                transaction_data.transaction_type,
                transaction_data.amount
            ))
            logger.info(f"Transaction created for account {transaction_data.account_id}")
            return result[0] if result else None
        except Exception as e:
            logger.error(f"Failed to create transaction: {e}")
            return None

    def get_transactions_by_account(self, account_id):
        query = f"""
            SELECT * FROM {self.table} 
            WHERE account_id = %s AND is_deleted = FALSE
            ORDER BY transaction_date DESC;
        """
        try:
            self.db.execute(query, (account_id,))
            results = self.db.fetch_all()
            logger.info(f"Transactions retrieved for account ID {account_id}")
            return results if results else []
        except Exception as e:
            logger.error(f"Failed to retrieve transactions for account ID {account_id}: {e}")
            return []

    def get_transaction(self,start_date,end_date,customer_id):
        query = f"""SELECT t.transaction_id, t.account_id, t.transaction_type,
        t.amount, t.transaction_date
        FROM transactions t
        JOIN accounts a ON t.account_id = a.account_id
        JOIN customers c ON a.customer_id = c.customer_id
        WHERE c.customer_id = %s 
        AND t.transaction_date BETWEEN %s AND %s
        ORDER BY t.transaction_date DESC;
        """
        try:
            self.db.execute(query,(customer_id,start_date,end_date))
            result = self.db.fetch_all()
            if result:
                columns = [
                    "transaction_id", "account_id", "transaction_type", "amount", "transaction_date"
                ]
                return dict(zip(columns, result))
            return None
        except:
            logger.error(f"Failed to retrieve transactions for account ID {customer_id}: {e}")