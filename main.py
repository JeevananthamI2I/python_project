from app.controllers.customer_controller import CustomerController
from app.controllers.bank_account_controller import BankAccountController
from app.controllers.transaction_controller import TransactionController
from app.controllers.auth_controller import AuthController    
from app.models.customer import Customer
from app.models.bank_account import BankAccount
from app.models.transaction import Transaction

class Main():
    def __init__(self):
        self.customer_controller = CustomerController()
        self.bank_Account_controller = BankAccountController()
        self.transaction_controller = TransactionController()
        self.auth_controller = AuthController()
        # self.customer = Customer
        self.bank_account = BankAccount
        self.transaction = Transaction

    def main_menu(self):
        print("!______Welcome to XYZ bank______!")
        while True:
            try:
                print("\n1.User Account\n2.Admin Account\n3.Exit")
                choice_input= int(input("Enter your choice....?\n::"))
                
                if choice_input == 3:
                    print("Thank you for visiting XYZ bank")
                    break
                elif choice_input == 1:
                    self.user_account()
                elif choice_input == 2:
                    self.admin_menu()
            except ValueError:
                print("invalid input")
            

    def user_account(self):
        while True:
            try:  
                print("1.Login\n2.Register Account\n3.Exit")
                choice_input= int(input("Enter your user account menu choice....?\n:"))
                if choice_input == 2:
                    print("!________Register your account_______!")
                    customer_id= input("Enter your customer id....?\n::")
                    customer_password= input("Enter your password....?\n::")
                    re_password= input("Re-enter your password....?\n::")
                    dob= input("Enter your date of birth\n::")
                    if customer_password == re_password:
                        customer_values = self.customer(customer_id=customer_id,password=customer_password,dob=dob)
                        customer_data = self.customer_controller.update_register_customer(customer_values)
                        print(customer_data)
                        if customer_data:
                            print("!__________Successfully registered your account_________!")
                        else:
                            print("Failed to register your account. Try again.")
                elif choice_input == 1:
                    customer_id= input("Enter your login customer id....?\n::")
                    customer_password= input("Enter your password....?\n::")
                    customer_login= self.customer(customer_id=customer_id,password=customer_password)
                    result= self.customer_controller.user_login(customer_login)
                    if result:
                        self.account_menu()
                    else:
                         print("Failed to log in your account. Try again.")
                elif choice_input == 3:
                    break
            except ValueError:
                print("invalid input")
                # logic here todo 

    def admin_menu(self):
        while True:
            try:
                
                admin_id= input("\nEnter your admin id....?\n::")
                password= input("\nEnter your password....?\n::")
                if admin_id != None or password != None:
                    result = self.auth_controller.admin_login(admin_id, password)
                    if result:
                        print("___Welcome admin account___\n1.CreateAccount\n2.DeleteAccount\n3.Exit\n::")
                        admin_input = int(input("Choose Your option  above.........?\n::"))
                        if admin_input == 1: 
                            customer_name=input("Enter account creation Name?::\n::")
                            mobile_number=input("Enter mobile Number?::\n::")
                            dob=input("Enter date of Birth.( %d/%m/%Y).?::\n::").strip()
                            address=input("Enter your Address?\n")
                            account_type=input("Enter your Account Type?\n")
                            # customer_values = self.customer(customer_name=customer_name,mobile_number=mobile_number,address=address,dob=dob)
                            customer_data = self.customer_controller.create_customer(customer_name,mobile_number,address,dob,account_type)
                            print(customer_data)
                            if customer_data != None:
                                print("Successfully login create account")
                            else:
                                print("Failed to login create account. Try again.")
                        elif admin_input == 2:
                            pass
                        elif admin_input == 3:    
                            break
                    else:
                        print("Invalid credentials")
                else:
                    print("Invalid credentials")
                
                
            except ValueError:
                print("Invalid input!!!!!!!!!!!!")
                # logic here todo

    def account_menu(self):
        while True:
            try:
                print(f"Welcome to Your Account")
                print("1.Deposit\n2.Withdraw\n3.Balance\n4.Transaction History\n5.Account Details\n6.exit")
                choice_input = int(input("Choose your option..?\n:"))
                if choice_input == 1:
                    pass
                elif choice_input ==2:
                    pass
                elif choice_input == 3:
                    balance= self.bank_Account_controller.get_balance()
            except ValueError:
                print("Invalid Inputs!!!!!!!!!!!!!")

                        
if __name__ == "__main__":
    app = Main()
    app.main_menu()