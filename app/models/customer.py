import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from models.base_model import BaseModel

class Customer(BaseModel):
    def __init__(self, customer_name, dob, mobile_number,address,customer_id=None, password=None, **kwargs):
        super().__init__(**kwargs)
        if not customer_name or not mobile_number:
            raise ValueError("Customer name and mobile number are required.")
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.address = address
        self.dob = dob
        self.password = password

    @property   
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id
    
    @property
    def customer_name(self):
        return self._customer_name
    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name
    
    @property
    def dob(self):
        return self._dob
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    @property
    def mobile_number(self):
        return self._mobile_number
    @mobile_number.setter
    def mobile_number(self, mobile_number):
        self._mobile_number = mobile_number
    
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f"{self.customer_id} {self.customer_name} {self.mobile_number} {self.address} {self.created_at} {self.updated_at} {self.is_deleted}"

# u = Customer(1, "jeeva", "9122324320", "Chennai")
# print(u)