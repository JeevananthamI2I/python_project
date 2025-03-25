class TransactionController():
    def __init__(self):
        self.transactions = []
    
    def create_transaction(self, transaction):
        self.transactions.append(transaction)
        return transaction
    
