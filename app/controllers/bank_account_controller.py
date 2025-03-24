import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

import logging
from app.models.bank_account import BankAccount
from services.bank_account_service import BankAccountService

logger = logging.getLogger(__name__)

class BankAccountController:
    def __init__(self):
        self.bank_account_service = BankAccountService()

    def deposit(self, amount, account_id):
        try:
            result = self.bank_account_service.deposit(amount, account_id)
            logger.info(f"Deposited {amount} to account: {account_id}")
            return result
        except Exception as e:
            logger.error(f"Error during deposit: {e}")
            raise Exception("Deposit failed.") from e
    
    def withdraw(self, amount, account_id):
        try:
            result = self.bank_account_service.withdraw(amount, account_id)
            logger.info(f"Withdraw {amount} to account: {account_id}")
            return result
        except Exception as e:
            logger.error(f"Error during deposit: {e}")
            raise Exception("Deposit failed.") from e

    def get_balance(self, customer_id):
        try:
            result = self.bank_account_service.get_balance(customer_id)
            logger.info(f"Balance check requested for Customer ID: {customer_id}")
            balance = float(result)
            if result is not None:
                logger.info(f"Your Balance is Rs={balance}")
                return balance
            else:
                logger.warning(f"No account found for Customer ID: {customer_id}")
                return None

        except Exception as e:
            logger.error(f"Error fetching balance for Customer ID {customer_id}: {e}")
            raise Exception("Failed to get balance.") from e

