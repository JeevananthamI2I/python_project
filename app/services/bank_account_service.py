class BanskService():
    def __init__(self):
        self.bank_account = BankAccount()

    def get_bank_account(self, bank_account_id):
        return self.bank_account.get(bank_account_id)

    def create_bank_account(self, bank_account):
        return self.bank_account.create(bank_account)

    def update_bank_account(self, bank_account_id, bank_account):
        return self.bank_account.update(bank_account_id, bank_account)

    def delete_bank_account(self, bank_account_id):
        return self.bank_account.delete(bank_account_id)

    def get_bank_accounts(self):
        return self.bank_account.all()