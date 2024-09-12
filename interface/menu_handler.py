"""
Module for building and handling various user interaction menus for the Finance Manager application.

This module defines functions to display different menu interfaces and handle user choices.
Each menu presents numbered options to the user, and based on their selection, corresponding functions
are executed. The main menu is the entry point, and subsequent submenus can be called from there.

Functions: ----------- - menu_header(header_title): Displays a formatted header for each menu. - menu_choices(
choices_and_functions): Lists the available numbered menu options for the user. - menu_maker(menu_key): Displays a
specified menu and handles user choice selection by calling the corresponding function.

Data Structures: ---------------- - MENU_LIST: A dictionary that maps each menu to a list of numbered tuples. Each
tuple contains a number, a string description of the menu option, and the corresponding function to execute.

Example:
--------
MENU_LIST = {
    'Main Menu': [
        (1, 'Choose Account', choose_account),
        (2, 'Create Account', create_account),
        (3, 'Options', options_menu),
        (4, 'Exit', exit_program)
    ]
}

Dependencies:
-------------
- Requires functions from `interface.user_interaction`, which handles user choice selection (e.g., `get_user_choice`).
"""
from interface.user_interface_transactions import transaction_interaction, transaction_vew_balance
from interface.user_interface_bill_tracker import *
from interface.user_interface_budget import *
from interface.user_interface_market_watch import *
from account_objects.accounts.account_creator import create_new_account_interface
from data_handler.database.data_base_handler import display_account_list




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
    for number, choice, _ in MENU_LIST:
        print(f'({number}) {choice}')
    print("******************************")


def menu_maker(menu_key):
    """
    Displays the menu based on the given key and handles user choice selection.

    Parameters:
    menu_key (str): The key to identify which menu to display from MENU_LIST.

    Returns:
    None
    """
    if menu_key in MENU_LIST:
        header = menu_key
        choices_and_funcs = MENU_LIST[menu_key]
        menu_header(header)
        menu_choices(choices_and_funcs)
        get_user_choice(choices_and_funcs)
    else:
        print(f"Menu '{menu_key}' not found.")


def main_menu():
    if 'Main Menu' in MENU_LIST:
        header = 'Main Menu'
        choices_and_funcs = MENU_LIST['Main Menu']
        menu_header(header)
        menu_choices(choices_and_funcs)
        get_user_choice(choices_and_funcs)


def get_user_choice(choices_and_funcs):
    """
    Prompts the user to select a choice from a list of options, then executes the corresponding function.

    Parameters:
    choices_and_funcs (list): A list of tuples where each tuple contains a number, a string description of the choice,
                              and the function to be executed for that choice.

    Returns:
    None
    """
    while True:
        string_choice = input('Choice: ')

        if string_choice.isdigit():
            int_choice = int(string_choice)

            # Adjust for zero-indexing in Python lists
            if 1 <= int_choice <= len(choices_and_funcs):
                number, description, action = choices_and_funcs[int_choice - 1]

                # Call the function corresponding to the choice
                if callable(action):  # Ensure it's a function
                    action()

                else:
                    print(f"'{description}' is not a valid option.")
            else:
                print("Invalid choice. Please select a valid number.")
        else:
            print("Invalid input. Please enter a number.")

def exit_program():
    pass

MENU_LIST = {
    'Main Menu': [
        (1, 'Choose Account', 'Choose Account'),
        (2, 'Create Account', create_new_account_interface),
        (3, 'Exit', exit_program)
    ],

    'Choose Account': [
        (1, 'Account Name 1', display_account_list),

    ],

    'Create Account': [
        (1, 'Run Create Account Program', create_new_account_interface),
        (2, 'Return to Main Menu', main_menu)  # Return to Main Menu
    ],

    'Chosen-Account Menu': [
        (1, 'View Balances', transaction_vew_balance),
        (2, 'Deposit', transaction_interaction('Deposit')),
        (3, 'Withdrawal', transaction_interaction('Withdrawal')),
        (4, 'View Bill Tracker', 'Bill Tracker'),
        (5, 'View Budget', 'Budgeted'),
        (6, 'Personal Market Watch', 'Personal Market Watch'),
        (7, 'Return to Main Menu', main_menu)
    ],

    'Bill Tracker': [
        (1, 'Add Bill', user_add_bill),
        (2, 'Remove Bill', user_remove_bill),
        (3, 'View Current List of All Bills', user_view_all_bills),
        (4, 'Return to Main Menu', main_menu)
    ],

    'Budgeted': [
        (1, 'Current Budget', user_view_current_budget),
        (2, 'New Budget', user_create_new_budget),
        (3, 'Remove Budget', user_remove_budget),
        (4, 'Update Budget', user_update_budget),
        (5, 'Return to Main Menu', main_menu)
    ],

    'Personal Market Watch': [
        (1, 'Indexes - Global', user_view_global_indexes),
        (2, 'Indexes - By Region', user_view_indexes_by_region),
        (3, 'Set Favorite Index\'s', user_set_favorite_index),
        (4, 'Indexes - Favorites', user_view_favorite_index),
        (5, 'Stocks - Watch List', user_view_stock_watchlist),
        (6, 'Stocks - Add to Watchlist', user_add_to_stock_watchlist),
        (7, 'Search Stock data', user_search_stock_data),
        (8, 'Return to Main Menu', main_menu)  # Return to Main Menu
    ]
}


