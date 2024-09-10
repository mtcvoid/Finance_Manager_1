
def input_with_validation(field_name):
    """
    Handles input validation and allows users to confirm their input.
    Returns the validated input or None if the user cancels the process.
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
    Returns True if the user confirms 'Y', False if 'N'.
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
    Offers the user the choice to retry input or exit the process.
    Returns 'retry' to retry the input or 'exit' to cancel the process.
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
    while True:
        string_choice = input('Choice: ')
        int_choice = int(string_choice)
        _, func_choice = choices_and_funcs[int_choice - 1]
        func_choice()
