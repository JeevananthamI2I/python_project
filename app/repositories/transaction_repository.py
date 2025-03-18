from  app.db.database import Database

class TransactionRepository():
    def __init__(self):
        self.db = Database()
        self.table = "transactions"
        self.columns = ["transaction_id", "account_id", "amount", "transaction_type", "transaction_date"]

    def get(self, transaction_id):
        query = f"SELECT * FROM {self.table} WHERE transaction_id = %s"
        self.db.execute(query, (transaction_id,))
        return self.db.fetch_one()
    
    def create(self, transaction):
        query = f"INSERT INTO {self.table} (account_id, amount, transaction_type, transaction_date) VALUES (%s, %s, %s, %s) RETURNING transaction_id"
        self.db.execute(query, (transaction.account_id, transaction.amount, transaction.transaction_type, transaction.transaction_date))
        return self.db.fetch_one()
    
    def update(self, transaction_id, transaction):
        query = f"UPDATE {self.table} SET account_id=%s, amount=%s, transaction_type=%s, transaction_date=%s WHERE transaction_id = %s RETURNING transaction_id"
        self.db.execute(query, (transaction.account_id, transaction.amount, transaction.transaction_type, transaction.transaction_date, transaction_id))
        return self.db.fetch_one()
    
    def delete(self, transaction_id):
        query = f"DELETE FROM {self.table} WHERE transaction_id = %s RETURNING transaction_id"
        self.db.execute(query, (transaction_id,))
        return self.db.fetch_one()
    
    def all(self):
        query = f"SELECT * FROM {self.table}"
        self.db.execute(query)
        return self.db.fetch_all()
    
    def get_transactions_by_account_id(self, account_id):
        query = f"SELECT * FROM {self.table} WHERE account_id = %s"
        self.db.execute(query, (account_id,))
        return self.db.fetch_all()
    
    def get_total_transactions_by_account_id(self, account_id):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE account_id = %s"
        self.db.execute(query, (account_id,))
        return self.db.fetch_one()
    
    def get_total_amount_by_account_id(self, account_id):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE account_id = %s"
        self.db.execute(query, (account_id,))
        return self.db.fetch_one()
    
    def get_total_amount_by_account_id_and_transaction_type(self, account_id, transaction_type):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE account_id = %s AND transaction_type = %s"
        self.db.execute(query, (account_id, transaction_type))
        return self.db.fetch_one()
    
    def get_total_amount_by_transaction_type(self, transaction_type):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE transaction_type = %s"
        self.db.execute(query, (transaction_type,))
        return self.db.fetch_one()
    
    def get_total_transactions_by_transaction_type(self, transaction_type):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE transaction_type = %s"
        self.db.execute(query, (transaction_type,))
        return self.db.fetch_one()
    
    def get_total_transactions(self):
        query = f"SELECT COUNT(*) FROM {self.table}"
        self.db.execute(query)
        return self.db.fetch_one()
    
    def get_total_amount(self):
        query = f"SELECT SUM(amount) FROM {self.table}"
        self.db.execute(query)
        return self.db.fetch_one()
    
    def get_total_amount_by_date(self, date):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE transaction_date = %s"
        self.db.execute(query, (date,))
        return self.db.fetch_one()
    
    def get_total_transactions_by_date(self, date):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE transaction_date = %s"
        self.db.execute(query, (date,))
        return self.db.fetch_one()
    
    def get_total_amount_by_date_range(self, start_date, end_date):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE transaction_date BETWEEN %s AND %s"
        self.db.execute(query, (start_date, end_date))
        return self.db.fetch_one()
    
    def get_total_transactions_by_date_range(self, start_date, end_date):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE transaction_date BETWEEN %s AND %s"
        self.db.execute(query, (start_date, end_date))
        return self.db.fetch_one()
    
    def get_total_amount_by_account_id_and_date(self, account_id, date):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE account_id = %s AND transaction_date = %s"
        self.db.execute(query, (account_id, date))
        return self.db.fetch_one()
    
    def get_total_transactions_by_account_id_and_date(self, account_id, date):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE account_id = %s AND transaction_date = %s"
        self.db.execute(query, (account_id, date))
        return self.db.fetch_one()
    
    def get_total_amount_by_account_id_and_date_range(self, account_id, start_date, end_date):
        query = f"SELECT SUM(amount) FROM {self.table} WHERE account_id = %s AND transaction_date BETWEEN %s AND %s"
        self.db.execute(query, (account_id, start_date, end_date))
        return self.db.fetch_one()
    
    def get_total_transactions_by_account_id_and_date_range(self, account_id, start_date, end_date):
        query = f"SELECT COUNT(*) FROM {self.table} WHERE account_id = %s AND transaction_date BETWEEN %s AND %s"       
        self.db.execute(query, (account_id, start_date, end_date))
        return self.db.fetch_one()