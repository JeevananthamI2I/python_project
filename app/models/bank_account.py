import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from models.base_model import BaseModel
from models.customer import Customer

class BankAccount(BaseModel):
    def __init__(self, customer: Customer = None, customer_id=None, account_id=None, account_number=None, account_type=None, balance=0.0, **kwargs):
        super().__init__(**kwargs)
        self._account_id = account_id
        self._account_number = account_number
        self._account_type = account_type
        self.balance = balance
        self.customer = customer  # Uses the property setter
        if not customer:
            self._customer_id = customer_id

    # Property: account_id
    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    # Property: account_number
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # Property: account_type
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value

    # Property: balance
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    # Property: customer (Only one definition now)
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if value and not isinstance(value, Customer):
            raise TypeError("Expected a Customer object")
        self._customer = value
        if value:
            self._customer_id = value.customer_id

    # Read-only Property for customer_id
    @property
    def customer_id(self):
        return self._customer_id

    def __str__(self):
        return f"{self.account_id} [{self.customer}] {self.account_number} {self.account_type} {self.balance} {self.created_at} {self.updated_at} {self.is_deleted}"
