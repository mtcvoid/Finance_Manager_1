class Transactions:
    CHECKING = 'Checking'
    SAVINGS = 'Savings'
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'

    def __init__(self):
        self.transactions = []
        self.balance = {'Checking_balance': 0, 'Savings_balance': 0}

    def deposit_withdrawal(self, account: str, transaction_type: str, amount: float = 0):
        """
        Processes a deposit or withdrawal transaction for a specified account type.

        This method handles two types of accounts: 'Checking' and 'Savings'. It supports
        two transaction types: 'Deposit' and 'Withdrawal'. If a deposit is made, the amount
        is added to the specified account. If a withdrawal is made, the method checks if
        the withdrawal amount would cause an overdraft and either processes the transaction
        or returns a warning if insufficient funds are available.

        example:
        deposit_withdrawal('Checking','Deposit', 120.34)

        :param account:
        :param transaction_type:
        :param amount:
        :return:
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

    def money_transfer(self):
        pass
