import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

from db.database import Database
# from models.customer import Customer

class CustomerRepository():
    def __init__(self):
        self.db = Database()
        # self.customer = Customer()
        self.table = "customers"
        self.columns = ["customer_id", "name", "mobile", "address", "dob", "password", "created_at", "updated_at"]
    
    def customer_create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS customers (
        customer_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        mobile TEXT NOT NULL,
        address TEXT NOT NULL,
        dob DATE,
        password TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        """
        return self.db.execute(query)

    def get(self, customer_id):
        query = f"SELECT * FROM {self.table} WHERE customer_id = %s"
        self.db.execute(query, (customer_id,))
        return self.db.fetch_one()
    
    def customer_create(self, customer):
        query = f"INSERT INTO {self.table} (name, mobile, address, dob) VALUES (%s, %s, %s, %s) RETURNING customer_id;"
        self.db.execute(query, (customer["name"], customer["mobile"], customer["address"], customer["dob"]))
        return self.db.fetch_one()
    

    def update(self, customer_id, customer):
        query = f"UPDATE {self.table} SET name=%s, mobile=%s, address=%s WHERE customer_id = %s RETURNING customer_id"
        self.db.execute(query, (customer.name, customer.mobile, customer.address, customer_id))
        return self.db.fetch_one()
    
    def delete(self, customer_id):
        query = f"DELETE FROM {self.table} WHERE customer_id = %s RETURNING customer_id"
        self.db.execute(query, (customer_id))
        return self.db.fetch_one()
    
    def add_register_password(self, customer_id, password):
        query = f"""UPDATE {self.table} SET password=%s WHERE customer_id=%s"""
        self.db.execute(query,(password, customer_id))
    
    def alter_customers_table(self):
        query =f"""ALTER TABLE customers ADD COLUMN password TEXT """
        self.db.execute(query)

# cr = CustomerRepository()
# customer = {"name":"aaaa", "mobile":"8902300320", "address":"Guindy", "dob": "2000-11-11"}
# cr.customer_create(customer)

