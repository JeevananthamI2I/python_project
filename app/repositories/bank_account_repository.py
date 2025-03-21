import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from db.database import Database
from models.bank_account import BankAccount
from models.customer import Customer

class BankAccountRepository():
    def __init__(self):
        self.db = Database()
        self.table = "accounts"
        self.columns = ["account_id", "account_number", "type", "balance", "customer_id", "created_at", "updated_at"]
    
    def create_enum(self):
        query = """CREATE TYPE bank_account_enum AS ENUM ('Savings Account', 'Current Account');
        """
        return self.db.execute(query)

    def add_bank_account(self, account_data):
        query =f"""INSERT INTO accounts (account_number,customer_id,balance,account_type) VALUES (%s,%s,%s,%s) RETURNING account_id"""
        result = self.db.execute_and_return(query,(account_data.account_number,account_data.customer_id,account_data.balance,account_data.account_type))
        return result[0]
    
    def update_account_number(self, account_id, account_number):
        query = f"UPDATE {self.table} SET account_number = %s WHERE account_id = %s RETURNING account_number"
        return self.db.execute_and_return(query, (account_number, account_id))

    def retrive_balance(self, account_number):  
        print(account_number)  
        query =f""""SELECT a.account_number AND a.balance ,COALESCE(SUM(t.amount),0) FROM {self.table} a
        LEFT JOIN transaction t ON a.account_number= t.account_number AND t.transaction_type='DEPOSIT'
        WHERE a.account_number=%s
        GROUP BY a.account_number AND a.balance"""
        self.db.execute(query, (account_number))
        return self.db.fetch_one()
    
    def doposit(self, amount, account_number):
        query =f"""UPDATE {self.table} SET amount=%s WHERE account_number=%s RETUNING customer_id """
        return self.db.execute_and_return(query,(amount,account_number))
    
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
        is_deleted BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            ON DELETE CASCADE
        );


        """
        return self.db.execute(query)

    def alter_accounts_table(self):
        query =f"""ALTER TABLE accounts ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE """
        self.db.execute(query)

# BR = BankAccountRepository()
# BR.create_enum()
# BR.create_table()
# BR.alter_accounts_table()
# BR.retrive_balance()