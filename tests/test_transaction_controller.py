import unittest
from controllers.transaction_controller import TransactionController

class TestTransactionController(unittest.TestCase):
    def setUp(self):
        self.controller = TransactionController()

    def test_create_transaction(self):
        transaction = {"type": "deposit", "amount": 100}
        result = self.controller.create_transaction(transaction)
        self.assertIn(transaction, self.controller.transactions)

if __name__ == '__main__':
    unittest.main()
