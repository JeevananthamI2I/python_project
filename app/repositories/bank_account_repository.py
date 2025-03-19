import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from db.database import Database
from models.bank_account import BankAccount
from models.customer import Customer

class BankAccountRepository():
    def __init__(self):
        self.db = Database()
        # self.customer = Customer()
        self.table = "accounts"
        self.columns = ["account_id", "account_number", "type", "balance", "customer_id", "created_at", "updated_at"]
    def create_enum(self):
        query = """CREATE TYPE bank_account_enum AS ENUM ('Savings Account', 'Current Account');
        """
        return self.db.execute(query)
    
    def create_table(self):
        query = """
        CREATE TABLE accounts (
        account_id SERIAL PRIMARY KEY,
        customer_id INT NOT NULL,
        account_number INT NOT NULL UNIQUE,
        account_type bank_account_enum NOT NULL,
        balance NUMERIC DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            ON DELETE CASCADE
        );


        """
        return self.db.execute(query)

BR = BankAccountRepository()
# BR.create_enum()
BR.create_table()