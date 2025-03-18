from app.controllers.customer_controller import CustomerController
from app.controllers.auth_controller import AuthController    

class Main():
    def __init__(self):
        self.customer_controller = CustomerController()
        self.auth_controller = AuthController()
        

    def main_menu(self):
        print("!______Welcome to XYZ bank______!")
        while True:
            try:
                print("\n1.User Account\n2.Admin Account\n3.Exit")
                choice_input= int(input("Enter your choice....?"))
                
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
                db_login_id= "admin"
                db_password= "admin"   
                print("1.Login\n2.Register Account\n3.Exit")
                choice_input= int(input("Enter your user account menu choice....?\n:"))
                if choice_input == 2:
                    print("!________Register your account_______!")
                    customer_id= input("Enter your customer id....?\n:")
                    customer_password= input("Enter your password....?\n:")
                    re_password= input("Re-enter your password....?\n:")
                    account_num= input('Enter your account number\n')
                    dob= input("Enter your date of birth")
                    login_data = [customer_id,customer_password, re_password, account_num, dob]
                    result = self.auth_controller.user_register(login_data)
                    if result != None:
                        pass
                        # to do
                    else:
                        pass
                    print(result)
                    print("!__________Successfully registered your account_________!")
                elif choice_input == 1:
                    customer_id= input("Enter your login customer id....?\n:")
                    customer_password= input("Enter your password....?\n:")
                    is_user = self.auth_controller.user_login(customer_id, customer_password)
                    if is_user:
                        print("Successfully login User account")
                        #to do
                        # else:
                elif choice_input == 3:
                    break
            except ValueError:
                print("invalid input")
                # logic here todo 

    def admin_menu(self):
        try:
            
            admin_id= input("\nEnter your admin id....?\n:")
            password= input("\nEnter your password....?\n:")
            is_valid = self.auth_controller.admin_login(admin_id, password)
            if is_valid:
                print("1.CreateAccount\n2.DeleteAccount")
                admin_input = input("Choose Your Action .........?\n:")
                if admin_input==1: 
                    name=input("Enter Name?\n")
                    number=input("Enter Number?\n")
                    address=input("Enter Address?\n")
                    data = [name,number,address]
                    customer_data = self.customer_controller(data)
                    print(customer_data)
                    print("Successfully login Admin account")
                elif admin_input==2:
                    customer_id_input= input
            else:
                print("Invalid credentials")
        except ValueError:
            print("Invalid input")
            # logic here todo

if __name__ == "__main__":
    app = Main()
    app.main_menu()