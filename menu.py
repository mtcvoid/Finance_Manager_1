from accounts.new_account import NewAccount

"""
Menu for navigating different functions and classes for the finance manager application.

 menu
    - log in
        -username
        -password
            - account details
                -account list with totals.
                -transaction history
            - deposit
                -from account:
                    - how much
                        -account details before and after deposit
            - withdrawal
                -from account:
                    -how much
                        - account details before and after withdrawal
            - account options
                -change username
                -change password
                -delete account
                    - add requirements for account deletion (no money in account)
                    - make sure and admin has to approve of account deletion.
                -add verified user
            -
    -view options
        -admin options
        -user options

    -MarketWatch
        - Add utilities to look at current market state. can use indexes. possible start having a saved list* of stocks.
        - add portfolio management. Will need to use selenium to log into profiles and pull data from page.
    -exit
    
    
    
    
    
    *****CURRENTLY UNDER CONSTRUCTION******
"""


def menu_builder(menu_header: str, choices_and_funcs: list):
    """
    Displays a menu and calls the appropriate function based on the user's choice.
    """


def log_in():
    user_name = input('Username: ')
    pass_word = input('Password: ')
    # Build logic around a login system. You'll need to figure out how to store
    # the objects and pull from that to check object username and password


def account_details(account):
    details = account.view_account_details()
    print(details)


def account_deposit(account, account_type, amount):
    account.deposit(account_type, amount)


def account_withdrawal(account, account_type, amount):
    account.withdrawal(account_type, amount)


def account_options_menu():
    pass


def create_new_account():
    account = NewAccount(76487293, 'ReAlLyBaDPaSS', 'Mr_Banker2024', 'Matthew tester',
                         'Checking/Savings', 234.98)
    return account


def admin_options_menu():
    pass


def market_watch_menu():
    pass  # this is a cool idea for later implementation. Will be nifty i think. everything in one app.


def view_options_menu():
    pass
