class Transactions:
    CHECKING = 'checking'
    SAVINGS = 'savings'
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'

    def __init__(self):
        """
        Initializes a new Transactions object with empty transaction history and zero balance for both Checking
        and Savings accounts.

        Attributes:
            transactions (list): A list to store tuples of transactions in the format (account, amount).
            balance (dict): A dictionary storing the current balance of both Checking and Savings accounts.
        """
        self.transactions = []
        self.balance = {'Checking_balance': 0, 'Savings_balance': 0}

    def deposit_withdrawal(self, account: str, transaction_type: str, amount: float = 0):
        """
        Processes a deposit or withdrawal transaction for a specified account type.

        This method supports two account types: 'Checking' and 'Savings', and two transaction types: 'Deposit'
        and 'Withdrawal'.
        - For a deposit, the amount is added to the specified account.
        - For a withdrawal, the method checks if there are sufficient funds before processing.

        If a withdrawal causes an overdraft, a warning message is returned, and the transaction is not processed.

        Example:
            deposit_withdrawal('Checking', 'Deposit', 120.34)

        Args:
            account (str): The account type, either 'Checking' or 'Savings'.
            transaction_type (str): The type of transaction, either 'Deposit' or 'Withdrawal'.
            amount (float, optional): The amount of money to deposit or withdraw (default is 0).

        Returns:
            str or None: A warning message if the withdrawal would cause an overdraft, otherwise None.
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
        """
        Checks if the account has sufficient funds for a withdrawal.

        This method verifies if the withdrawal from the specified account would result in a negative balance.

        Args:
            account (str): The account type to check, either 'Checking' or 'Savings'.
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the account has enough balance for the withdrawal, False if it would result in an overdraft.
        """
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

    def money_transfer(self,transfer_account: str,  amount: float):
        """
        Transfers money between Checking and Savings accounts.

        This method allows the user to transfer funds between their Checking and Savings accounts. The balance
        of one account is decreased by the specified amount, while the balance of the other account is increased
        by the same amount.

        Example:
            money_transfer('Checking', 100.0)

        Args:
            transfer_account (str): The account to transfer money from. Should be 'Checking' to transfer from
            Checking to Savings, or 'Savings' to transfer from Savings to Checking.
            amount (float): The amount to transfer.

        Returns:
            None
        """
        if transfer_account == 'Checking':
            self.balance['Checking_balance'] -= amount
            self.balance['Savings_balance'] += amount
        elif transfer_account == 'Savings':
            self.balance['Savings_balance'] -= amount
            self.balance['Checking_balance'] += amount

    def view_balances(self):
        pass
