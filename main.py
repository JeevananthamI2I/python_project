# main.py

from app.controllers.customer_controller import CustomerController
from app.controllers.bank_account_controller import BankAccountController
from app.controllers.transaction_controller import TransactionController
from app.controllers.auth_controller import AuthController
from app.models.customer import Customer
from app.models.bank_account import BankAccount
from app.models.transaction import Transaction

class Main:
    def __init__(self):
        self.customer_controller = CustomerController()
        self.bank_account_controller = BankAccountController()
        self.transaction_controller = TransactionController()
        self.auth_controller = AuthController()

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
                print(f"Error registering customer: {e}")
                return False
    # ========================== User Section ==========================

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
                print(f"Error registering customer: {e}")
                return False

    def user_register(self):
        print("\n--- Register Your Account ---")
        customer_id = input("Enter your customer ID:\n:: ").strip()
        password = input("Enter your password:\n:: ").strip()
        re_password = input("Re-enter your password:\n:: ").strip()

        if password != re_password:
            print("Passwords do not match. Please try again.")
            return

        dob = input("Enter your date of birth (DD/MM/YYYY):\n:: ").strip()

        customer_obj = Customer(customer_id=customer_id, password=password, dob=dob)
        result = self.customer_controller.update_register_customer(customer_obj)

        if result:
            print("Successfully registered your account.")
        else:
            print("Registration failed. Please try again.")

    def user_login(self):
        print("\n--- User Login ---")
        customer_id = input("Enter your customer ID:\n:: ")
        password = input("Enter your password:\n:: ")

        customer_obj = Customer(customer_id=customer_id, password=password)
        login_success = self.customer_controller.user_login(customer_obj)

        if login_success:
            print("Login successful!")
            self.account_menu(customer_id)
        else:
            print("Login failed. Invalid credentials.")

    # ========================== Admin Section ==========================

    def admin_login_menu(self):
        print("\n--- Admin Login ---")
        admin_id = input("Enter your admin ID:\n:: ")
        password = input("Enter your password:\n:: ")

        login_success = self.auth_controller.admin_login(admin_id, password)

        if login_success:
            print("Welcome, Admin!")
            self.admin_actions()
        else:
            print("Invalid admin credentials.")

    def admin_actions(self):
        while True:
            try:
                print("\nAdmin Menu:")
                print("1. Create Customer Account")
                print("2. Delete Customer Account")
                print("3. Back to Main Menu")
                choice = int(input("Choose an option:\n:: "))

                if choice == 1:
                    self.create_customer_account()
                elif choice == 2:
                    self.delete_customer_account()
                elif choice == 3:
                    break
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def create_customer_account(self):
        print("\n--- Create New Customer Account ---")
        name = input("Enter full name:\n:: ")
        mobile = input("Enter mobile number:\n:: ")
        dob = input("Enter date of birth (DD/MM/YYYY):\n:: ")
        address = input("Enter address:\n:: ")
        age = input("Enter your age...?\n::")

        print("Account Types:\n1. Savings Account\n2. Current Account")
        try:
            account_type_input = int(input("Choose Account Type (1 or 2):\n:: "))
            account_type_map = {1: "Savings Account", 2: "Current Account"}
            account_type = account_type_map.get(account_type_input)
            if not account_type:
                print("Invalid account type. Must be 1 or 2.")
                return
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            return

        result = self.customer_controller.create_customer(name, mobile, address, dob,age, account_type)
        if result:
            print("Customer account created successfully.")
        else:
            print("Failed to create account. Please try again.")

    def delete_customer_account(self):
        customer_id = input("Enter Customer ID to delete:\n:: ")
        result = self.customer_controller.delete_customer(customer_id)
        if result:
            print("Customer account deleted successfully.")
        else:
            print("Failed to delete account. Please try again.")

    # ========================== User Bank Operations ==========================

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
                    self.check_balance()
                elif choice == 4:
                    self.view_transaction_history()
                elif choice == 5:
                    self.view_account_details()
                elif choice == 6:
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please select 1 to 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def deposit_amount(self):
        try:
            amount = float(input("Enter amount to deposit:\n:: "))
            account_number = input("Enter your account ID:\n:: ")
            success = self.bank_account_controller.deposit(account_number, amount)
            if success:
                print(f"Successfully deposited {amount}.")
            else:
                print("Deposit failed. Please try again.")
        except ValueError:
            print("Invalid amount entered.")

    def withdraw_amount(self, customer_id):
        try:
            amount = float(input("Enter amount to withdraw:\n:: "))
            account_id = input("Enter your account ID:\n:: ")
            success = self.bank_account_controller.withdraw(account_id, amount)
            if success:
                print(f"Successfully withdrew {amount}.")
            else:
                print("Withdrawal failed or insufficient balance.")
        except ValueError:
            print("Invalid amount entered.")

    def check_balance(self):
        account_number = input("Enter your account Numer:\n:: ")
        balance = self.bank_account_controller.get_balance(account_number)
        print(f"Your current balance is: {balance}")

    def view_transaction_history(self, customer_id):
        account_id = input("Enter your account ID:\n:: ")
        transactions = self.transaction_controller.get_transactions(account_id)
        print("\nTransaction History:")
        for tx in transactions:
            print(tx)

    def view_account_details(self, customer_id):
        account_id = input("Enter your account ID:\n:: ")
        details = self.bank_account_controller.get_account_details(account_id)
        print("\nAccount Details:")
        print(details)

# Entry point
if __name__ == "__main__":
    app = Main()
    app.main_menu()
