import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

# transaction_service.py

from app.repositories.transaction_repository import TransactionRepository
from app.models.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.transaction_repo = TransactionRepository()
        self.transaction_obj = Transaction

    def create_transaction(self, transaction_data):
        # Create a Transaction model object using correct dict access
        transaction_obj = Transaction(
            account_id=transaction_data["account_id"],
            transaction_type=transaction_data["transaction_type"],
            amount=transaction_data["amount"]
        )
        return self.transaction_repo.create_transaction(transaction_obj)

    def get_transactions_by_account(self, account_id):
        return self.transaction_repo.get_transactions_by_account(account_id)
