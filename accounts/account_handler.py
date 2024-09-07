"""
WORK IN PROGRESS

youll probably have to change all of these if you are wanting to try and section things out

"""


def account_deposit(account, account_type, amount):
    account.deposit(account_type, amount)


def account_withdrawal(account, account_type, amount):
    account.withdrawal(account_type, amount)


def account_details(account):
    details = account.view_account_details()
    print(details)


def log_in():
    pass
    # Build logic around a login system. You'll need to figure out how to store
    # the objects and pull from that to check object username and password


def email_notifier():
    pass  # think this would be a cool idea. possibly text? figure this out.


def change_password(self):
    pass
