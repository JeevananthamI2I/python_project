import re
import getpass
import bcrypt
from datetime import datetime

class Validation():
    # Validate Account ID
    def get_validated_account_id(self):
        account_id_input = input("Enter your Account ID:\n:: ").strip()
        if not account_id_input.isdigit():
            print("Invalid Account ID. Please enter numeric ID.")
            return None
        return int(account_id_input)

    # Validate Amount
    def get_validated_amount(self,prompt="Enter amount:\n:: "):
        amount_input = input(prompt).strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return None
            return amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return None

    # Validate Mobile Number (10 digits, starts with 6-9)
    def get_validated_mobile_number(self):
        mobile = input("Enter mobile number (10 digits):\n:: ").strip()
        if re.fullmatch(r"[6-9]\d{9}", mobile):
            return mobile
        else:
            print("Invalid mobile number. Must be 10 digits and start with 6-9.")
            return None

    # Validate Date of Birth
    def get_validated_dob(self):
        dob_input = input("Enter date of birth (DD/MM/YYYY):\n:: ").strip()
        try:
            dob = datetime.strptime(dob_input, "%d/%m/%Y").date()
            return dob
        except ValueError:
            print("Invalid date format. Please use DD/MM/YYYY.")
            return None

    # Optional: Validate Password (min 6 chars, at least 1 digit and letter)
    def get_validated_password(self):
        password = input("Enter password (min 6 characters, include letters and numbers):\n:: ").strip()
        if len(password) >= 6 and re.search(r"[A-Za-z]", password) and re.search(r"\d", password):
            return password
        else:
            print("Password too weak. Include letters and numbers, min 6 characters.")
            return None
        

    def hash_password(self,plain_password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    def check_password(self,plain_password, hashed_password_from_db):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password_from_db.encode('utf-8'))

