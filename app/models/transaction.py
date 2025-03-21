import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from datetime import datetime
from models.base_model import BaseModel

class Transaction(BaseModel):
    def __init__(self, transaction_id, bank_account_id, transaction_type, amount, start_date=None, end_date=None, **kwargs):
        super().__init__(**kwargs)
        self.transaction_id = transaction_id
        self.bank_account_id = bank_account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.start_date = start_date or datetime.now()
        self.end_date = end_date or datetime.now()

    @property
    def transaction_id(self):
        return self._transaction_id
    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @property
    def bank_account_id(self):
        return self._bank_account_id
    @bank_account_id.setter
    def bank_account_id(self, value):
        self._bank_account_id = value

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
    def start_date(self):
        return self._start_date 
    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, value):
        self._end_date = value    

    def __str__(self):
        return (f"{self.transaction_id} {self.bank_account_id} {self.transaction_type} "
                f"{self.amount} {self.start_date} {self.end_date} {self.created_at} "
                f"{self.updated_at} {self.is_deleted}")

# Test Example
# if __name__ == "__main__":
#     T = Transaction(transaction_id=1, bank_account_id=1, transaction_type="credit", amount=1000)
#     print(T)
