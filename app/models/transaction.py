import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from datetime import datetime
from models.base_model import BaseModel
from models.bank_account import BankAccount

class Transaction(BaseModel):
    def __init__(self, bank_account: BankAccount = None, transaction_id=None, account_id=None,
                 transaction_type=None, amount=None, transaction_date=None, **kwargs):
        super().__init__(**kwargs)
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_date = transaction_date or datetime.now()
        self.bank_account = bank_account
        if not bank_account:
            self.account_id = account_id

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, value):
        self._transaction_date = value

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        if value and not isinstance(value, BankAccount):
            raise TypeError("Expected a BankAccount object")
        self._bank_account = value
        if value:
            self._account_id = value.account_id

    def __str__(self):
        return (f"TransactionID: {self.transaction_id}, AccountID: {self.account_id}, "
                f"Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.transaction_date}, "
                f"{super().__str__()}")
