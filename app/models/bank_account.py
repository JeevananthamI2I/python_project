
import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from models.base_model import BaseModel
from models.customer import Customer

class BankAccount(BaseModel):
    def __init__(self,account_id, customer:Customer, account_number, account_type, balance, **kwargs):
        super().__init__(**kwargs)
        self._account_id = account_id
        self._account_number = account_number
        self._account_type = account_type
        self.balance = balance
        self.customer = customer

    @property
    def account_id(self):
        return self._account_id
    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def account_number(self):
        return self._account_number
    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number
    
    @property
    def account_type(self):
        return self._account_type
    @account_type.setter
    def account_type(self, account_type):
        self._account_type = account_type

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, balance):
        self._balance = balance
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        self._customer = customer
    
    def __str__(self):
        return f"{self.account_id} [{self.customer}] {self.account_number} {self.account_type} {self.balance} {self.created_at} {self.updated_at} {self.is_deleted}"

# c = Customer(1, "jeeva", "9122324320", "Chennai")
# ba= BankAccount(1, c, "1234567890", "savings", 1000)
# print(ba)
       
    