import sys 
sys.path.append('C:\\PythonLearning\\bank_management\\app')

import logging
import json
from datetime import datetime,date
from services.transaction_service import TransactionService

logger = logging.getLogger(__name__)

class TransactionController:
    def __init__(self):
        self.transactions = []
        self.transaction_service= TransactionService()

    def view_transaction(self, start_date,end_date,customer_id):
        try:
            transaction_data= self.transaction_service.get_transaction(start_date,end_date,customer_id)
            # result= self.clean_and_print_transaction(transaction_data)
            # logger.info(f"Transaction created: {result}")
            return transaction_data
        except Exception as e:
            logger.error(f"Error creating transaction: {e}")
            raise Exception("Transaction creation failed.") from e
        
        
    # def clean_and_print_transaction(self,transactions):
    #     cleaned_list = []
    #     for transaction in transactions:
    #         transaction_date = transaction['transaction_date']
    #         if isinstance(transaction_date, str):
    #             try:
    #                 transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")
    #             except ValueError:
    #                 raise ValueError(f"Invalid date format: {transaction_date}")
    #         cleaned_transaction = {
    #             "Transaction ID": transaction['transaction_id'],
    #             "Account ID": transaction['account_id'],
    #             "Mobile": transaction['transaction_type'],
    #             "Address": transaction['amount'],
    #             "Date": transaction_date.strftime("%Y-%m-%d"),
    #         }
    #         cleaned_list.append(cleaned_transaction)

    #     print(json.dumps(cleaned_list, indent=4))
