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


def log_in():
    pass  # needs to return validation from password checker.


def log_out():
    pass


def account_details(account):
    details = account.view_account_details()
    print(details)


def account_deposit():
    pass


def account_withdrawal():
    pass


def account_options():
    pass


def create_new_account():
    account = NewAccount(5555, '1234', 'mtester', 'Matthew tester',
                         'Checking', 10)
    return account


def admin_options():
    pass


def market_watch():
    pass  # this is a cool idea for later implementation. Will be nifty i think. everything in one app.


matt = create_new_account()

account_details(matt)
