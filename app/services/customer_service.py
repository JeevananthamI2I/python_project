import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from repositories.customer_repository import CustomerRepository
from models.customer import Customer

class CustomerService():
    def __init__(self):
        self.customer_repository = CustomerRepository()
    
    def add_customer(self, customer):
        # customer = Customer(**customer)
        return self.customer_repository.customer_create(customer)

    def get_customer(self, customer_id):
        return self.customer_repository.get(customer_id)

    def update_customer(self, customer_id, customer):
        customer = Customer(**customer)
        return self.customer_repository.update(customer_id, customer)

    def delete_customer(self, customer_id):
        return self.customer_repository.delete(customer_id)

    # def get_all_customers(self):
    #     return self.customer_repository.get_all()
# cs = CustomerService()
# custom_data={"customer_id":4, "name":"XYZ", "mobile":"09876543000", "address":"guindy", "DOB": "2001-11-10"}
# add_customer = cs.add_customer(custom_data)
# print(add_customer)
# data=cs.get_customer(2)
# print(data)