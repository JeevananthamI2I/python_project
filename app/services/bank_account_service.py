# bank_account_service.py
# import sys 
# sys.path.append('C:\\PythonLearning\\bank_management\\app')
import random
from app.repositories.bank_account_repository import BankAccountRepository
from app.services.transaction_service import TransactionService
from app.models.bank_account import BankAccount
from app.enums import  TransactionType
class BankAccountService:
    def __init__(self):
        self.bank_account_repo = BankAccountRepository()
        self.transaction_service = TransactionService()
        self.bank_account =BankAccount

    def create_account(self, account_type, customer_id):
        # TEMP placeholder account number
        account_number = self.generate_account_number()

        # Create account object
        account_data = BankAccount(
            customer_id=customer_id,
            account_type=account_type,
            account_number=account_number,
            balance=0.0
        )

        # Insert and get account_id
        account_id = self.bank_account_repo.add_bank_account(account_data)
        if not account_id:
            raise Exception("Failed to create account.")

        return account_number

   

    def generate_account_number(self):
        """
        Generate a 10-digit random unique account number (string).
        """
        return f"ACC{random.randint(1000000000, 9999999999)}"


    def deposit(self, balance, account_id):
        # Create a fresh BankAccount object
        bank_account = BankAccount(
            account_id=account_id,
            balance=balance
        )
        if not self.bank_account_repo.account_exists(account_id):
            raise Exception(f"Account ID {account_id} does not exist. Cannot deposit.")
        updated_balance = self.bank_account_repo.deposit(bank_account)

        if updated_balance:
            print(f"Successfully deposited ₹{balance:.2f} into Account ID {account_id}.")
            transaction_data = {
                "account_id": account_id,
                "transaction_type": TransactionType.CREDIT.value,
                "amount": balance
            }
            print(TransactionType.CREDIT.value,"Deposit")
            transaction_id=self.transaction_service.create_transaction(transaction_data)
            return {
                "new_balance": f"+{updated_balance}",
                "transaction_id": transaction_id,
                "message": "Deposit successful."
            }  # Return new balance
        else:
            print("Deposit failed. Please try again.")
            return None
           

    def withdraw(self, balance, account_id):
        bank_account = BankAccount(
            account_id=account_id,
            balance=balance
        )
        if not self.bank_account_repo.account_exists(account_id):
            raise Exception(f"Account ID {account_id} does not exist. Cannot deposit.")
        
        updated_balance = self.bank_account_repo.withdraw(bank_account)
        if updated_balance:
            transaction_data = {
                "account_id": account_id,
                "transaction_type": TransactionType.DEBIT.value,
                "amount": balance
            }
            transaction_id= self.transaction_service.create_transaction(transaction_data)
            return {
                "new_balance": f"-{updated_balance}",
                "transaction_id": transaction_id,
                "message": "Withdrawal successful."
            }
        else:
            print("Withdraw failed. Please try again.")
            return None

    def get_balance(self, customer_id):
        return self.bank_account_repo.get_balance(customer_id)
    
