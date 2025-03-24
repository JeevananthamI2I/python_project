import unittest
from controllers.bank_account_controller import BankAccountController

class TestBankAccountController(unittest.TestCase):
    def setUp(self):
        self.controller = BankAccountController()

    def test_deposit(self):
        result = self.controller.deposit(500, "ACC123")
        self.assertIsNotNone(result)

    def test_get_balance(self):
        result = self.controller.get_balance("ACC123")
        self.assertIsInstance(result, (int, float))

if __name__ == '__main__':
    unittest.main()
