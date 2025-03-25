from repositories.bank_account_repository import BankAccountRepository
from repositories.transaction_repository import TransactionRepository
from models.bank_account import BankAccount

class BankAccountService():
    def __init__(self):
        self.bank_account_repo = BankAccountRepository()
        self.transaction_repo = TransactionRepository()

    def create_account(self, account_type, customer_id):
        account_data= BankAccount(customer_id=customer_id,account_type=account_type, balance=0.0)
        account_id = self.bank_account_repo.add_bank_account(account_data)
        account_number= f"ACC{account_id+10000}"
        account_data.account_number = account_number
        return self.bank_account_repo.update_account_number(account_id, account_number)
 
    
    def get_balance(self, bank_account_number):
        return self.bank_account_repo.retrive_balance(bank_account_number)
    
    def doposit(self, amount, account_number):
        customer_id= self.bank_account_repo.doposit(amount,account_number)
        self.
        return 
    def get_bank_account(self, bank_account_id):
        return self.bank_account.get(bank_account_id)

    def update_bank_account(self, bank_account_id, bank_account):
        return self.bank_account.update(bank_account_id, bank_account)

    def delete_bank_account(self, bank_account_id):
        return self.bank_account.delete(bank_account_id)

    def get_bank_accounts(self):
        return self.bank_account.all()