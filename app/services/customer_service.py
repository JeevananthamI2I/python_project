import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

from repositories.customer_repository import CustomerRepository
from services.bank_account_service import BankAccountService
from models.customer import Customer


class CustomerService():
    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.bank_account_service = BankAccountService()
    
    def add_customer(self, customer_name,mobile_number,address,dob,account_type):
        dob = self.date_validation(dob)
        age = self.calculate_age(dob)
        customer = Customer(customer_name=customer_name,mobile_number=mobile_number,address=address,dob=dob,age=age)
        customer_id = self.customer_repository.add_customer(customer)
        account_number= self.bank_account_service.create_account(account_type,customer_id)
        return {
        "customer_id": customer_id,
        "account_number": account_number,
        "message": "Customer and account created successfully."
            }
    
    def calculate_age(self,dob):
        if not isinstance(dob, date):
            raise ValueError("DOB must be a date object")
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


    def date_validation(self,dob):
        if isinstance(dob, date):
            return dob 
        elif isinstance(dob, str):
            try:
                return datetime.strptime(dob.strip(), "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("DOB must be in DD/MM/YYYY format")
        else:
            raise ValueError("DOB must be a string or date object")



    def update_register_customer(self,customer_data):
        return self.customer_repository.update_register_customer(customer_data)
    
    def login_user(self, customer_data):
        return self.customer_repository.check_login(customer_data)
    
    def get_account_details_by_customer_id(self, customer_id):
        return self.customer_repository.get_account_details_by_customer_id(customer_id)
    
    def get_all_customers(self):
        return self.customer_repository.get_all_customers()
    
    def update_customer(self, customer_id, customer):
        customer = Customer(**customer)
        return self.customer_repository.update(customer_id, customer)

    def soft_delete_customer(self, customer_id):
        return self.customer_repository.soft_delete_customer(customer_id)

    # def get_all_customers(self):
    #     return self.customer_repository.get_all()
# cs = CustomerService()
# custom_data={"customer_id":4, "name":"XYZ", "mobile":"09876543000", "address":"guindy", "DOB": "2001-11-10"}
# add_customer = cs.add_customer(custom_data)
# print(add_customer)
# data=cs.get_customer(2)
# print(data)