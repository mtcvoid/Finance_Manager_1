import random


class NewAccount:
    """
    Class that takes in a userID, account holder name, type of account(savings, checking, etc.), and initial funds.
    account will be able to update funds. Check transactions.
    """

    def __init__(self, user_name: str, new_password: str,
                 holder_name: str = "", account_name: str = None):
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = random.randint(1, 31000)  # this will be used as an ID . All objects will be named account?
        self.user_name = user_name
        self._user_password = new_password
        self._entire_balance = 0
        self.all_transactions = []
        self._checking_balance = 0
        self.checking_transactions = []
        self._saving_balance = 0
        self.saving_transactions = []
        self.current_budget_warnings = 0

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
        # need to figure out the decimal place thing.
        """
        Returns a dictionary value of account details for admin purposes. Use this when
        manipulating and moving data. This will have more info than the view_account_details
        """
        return {'User ID': self._user_id, 'Account Holder Name': self.holder_name,
                'Overall Balance': self._entire_balance, 'User name': self.user_name,
                'User password': self._user_password, 'Transaction History': self.all_transactions,
                f'Checking Balance': self._checking_balance, 'Savings Balance': self._saving_balance,
                'Current Budget Warnings': self.current_budget_warnings}

    def deposit(self, account_type, amount: float = 0):
        """
        Adds amount to account_type and updates transaction history.
        """
        if account_type == 'checking':
            self._checking_balance += amount
            self.checking_transactions.append(amount)
            self.all_transactions.append(amount)
            self._entire_balance += amount
        elif account_type == "savings":
            self._saving_balance += amount
            self.saving_transactions.append(amount)
            self.all_transactions.append(amount)
            self._entire_balance += amount
        else:
            print('Please enter a valid account.')

    # you may need to mess with this more
    def withdrawal(self, account_type, amount: float = 0):
        """
        Withdrawals amount from account_type and updates transaction history
        """
        if account_type == 'savings':
            while True:
                if (self._saving_balance - amount) >= 0:
                    self._saving_balance -= amount
                    self.saving_transactions.append(-amount)
                    self.all_transactions.append(-amount)
                    self._entire_balance -= amount
                    print(f'${amount} has been removed from {account_type}. Current balance: {self._saving_balance}')
                    break
                else:
                    print('The amount requested is more than current account value.')
        elif account_type == 'checking':
            while True:
                if (self._checking_balance - amount) >= 0:
                    self._checking_balance -= amount
                    self.checking_transactions.append(-amount)
                    self.all_transactions.append(-amount)
                    self._entire_balance -= amount
                    print(f'${amount} has been removed from {account_type}. Current balance: {self._checking_balance}')
                    break
                else:
                    print('The amount requested is more than current account value.')

    # need to implement
    def change_password(self):
        pass

    # need to implement
    def change_account_holder(self):
        pass


def create_new_account():
    while True:
        print(f"""
                   ####Finance Manager####
                *****************************
                      Account Creation
                *****************************
The following information will be required for creating a new account. 
        Please review all information for accuracy. 
                            **
       - Account username and password for logging into account.
       - Account holder full name.
       - A name for the Account. (Ex: John's Investment account)
            L All account's come with a checking and a savings
       - Initial fund's
                            **
""")
        while True:
            y_n = input('Create a new account? (Y)es, (N)o')
            if y_n.lower() == 'y':
                user_name = new_account_getter("Username")
                new_password = new_account_getter('Password')
                holder_name = new_account_getter("Account holder name")
                account_name = new_account_getter('Name for the account')
                break

        account = NewAccount(user_name, new_password, holder_name, account_name)
        print('Account Created')
        return account


def new_account_getter(getter_type: str):
    routine_running = True
    while routine_running:
        getter = input(f'Please enter a {getter_type}: ')
        y_n = input(f'Is this correct: {getter}. (Y)es, (N)o')
        if y_n.lower() == 'y':
            return getter
        elif y_n.lower() == 'n':
            print('Please try again.')
            continue
        else:
            print('Please Enter a valid choice.')
            o_t = input("""
(1)Try again
(2)Exit to main Interface
                               """)
            if o_t == '1':
                continue
            else:
                routine_running = False
                # main_menu() # make this

# def budget_warnings(self, amount):
#   pass  # set up 4 tiers. with warnings so you know when you go over budget.
