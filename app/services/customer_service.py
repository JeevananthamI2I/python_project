import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from datetime import datetime

from repositories.customer_repository import CustomerRepository
from services.bank_account_service import BankAccountService
from models.customer import Customer


class CustomerService():
    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.bank_account_service = BankAccountService()
    
    def add_customer(self, customer_name,mobile_number,address,dob,account_type):
        dob= self.date_validation(dob)
        customer = Customer(customer_name=customer_name,mobile_number=mobile_number,address=address,dob=dob)
        customer_id = self.customer_repository.add_customer(customer)
        account_number= self.bank_account_service.create_account(account_type,customer_id)
        return {
        "customer_id": customer_id,
        "account_number": account_number,
        "message": "Customer and account created successfully."
            }

    def date_validation(self,dob_input):
        try:
            return datetime.strptime(dob_input, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD/MM/YYYY")

    def update_register_customer(self,customer_data):
        customer_data.dob= self.date_validation(customer_data.dob)
        return self.customer_repository.update_register_customer(customer_data)
    
    def login_user(self, customer_data):
        return self.customer_repository.check_login(customer_data)
    
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