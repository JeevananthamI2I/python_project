from customer import Customer

class RegisterDetail():
    def __init__(self, register_id, password, customer:Customer):
        self.register_id = register_id
        self.password = password
        self.customer = customer

    @property
    def register_id(self):
        return self._register_id
    @register_id.setter
    def register_id(self, register_id):
        self._register_id = register_id
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        self._customer = customer
    
    def __str__(self):
        return f"{self.register_id} [{self.customer}] {self.password}"
    
rd= RegisterDetail(1, "password", Customer(1, "jeeva", "9122324320", "Chennai"))
print(rd)
        