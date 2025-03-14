print("!______Welcome to XYZ bank______!")

while True:
    try:
        print("\n1.login\n 2.Create Accont\n 3.Exit")
        # print("2.Create Accont")
        # input("Enter your choice....?")
        choice_input= int(input("Enter your choice....?"))
        
        if choice_input == 3:
            print("Thank you for visiting XYZ bank")
            break
        elif choice_input == 1:
            login_id= input("Enter your login id....?")
            password= input("Enter your password....?")
        elif choice_input == 2:
            print("Enter your details to create an account")
    except:
        print("invalid input")
    