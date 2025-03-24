import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

import logging
from services.customer_service import CustomerService
import json

# Configure logging (optional, adjust level as needed)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomerController:
    def __init__(self):
        self.customer_service = CustomerService()

    def create_customer(self, customer_name, mobile_number, address, dob, account_type):
        try:
            result = self.customer_service.add_customer(customer_name, mobile_number, address, dob, account_type)
            logger.info(f"Customer created: {customer_name}")
            return result
        except Exception as e:
            logger.error(f"Error creating customer: {e}")
            raise Exception("Failed to create customer.") from e

    def update_register_customer(self, customer_data):
        try:
            result = self.customer_service.update_register_customer(customer_data)
            logger.info(f"Customer registration updated: {customer_data}")
            return result
        except Exception as e:
            logger.error(f"Error updating registered customer: {e}")
            raise Exception("Failed to update registered customer.") from e
    
    def user_login(self, customer_data):
        try:
            is_user = self.customer_service.login_user(customer_data)
            logger.info(f"User login attempted: {customer_data}")
            return is_user
        except Exception as e:
            logger.error(f"User login failed: {e}")
            raise Exception("User login failed.") from e
        
    def view_account(self, customer_id):
        try:
            account = self.customer_service.get_account_details_by_customer_id(customer_id)
            logger.info(f"Account Datails: {customer_id}")
            return account
        except Exception as e:
            logger.error(f"Error fetching details: {e}")
            raise Exception("Failed to get detail.") from e
    
    def get_all_customers(self):
        try:
            customers = self.customer_service.get_all_customers()
            result = clean_and_print_customers(customers)
            logger.info("Fetched all customers")
            return result
        except Exception as e:
            logger.error(f"Error fetching customers: {e}")
            raise Exception("Failed to retrieve customers.") from e

    def update_customer(self, customer_id, update_data):
        try:
            result = self.customer_service.update_customer(customer_id, update_data)
            logger.info(f"Customer updated: {customer_id}")
            return result
        except Exception as e:
            logger.error(f"Error updating customer: {e}")
            raise Exception("Failed to update customer.") from e

    def soft_delete_customer(self, customer_id):
        try:
            result = self.customer_service.soft_delete_customer(customer_id)
            logger.info(f"Customer deleted: {customer_id}")
            return result
        except Exception as e:
            logger.error(f"Error deleting customer: {e}")
            raise Exception("Failed to delete customer.") from e


####___________helper function_____________####
def clean_and_print_customers(self,customers):
    cleaned_list = []

    for customer in customers:
        dob = customer['dob']
        cleaned_customer = {
            "Customer ID": customer['customer_id'],
            "Name": customer['name'],
            "Mobile": customer['mobile'],
            "Address": customer['address'],
            "Date of Birth": dob.strftime("%Y-%m-%d"),
            "Age": customer['age']
        }
        cleaned_list.append(cleaned_customer)

    print(json.dumps(cleaned_list, indent=4))
