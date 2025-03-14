
from base_model import BaseModel

class Customer(BaseModel):
    def __init__(self,customer_id, customer_name, mobile_number, address, **kwargs):
        super().__init__(**kwargs)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.address = address

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

    def __str__(self):
        return f"{self.customer_id} {self.customer_name} {self.mobile_number} {self.address} {self.created_at} {self.updated_at} {self.is_deleted}"

u = Customer(1, "jeeva", "9122324320", "Chennai")
print(u)