import unittest
from controllers.customer_controller import CustomerController

class TestCustomerController(unittest.TestCase):
    def setUp(self):
        self.controller = CustomerController()

    def test_create_customer_success(self):
        # Sample test data
        customer_name = "Alice"
        mobile_number = "1234567890"
        address = "123 Street"
        dob = "1995-01-01"
        age = 30
        account_type = "savings"

        result = self.controller.create_customer(customer_name, mobile_number, address, dob, age, account_type)
        self.assertIsNotNone(result)

    def test_get_all_customers(self):
        customers = self.controller.get_all_customers()
        self.assertIsInstance(customers, list)

if __name__ == '__main__':
    unittest.main()
