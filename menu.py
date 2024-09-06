from accounts.new_account import NewAccount



"""
All account functions
"""
def create_new_account():# build the logic for this so someone can actually make an account.
    account = NewAccount(76487293, 'ReAlLyBaDPaSS', 'Mr_Banker2024', 'Matthew tester',
                         'Checking/Savings', 234.98)
    return account



def log_in():
    user_name = input('Username: ')
    pass_word = input('Password: ')
    # Build logic around a login system. You'll need to figure out how to store
    # the objects and pull from that to check object username and password


"""
All functions for account manipulation. 
"""

def account_details(account):
    details = account.view_account_details()
    print(details)


def account_deposit(account, account_type, amount):
    account.deposit(account_type, amount)


def account_withdrawal(account, account_type, amount):
    account.withdrawal(account_type, amount)


"""
All functions for menu building
"""


def account_options_menu(): # have this inside the login menu. Not the main menu
    pass


def admin_options_menu():
    pass


def market_watch_menu():
    pass  # this is a cool idea for later implementation. Will be nifty i think. everything in one app.




def menu_builder(menu_header: str, choices_and_funcs):
    """
    Displays a menu and calls the appropriate function based on the user's choice.
    """
    while True:
        print(f"""
   #####Finance Manager#####
******************************
         {menu_header}
******************************""")
        for index, (choice, _) in enumerate(choices_and_funcs, start=1):
            print(f'({index}) {choice}')

        print("******************************")

        u_c = input('Choice: ')

        if u_c.isdigit():
            u_c = int(u_c)
            if 1 <= u_c <= choices_and_funcs:
                choice, func = choices_and_funcs[u_c, -1]
                if func:  # only call the function if it's not none. Will get you out of loop
                    func()
                else:
                    print('Exiting...')
                    break
            else:
                print('Invalid choice. Please select a valid option.')
        elif u_c == 'Admin':
            admin_options_menu()
        else:
            print('Invalid input. Please enter a number corresponding to a choice.')
            break



#testing area

