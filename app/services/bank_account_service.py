from repositories.bank_account_repository import BankAccountRepository
from models.bank_account import BankAccount

class BankAccountService():
    def __init__(self):
        self.bank_account = BankAccountRepository()


    def create_account(self, account_type, customer_id):
        account_data= BankAccount(account_number=account_number,customer_id=customer_id,account_type=account_type, balance=0.0)
        self.bank_account.add_bank_account(account_data)
        account_number= f"ACC{customer_id+10000}"
        account_data.account_number = account_number
        self.account_repository.update_account_number(customer_id, account_number)

        return 
    
    def get_bank_account(self, bank_account_id):
        return self.bank_account.get(bank_account_id)

    def update_bank_account(self, bank_account_id, bank_account):
        return self.bank_account.update(bank_account_id, bank_account)

    def delete_bank_account(self, bank_account_id):
        return self.bank_account.delete(bank_account_id)

    def get_bank_accounts(self):
        return self.bank_account.all()