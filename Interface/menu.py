from accounts.new_account import *


import Interface.menu_handler


def log_in():
    user_name = input('Username: ')
    pass_word = input('Password: ')
    # Build logic around a login system. You'll need to figure out how to store
    # the objects and pull from that to check object username and password


def email_notifier():
    pass  # think this would be a cool idea. possibly text? figure this out.


# testing area
user_account = create_new_account()

user_account.accounts.deposit('checking', 200)
print(user_account.all_transactions)
print(user_account.holder_name)
