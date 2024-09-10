"""
Module for building and handling various user interaction menus for the Finance Manager application.

This module defines functions to display different menu interfaces and handle user choices.
Each menu presents options to the user, and based on their selection, corresponding functions
are executed. The main menu is the entry point, and subsequent submenus can be called from there.

Functions:
-----------
- menu_header(header_title): Displays a formatted header for each menu.
- menu_choices(choices_and_functions): Lists the available menu options for the user.
- main_menu(): Displays the main menu and handles the user's choice.
- main_menu_options(): Displays the main options submenu.
- account_main_menu(): Displays the account management menu.
- account_options_menu(): Displays additional account options.
- admin_options_menu(): Displays the admin options menu.
- market_watch_menu(): Displays the stock market watch menu.
- bill_tracking_menu(): Displays the bill tracking menu.

Dependencies:
-------------
- Requires functions from `Interface.user_interaction`, which handles user choice selection (e.g., `get_user_choice`).
"""

from Interface.user_interaction import *


def menu_header(header_title):
    """
    Displays a formatted header for a menu.

    Parameters:
    header_title (str): The title to display at the top of the menu.

    Returns:
    None
    """
    print(f"""
       #####Finance Manager#####
    ******************************
             {header_title}
    ******************************""")


def menu_choices(choices_and_functions):
    """
    Displays the menu options for the user.

    Parameters:
    choices_and_functions (list): A list of tuples, where each tuple contains a menu option
                                  (str) and a corresponding function.

    Returns:
    None
    """
    for index, (choice, _) in enumerate(choices_and_functions, start=1):
        print(f'({index}) {choice}')
    print("******************************")


def main_menu():
    """
    Displays the main menu and handles the user's choice.

    Presents options to the user, and executes the corresponding function based on their input.

    Returns:
    None
    """
    header = 'Main Menu'
    choices_and_funcs = [('View options', main_menu_options)]
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def main_menu_options():
    """
    Displays the submenu for main options.

    Returns:
    None
    """
    header = 'Main Options'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def account_main_menu():
    """
    Displays the account management menu.

    Returns:
    None
    """
    header = 'Account Management'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def account_options_menu():
    """
    Displays additional options for account management.

    Returns:
    None
    """
    header = 'Account Options'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def admin_options_menu():
    """
    Displays the admin options menu.

    Returns:
    None
    """
    header = 'Admin Options'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def market_watch_menu():
    """
    Displays the stock market watch menu.

    Returns:
    None
    """
    header = 'Stock Market Watcher'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)


def bill_tracking_menu():
    """
    Displays the bill tracking menu.

    Returns:
    None
    """
    header = 'Bill Tracking'
    choices_and_funcs = []
    menu_header(header)
    menu_choices(choices_and_funcs)
    get_user_choice(choices_and_funcs)



