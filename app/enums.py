from enum import Enum

class TransactionType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

class AccountType(Enum):
    SAVINGS = "Savings Account"
    CURRENT = "Current Account"
    FIXED = "Fixed Deposit"
