"""
Module for handling user input validation and menu selection.

This module provides functions that allow for:
- Validating user input with confirmation steps
- Offering retry or exit choices during input processes
- Managing user selections from a menu, where each selection is tied to a specific function

Functions:
-----------
- input_with_validation(field_name): Prompts the user for input, validates it through confirmation, and handles retry or exit.
- get_user_confirmation(prompt): Asks the user to confirm their input ('Y' for Yes, 'N' for No).
- get_retry_or_exit_choice(): Offers the user a choice to retry entering input or exit the process.
- get_user_choice(choices_and_funcs): Displays menu options, captures the user's choice, and executes the corresponding function.

Intended Usage:
---------------
This module can be used in applications that require input validation from the user and
menu-based interfaces where user selections trigger specific functionality.

Example:
--------
main_choices_and_funcs = [('LOG IN', log_in), ('View options', main_menu_options)]
get_user_choice(main_choices_and_funcs)

Dependencies:
-------------
None.

"""


def input_with_validation(field_name):
    """
    Prompts the user to enter a value for the specified field and validates the input by
    allowing the user to confirm or retry the input.

    Parameters:
    field_name (str): The name of the field for which input is required.

    Returns:
    str: The user's validated input if confirmed.
    None:
    """
    while True:
        user_input = input(f'Please enter {field_name}: ')
        if get_user_confirmation(f'Is this correct: {user_input}? (Y)es, (N)o'):
            return user_input
        else:
            retry_or_exit = get_retry_or_exit_choice()
            if retry_or_exit == 'exit':
                return None  # User decided to cancel


def get_user_confirmation(prompt):
    """
    Asks the user to confirm their input.

    Parameters:
    prompt (str): The confirmation message to display to the user.

    Returns:
    bool: True if the user confirms with 'Y', False if the user declines with 'N'.
    """
    while True:
        choice = input(prompt).lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid choice, please enter (Y)es or (N)o.')


def get_retry_or_exit_choice():
    """
    Asks the user if they want to retry entering input or exit the process.

    Returns:
    str: 'retry' if the user wants to try entering input again.
         'exit' if the user chooses to exit the process.
    """
    while True:
        choice = input("(1) Try again\n(2) Exit to main interface\nEnter choice: ")
        if choice == '1':
            return 'retry'
        elif choice == '2':
            return 'exit'
        else:
            print('Invalid choice. Please select 1 or 2.')


def get_user_choice(choices_and_funcs):
    """
    Prompts the user to select a choice from a list of options, then executes the corresponding function.

    Parameters:
    choices_and_funcs (list): A list of tuples where each tuple contains a string description of the choice
                              and the function to be executed for that choice.

    Returns:
    None
    """
    while True:
        string_choice = input('Choice: ')
        int_choice = int(string_choice)
        _, func_choice = choices_and_funcs[int_choice - 1]
        func_choice()
