class TransactionService():
    def __init__(self, transaction_repository):
        self.transaction_repository = transaction_repository

    def create_transaction(self, transaction):
        self.transaction_repository.create_transaction(transaction)

    def get_transaction(self, transaction_id):
        return self.transaction_repository.get_transaction(transaction_id)

    def get_transactions(self):
        return self.transaction_repository.get_transactions()

    def update_transaction(self, transaction_id, transaction):
        self.transaction_repository.update_transaction(transaction_id, transaction)

    def delete_transaction(self, transaction_id):
        self.transaction_repository.delete_transaction(transaction_id)