
from data_handler.database.data_base_handler import *


def account_list_from_database():
    """
    Retrieves a list of accounts from the 'accountlog' table and displays the usernames
    along with a numbered list. The user can then make a selection to either view a specific
    account or return to the main menu.
    """
    with ContextManager('BankingData.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT user_name, userID FROM accountlog')
        row = cursor.fetchall()

        # Enumerate through the rows and print the usernames with numbers
        for idx, (username, ident) in enumerate(row, start=1):
            print(f"{idx}. {username}")

        # Add an extra option for returning to the main menu
        print(f"{len(row) + 1}. Return to main menu")

        # Here you can prompt the user for input and handle their selection
        user_input = input("Select an option: ")

        # Convert user input to integer and check their selection
        if user_input.isdigit():
            user_selection = int(user_input)

            # Return to menu will always populate at the end of the list.
            if user_selection == len(row) + 1:
                from interface.menu_handler import main_menu  # Located here to avoid circular imports.
                main_menu()
            elif 1 <= user_selection <= len(row):  # selected_user[1] will default to the ID tag (MATT)
                selected_user = row[user_selection - 1]
                print(f"You selected: {selected_user[0]} (ID: {selected_user[1]})")
                confirmation = get_user_confirmation('Is this the correct account?')
                if confirmation:
                    handler = DatabaseUnpacker()
                    tester = handler.pull_from_database(selected_user[1])
                    print(tester)
                else:
                    print('test FALSE')
            else:
                print("Invalid selection, please try again.")
        else:
            print("Invalid input, please enter a number.")



account_list_from_database()
