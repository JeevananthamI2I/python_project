import unittest
from controllers.auth_controller import AuthController

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.controller = AuthController()

    def test_create_admin(self):
        result = self.controller.create_admin("admin1", "password123")
        self.assertIsNotNone(result)

    def test_admin_login(self):
        result = self.controller.admin_login("admin1", "password123")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
