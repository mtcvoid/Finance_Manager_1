"""
PAGE WILL BE DELETED ONCE COMPLETE. COPY AND PASE PAGE

"""

def func_1_tester():

    """ A submenu with its own options """
    submenu_choices_and_funcs = [
        ("Submenu Option 1", submenu_1_func),
        ("Submenu Option 2", submenu_2_func),
        ("Back to Main Menu", None)  # Option to go back
    ]
    menu_builder("Submenu", submenu_choices_and_funcs)



# Main Menu Choices
def main_menu():
    menu_header = "Main Menu"
    main_choices_and_funcs = [
        ("Main Menu Option 1", func_1),
        ("Main Menu Option 2", func_2),
        ("Go to Submenu", submenu),
        ("Exit", None)  # To exit the loop
    ]
    menu_builder(menu_header, main_choices_and_funcs)

from accounts.new_account import *


import Interface.menu_handler
################################################################################


# Save this stuff for later.




# testing area
user_account = create_new_account()

user_account.accounts.deposit('checking', 200)
print(user_account.all_transactions)
print(user_account.holder_name)
