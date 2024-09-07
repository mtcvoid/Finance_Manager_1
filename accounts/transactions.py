class Transactions:
    CHECKING = 'Checking'
    SAVINGS = 'Savings'
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'

    def __init__(self):
        self.transactions = []
        self.balance = {'Checking_balance': 300, 'Savings_balance': 745}

    def deposit_withdrawal(self, account: str, transaction_type: str, amount: float = 0):
        """
        Adds amount to account_type and updates transaction history.
        """
        if amount < 0 and transaction_type == Transactions.DEPOSIT:
            return f'Cannot deposit a negative amount: {amount}'
        else:
            if transaction_type == Transactions.DEPOSIT:
                if account == Transactions.CHECKING:
                    self.balance['Checking_balance'] += amount
                    self.transactions.append((account, amount))
                elif account == Transactions.SAVINGS:
                    self.balance['Savings_balance'] += amount
                    self.transactions.append((account, amount))
            elif transaction_type == Transactions.WITHDRAWAL:
                if account == Transactions.CHECKING:
                    if self.over_draft_checker(Transactions.CHECKING, amount):
                        self.balance['Checking_balance'] -= amount
                        self.transactions.append((account, -amount))
                    else:
                        return f'${amount} would cause an overdraft. Please choose another amount'
                elif account == Transactions.SAVINGS:
                    if self.over_draft_checker(Transactions.SAVINGS, amount):
                        self.balance['Savings_balance'] -= amount
                        self.transactions.append((account, -amount))
                    else:
                        return f'${amount} would cause an overdraft. Please choose another amount'

    def over_draft_checker(self, account, amount: float):
        if account == Transactions.CHECKING:
            if self.balance['Checking_balance'] - amount >= 0:
                return True
            else:
                return False
        elif account == Transactions.SAVINGS:
            if self.balance['Savings_balance'] - amount >= 0:
                return True
            else:
                return False
