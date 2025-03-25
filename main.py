from app.controllers.customer_controller import CustomerController
from app.controllers.bank_account_controller import BankAccountController
from app.controllers.transaction_controller import TransactionController
from app.controllers.auth_controller import AuthController
from app.models.customer import Customer
from app.enums import AccountType
from app.utils.validation import Validation

import logging 
from logs.logging_config import setup_logging

logger = logging.getLogger(__name__)

class Main:
    def __init__(self):
        self.customer_controller = CustomerController()
        self.bank_account_controller = BankAccountController()
        self.transaction_controller = TransactionController()
        self.auth_controller = AuthController()
        self.validation = Validation()

    def main_menu(self):
        print("\n====== Welcome to XYZ Bank ======")
        while True:
            try:
                print("\nMain Menu:")
                print("1. User Account")
                print("2. Admin Account")
                print("3. Exit")
                choice = int(input("Enter your choice:\n:: "))

                if choice == 1:
                    self.user_account_menu()
                elif choice == 2:
                    self.admin_login_menu()
                elif choice == 3:
                    print("Thank you for visiting XYZ Bank. Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")
            except Exception as e:
                logger.error(f"Main menu error: {e}")
                print(f"Error: {e}")

    # ========== User Section ==========

    def user_account_menu(self):
        while True:
            try:
                print("\nUser Account Menu:")
                print("1. Login")
                print("2. Register")
                print("3. Back to Main Menu")
                choice = int(input("Enter your choice:\n:: "))

                if choice == 1:
                    self.user_login()
                elif choice == 2:
                    self.user_register()
                elif choice == 3:
                    break
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")
            except Exception as e:
                logger.error(f"User account menu error: {e}")
                print(f"Error: {e}")

    def user_register(self):
        print("\n--- Register Your Account ---")
        customer_id = input("Enter your customer ID:\n:: ").strip()
        password = self.validation.get_validated_password()
        re_password = input("Re-enter your password:\n:: ").strip()
        hash_pass= self.validation.hash_password(password)
        if password != re_password:
            print("Passwords do not match. Please try again.")
            return

        dob = input("Enter Your Date of birth ...(dd/mm/year)..?::\n")

        customer_obj = Customer(customer_id=customer_id, password=hash_pass, dob=dob)
        try:
            result = self.customer_controller.update_register_customer(customer_obj)
            if result:
                print("Successfully registered your account.")
            else:
                print("Registration failed. Please try again.")
        except Exception as e:
            logger.error(f"User registration error: {e}")
            print("An error occurred during registration.")

    def user_login(self):
        print("\n--- User Login ---")
        customer_id = input("Enter your customer ID:\n:: ")
        password = self.validation.get_validated_password()
        customer_obj = Customer(customer_id=customer_id)
        try:
            login_pass = self.customer_controller.user_login(customer_obj)
            is_success = self.validation.check_password(password, login_pass)
            if is_success:
                print("Login successful!")
                self.account_menu(customer_id)
            else:
                print("Login failed. Invalid credentials.")
        except Exception as e:
            logger.error(f"User login error: {e}")
            print("An error occurred during login.")

    # ========== Admin Section ==========

    def admin_login_menu(self):
        print("\n--- Admin Login ---")
        admin_id = input("Enter your admin ID:\n:: ")
        password = input("Enter your admin password::\n::")

        try:
            login_success = self.auth_controller.admin_login(admin_id, password)
            if login_success:
                print("Welcome, Admin!")
                self.admin_actions()
            else:
                print("Invalid admin credentials.")
        except Exception as e:
            logger.error(f"Admin login error: {e}")
            print("An error occurred during admin login.")

    def admin_actions(self):
        while True:
            try:
                print("\nAdmin Menu:")
                print("1. Create Customer Account")
                print("2. Delete Customer Account")
                print("3. View All Customers")
                print("4. Back to Main Menu")
                choice = int(input("Choose an option:\n:: "))

                if choice == 1:
                    self.create_customer_account()
                elif choice == 2:
                    self.delete_customer_account()
                elif choice == 3:
                    self.view_all_customer()
                elif choice == 4:
                    break
                else:
                    print("Invalid option. Please choose 1, 2,3,4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                logger.error(f"Admin action error: {e}")
                print("An error occurred while performing admin actions.")

    def create_customer_account(self):
        print("\n--- Create New Customer Account ---")
        name = input("Enter full name:\n:: ")
        mobile = self.validation.get_validated_mobile_number()
        dob = self.validation.get_validated_date("Enter date of birth (DD/MM/YYYY):\n:: ")
        address = input("Enter address:\n:: ")
        print("Account Types:\n1. Savings Account\n2. Current Account\n3. Fixed Deposit")
        try:
            account_type_input = int(input("Choose Account Type (1, 2, or 3):\n:: "))
            account_type_map = {1: AccountType.SAVINGS.value, 2: AccountType.CURRENT.value, 3: AccountType.FIXED.value}
            account_type = account_type_map.get(account_type_input)
            if not account_type:
                print("Invalid account type. Must be 1, 2, or 3.")
                return

            result = self.customer_controller.create_customer(name, mobile, address, dob, account_type)
            if result:
                print("Customer account created successfully.")
            else:
                print("Failed to create account. Please try again.")
        except Exception as e:
            logger.error(f"Create customer account error: {e}")
            print("An error occurred while creating account.")

    def view_all_customer(self):
        try:
            result= self.customer_controller.get_all_customers()
            print(result)
        except Exception as e:
            logger.error(f"View all customer account error: {e}")
            print("An error occurred while View all acustomer.")

    def delete_customer_account(self):
        customer_id = input("Enter Customer ID to delete:\n:: ")
        try:
            result = self.customer_controller.soft_delete_customer(customer_id)
            if result:
                print("Customer account deleted successfully.")
            else:
                print("Failed to delete account. Please try again.")
        except Exception as e:
            logger.error(f"Delete customer account error: {e}")
            print("An error occurred while deleting account.")

    # ========== User Bank Operations ==========

    def account_menu(self, customer_id):
        while True:
            try:
                print(f"\nWelcome, {customer_id}!")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Account Details")
                print("6. Logout")

                choice = int(input("Choose your option:\n:: "))

                if choice == 1:
                    self.deposit_amount()
                elif choice == 2:
                    self.withdraw_amount()
                elif choice == 3:
                    self.check_balance(customer_id)
                elif choice == 4:
                    self.view_transaction_history(customer_id)
                elif choice == 5:
                    self.view_account(customer_id)
                elif choice == 6:
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please select 1 to 6.")
            except Exception as e:
                logger.error(f"Account menu error: {e}")
                print("An error occurred in account operations.")

    # ========== Banking Operations ==========

    def deposit_amount(self):
        amount = self.validation.get_validated_amount("Enter amount to deposit:\n:: ")
        if amount is None:
            return
        account_id = self.validation.get_validated_account_id()
        if account_id is None:
            return

        try:
            result = self.bank_account_controller.deposit(amount, account_id)
            logger.info(result)
        except Exception as e:
            logger.error(f"Deposit error: {e}")
            print("An error occurred during deposit.")

    def withdraw_amount(self):
        amount = self.validation.get_validated_amount("Enter amount to withdraw:\n:: ")
        if amount is None:
            return
        account_id = self.validation.get_validated_account_id()
        if account_id is None:
            return

        try:
            result = self.bank_account_controller.withdraw(amount, account_id)
            logger.info(result)
        except Exception as e:
            logger.error(f"withdraw error: {e}")
            print("An error occurred during withdraw.")

    def check_balance(self,customer_id):
        try:
            result = self.bank_account_controller.get_balance(customer_id)
            logger.info(result)
        except Exception as e:
            logger.error(f"Check Blance error: {e}")
            print("An error occurred during chack balance.")

    def view_transaction_history(self,customer_id):
        start_date= input("Enter your start date..?::")
        end_date= input("Enter your end date..?::")
        is_valid= self.validation.compare_dates(start_date,end_date)
        start_date = self.validation.safe_convert_date(start_date)
        end_date = self.validation.safe_convert_date(end_date)

        if is_valid:
            try:
                result = self.transaction_controller.view_transaction(start_date,end_date,customer_id)
                logger.info(result)
            except:
                logger.error("Error occured in date")
        else:
            logger.info("Invalid Dates")
            
    def view_account(self,customer_id):
        try:
            result = self.customer_controller.view_account(customer_id)
            logger.info(result)
        except Exception as e:
            logger.error(f"Account_details error: {e}")
            print("An error occurred during view account.")

if __name__ == '__main__':
    setup_logging
    app = Main()
    app.main_menu()
