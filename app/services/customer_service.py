class CustomerService():
    def __init__(self):
        self.customer_list = []
    
    def add_customer(self, customer):
        self.customer_list.append(customer)
    
    def get_all_customers(self):
        return self.customer_list
    
    def get_customer_by_id(self, customer_id):
        for customer in self.customer_list:
            if customer.get_customer_id() == customer_id:
                return customer
        return None
    
    def update_customer(self, customer):
        for index, c in enumerate(self.customer_list):
            if c.get_customer_id() == customer.get_customer_id():
                self.customer_list[index] = customer
                return True
        return False
    
    def delete_customer(self, customer_id):
        for index, customer in enumerate(self.customer_list):
            if customer.get_customer_id() == customer_id:
                del self.customer_list[index]
                return True
        return False