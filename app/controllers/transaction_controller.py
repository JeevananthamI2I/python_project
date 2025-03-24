import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

import logging

logger = logging.getLogger(__name__)

class TransactionController:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, transaction):
        try:
            self.transactions.append(transaction)
            logger.info(f"Transaction created: {transaction}")
            return transaction
        except Exception as e:
            logger.error(f"Error creating transaction: {e}")
            raise Exception("Transaction creation failed.") from e

