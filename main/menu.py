from accounts.new_account import NewAccount

"""
All account functions
"""


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


def bill_tracking():
    pass


def email_notifier():
    pass  # think this would be a cool idea. possibly text? figure this out.


"""
All functions for menu building
"""


def account_main_menu():
    pass


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
(2)Exit to main menu
                               """)
            if o_t == '1':
                continue
            else:
                routine_running = False
                # main_menu() # make this


def account_options_menu():  # have this inside the login menu. Not the main menu
    pass


def admin_options_menu():
    pass


def market_watch_menu():
    pass  # this is a cool idea for later implementation. Will be nifty I think. everything in one app.


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


# testing area
user_account = create_new_account()

user_account.deposit('checking',200)
print(user_account.all_transactions)
print(user_account.holder_name)
