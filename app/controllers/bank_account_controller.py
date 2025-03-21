from app.models.bank_account import BankAccount
from services.bank_account_service import BankAccountService
class BankAccountController():
    def __init__(self):
        self.bank_account_service = BankAccountService()

    def deposit(self, account_number, amount):
        return self.bank_account_service.deposit(account_number,amount)

    def get_balance(self, bank_account_number):
        return self.bank_account_service.get_balance(bank_account_number)