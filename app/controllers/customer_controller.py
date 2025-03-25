import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from models.customer import Customer
from services.customer_service import CustomerService

class CustomerController():
    def __init__(self):
        self.customer_service = CustomerService()
        # self.customer = Customer()

    def create_customer(self, customer_name,mobile_number,address,dob,age,account_type):
        result = self.customer_service.add_customer(customer_name,mobile_number,address,dob,age,account_type)
        return result

    def update_register_customer(self, customer_data):
        result = self.customer_service.update_register_customer(customer_data)
        return result
    
    def user_login(self, customer_data):
        is_user = self.customer_service.login_user(customer_data)
        return is_user
    
    def get_all_customers(self):
        customers = self.customer_service.get_all_customers()
        return customers

    def update_customer(self, customer_id, update_data):
        result = self.customer_service.update_customer(customer_id, update_data)
        return result

    def delete_customer(self, customer_id):
        result = self.customer_service.delete_customer(customer_id)
        return result

    
# cs=CustomerController()
# custom_data={"name":"jennie", "mobile":"0987654398", "address":"chennai", "dob": "2001-11-10"}
# data=cs.create_customer(custom_data)
# print(data)