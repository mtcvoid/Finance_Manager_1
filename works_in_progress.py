account = NewAccount(5555, '1234', 'Mclouse', 'Matthew Clouse',
                     'Checking', 10)





while True:
    print("""
    (1) Log into account
    (2) Create new account.
    """)
    menu_1 = input('Choice: ')
    if menu_1 == '1':
        pass
    if menu_1 == '2':
        pass

    def __init__(self, user_id: int, new_password: str, user_name: str,
                 holder_name: str = "", account_name: str = None,initial_funds: int = 0):
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = user_id
        self.user_name = user_name
        self._user_password = new_password
        self.initial_funds = initial_funds
        self._entire_balance = 0
        self.all_transactions = []
        self._checking_balance = 0
        self.checking_transactions = []
        self._saving_balance = 0
        self.saving_transactions = []
        self.current_budget_warnings = 0

        # TESTING AREA
        matt = create_new_account()
        account_deposit(matt, 'checking', 40)
        account_withdrawal(matt, 'checking', 20)

        tester = matt.get_account_details()
        for key, value in tester.items():
            print(key, value)

#####################################################################################################################

def func_1_tester():

    """ A submenu with its own options """
    submenu_choices_and_funcs = [
        ("Submenu Option 1", submenu_1_func),
        ("Submenu Option 2", submenu_2_func),
        ("Back to Main Menu", None)  # Option to go back
    ]
    menu_builder("Submenu", submenu_choices_and_funcs)


def admin_options():
    print("Admin Options")


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


# Modified menu_builder to handle the 'None' function to exit



# Start with the main menu
main_menu()

