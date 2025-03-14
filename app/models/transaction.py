from datetime import datetime

from base_model import BaseModel
from bank_account import BankAccount

class Transaction(BaseModel):
    def __init__(self,tansaction_id,bank_account_id,transaction_type, amount, start_date, end_date,**kwargs):
        super().__init__(**kwargs)
        self.transaction_type = transaction_type
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.transaction_id = tansaction_id
        self.bank_account_id = bank_account_id

    # @property
    # def bank_account(self):
    #     return self._bank_account
    # @bank_account.setter
    # def bank_account(self, bank_account):
    #     self._bank_account = bank_account
    @property
    def bank_account_id(self):
        return self._bank_account_id
    @bank_account_id.setter
    def bank_account_id(self, bank_account_id):
        self._bank_account_id = bank_account_id

    @property
    def transaction_id(self):
        return self._transaction_id
    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id
    
    @property
    def transaction_type(self):
        return self._transaction_type
    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self._transaction_type = transaction_type
    
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    
    @property
    def start_date(self):
        return self._start_date 
    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date    
    
    def __str__(self):
        return f"{self.transaction_id} {self.bank_account_id} {self.transaction_type} {self.amount} {self.start_date} {self.end_date} {self.created_at} {self.updated_at} {self.is_deleted}"
T = Transaction(1,1,"credit",1000,datetime.now(),datetime.now())
print(T)
   