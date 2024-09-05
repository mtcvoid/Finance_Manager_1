class NewAccount:
    """
    Class that takes in a userID, account holder name, type of account(savings, checking, etc, and initial funds.
    account will be able to update funds. Check transactions
    """

    def __init__(self, user_id: int, new_password: str, user_name: str,
                 holder_name: str = "", account_name: str = None,initial_funds: int = 0):
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = user_id
        self.user_name = user_name
        self._user_password = new_password
        self.initial_funds = initial_funds
        self._entire_balance = initial_funds
        self.all_transactions = []
        self._checking_balance = 0
        self.checking_transactions = []
        self._saving_balance = 0
        self.saving_transactions = []
        self.current_budget_warnings = 0


    @property
    def user_id(self):
        """
        returns user ID for validation with database.
        """
        return self._user_id

    @property
    def account_name(self):
        """
        returns account name that can be used to help with searching database/json documents.
        """
        return self._account_name

    @property
    def accounts_balance(self):
        """
        Returns balance of both checking and savings accounts.
        """
        return self._entire_balance

    @property
    def checking_balance(self):
        """
        Returns balance of checking account.
        """
        return self._checking_balance

    @property
    def savings_balance(self):
        """
        Returns balance of savings account.
        """
        return self._saving_balance

    @account_name.setter
    def account_name(self, value):
        """
        Setter property that can be used when changing account name from checking to savings or visa versa
        """
        self._account_name = value

    @user_id.setter
    def user_id(self, value):
        """
        Used for ADMIN purposes only. If needing to change user ID for some reason you can. NOT A GOOD IDEA. database
        will not update automatically. You will need to pull ALL info from database before changing userID then re-write
        to database. CURRENTLY, NOT IMPLEMENTED. And probably won't be. someone will fuck up and lose data.

        """
        self._user_id = value

    def view_account_details(self):
        """
        Prints account details to user.
        """
        return (f"""
********************************
Account ID: {self._user_id}
Account Holder: {self.holder_name}
Total account Balance: {self._entire_balance}
********************************""")

    def get_account_details(self):
        """
        Returns a dictionary value of account details.
        """
        return {'User ID': self._user_id, 'Account Holder Name': self.holder_name,
                'Overall Balance': self._entire_balance}

    def deposit(self, account_type, amount: float = 0):
        """
        Adds amount to account_type and updates transaction history.
        """
        if account_type == 'Checking':
            self._checking_balance += amount
            self.checking_transactions.append(amount)
            self.all_transactions.append(amount)
        elif account_type == "Savings":
            self._saving_balance += amount
            self.saving_transactions.append(amount)
            self.all_transactions.append(amount)
        else:
            print('Please enter a valid account.')

    # you may need to mess with this more once implemented. Not sure if it should handle all the text to user.
    def withdrawal(self, account_type, amount: float = 0):
        """
        Withdrawals amount from account_type and updates transaction history
        """
        if account_type == 'Savings':
            while True:
                if (self._saving_balance - amount) >= 0:
                    self._saving_balance -= amount
                    self.saving_transactions.append(amount)
                    self.all_transactions.append(amount)
                    print(f'${amount} has been removed from {account_type}. Current balance: {self._saving_balance}')
                    break
                else:
                    print('The amount requested is more than current account value.')
        elif account_type == 'Checking':
            while True:
                if (self._checking_balance - amount) >= 0:
                    self._checking_balance -= amount
                    self.checking_transactions.append(amount)
                    self.all_transactions.append(amount)
                    print(f'${amount} has been removed from {account_type}. Current balance: {self._saving_balance}')
                    break
                else:
                    print('The amount requested is more than current account value.')

    # need to implement
    def change_password(self):
        pass

    # need to implement
    def change_account_holder(self):
        pass

# def budget_warnings(self, amount):
#   pass  # set up 4 tiers. with warnings so you know when you go over budget.
