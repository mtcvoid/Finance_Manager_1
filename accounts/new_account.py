import random


class Account:
    """
    Class that takes in a userID, account holder name, type of account(savings, checking, etc.), and initial funds.
    account will be able to update funds. Check transactions.
    """

    def __init__(self, user_name: str, new_password: str,
                 holder_name: str = "", account_name: str = None):
        """
        Takes in username, password, account holder name, and name of the account.
        :param user_name:
        :param new_password:
        :param holder_name:
        :param account_name:
        """
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = random.randint(1, 31000)  # this will be used as an ID . All objects will be named account?
        self.user_name = user_name
        self._user_password = new_password
        self.transactions = []
        self.current_budget_warnings = 0

    def view_account_details(self,checking_balance, savings_balance):
        """
        Prints account details to user.
        """
        return (f"""
********************************
Account ID: {self._user_id}
Account Holder: {self.holder_name}
Checking Balance: {checking_balance}
Savings Balance: {savings_balance}
********************************""")

    def get_account_details(self,checking_balance, savings_balance, trans_history):
        """
        Returns a dictionary containing the detailed account information for administrative purposes.

        This method provides a comprehensive view of the account details, including the user ID,
        account holder name, username, password, transaction history, checking and savings balances,
        and any current budget warnings. It is intended for backend operations such as data manipulation
        or retrieval by administrators.

        Parameters:
        -----------
        checking_balance : float
            The current balance of the checking account.

        savings_balance : float
            The current balance of the savings account.

        trans_history : list
            A list of the transaction history associated with the account.

        :param checking_balance:
        :param savings_balance:
        :param trans_history:
        :return:
        """
        return {'User ID': self._user_id, 'Account Holder Name': self.holder_name, 'User name': self.user_name,
                'User password': self._user_password, 'Transaction History': trans_history,
                'Checking Balance': checking_balance, 'Savings Balance': savings_balance,
                'Current Budget Warnings': self.current_budget_warnings}


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

        account = Account(user_name, new_password, holder_name, account_name)
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
