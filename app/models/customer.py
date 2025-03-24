import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from models.base_model import BaseModel

class Customer(BaseModel):
    def __init__(self, customer_name=None, age=None, dob=None, mobile_number=None,
                 address=None, customer_id=None, password=None, **kwargs):
        super().__init__(**kwargs)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.address = address
        self.dob = dob
        self.age = age
        self.password = password

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        self._dob = value

    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def __str__(self):
        return (f"CustomerID: {self.customer_id}, Name: {self.customer_name}, "
                f"Mobile: {self.mobile_number}, Address: {self.address}, "
                f"{super().__str__()}")
