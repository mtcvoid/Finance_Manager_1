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

def func_1():
    print("Function 1 from Main Menu")


def func_2():
    print("Function 2 from Main Menu")


def submenu_1_func():
    print("You are in Submenu 1")


def submenu_2_func():
    print("You are in Submenu 2")


def submenu():
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
def menu_builder(menu_header, choices_and_funcs):
    """
    Displays a menu and calls the appropriate function based on the user's choice.

    :param menu_header: Header for the menu
    :param choices_and_funcs: List of tuples where each tuple contains a menu choice and its corresponding function
    """
    while True:
        print(f"""
      #####Finance Manager#####
******************************
        {menu_header}
******************************""")

        # Dynamically print the menu choices
        for index, (choice, _) in enumerate(choices_and_funcs, start=1):
            print(f"({index}) {choice}")

        print("******************************")

        u_c = input('Choice: ')

        if u_c.isdigit():  # Check if input is a number
            u_c = int(u_c)
            if 1 <= u_c <= len(choices_and_funcs):
                choice, func = choices_and_funcs[u_c - 1]
                if func:  # Only call the function if it's not None
                    func()
                else:
                    print("Exiting...")
                    break
            else:
                print("Invalid choice. Please select a valid option.")
        elif u_c == 'admin':  # Admin option
            admin_options()
        else:
            print("Invalid input. Please enter a number corresponding to a choice.")
        break


# Start with the main menu
main_menu()

