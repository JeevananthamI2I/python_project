import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from services.customer_service import CustomerService

class CustomerController:
    def __init__(self):
        self.customer_service = CustomerService()
    

    def create_customer(self, customer_data):
        result = self.customer_service.add_customer(customer_data)
        return result

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
# custom_data={"customer_id":5, "name":"jennie", "mobile":"0987654398", "address":"chennai", "DOB": "2001-11-10"}
# data=cs.create_customer(custom_data)
# print(data)