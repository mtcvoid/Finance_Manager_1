import json

from account_objects.accounts.active_account import ActiveAccount
from data_handler.context_manager.context_manager import ContextManager
from interface.menu_handler import *
from interface.user_interface_general import get_user_confirmation


class DatabaseUnpacker:
    """
    A class responsible for interacting with a SQLite database to store and retrieve account
    information. This class provides methods for creating the necessary table, inserting or updating
    account data, and pulling account information from the database based on the user ID.
    """

    def __init__(self):
        self.create_account_log_table()

    def create_account_log_table(self):
        """
        Creates the 'accountlog' table in the 'BankingData.db' SQLite database if it does not already exist.
        This table is used to store account-related information such as userID, account holder name, and balances.

        The table includes the following fields:
        - userID: The primary key (unique identifier for the user).
        - account_holder_name: The name of the account holder.
        - user_name: The username for the account.
        - user_password: The password for the account.
        - transaction_history: A log of account transactions.
        - checking_balance: The balance in the checking account.
        - savings_balance: The balance in the savings account.
        - current_budget_warnings: A count of any budget warnings associated with the account.
        """
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS accountlog(userID integer primary key, account_holder_name '
                           'text, user_name text, user_password text, transaction_history text, checking_balance '
                           'real, savings_balance real, current_budget_warnings integer, bills text,'
                           'bill_reminders text)')

    def push_to_database(self, account_data):
        """
         Inserts or updates account information in the 'accountlog' table of the 'BankingData.db' database.
         If an account with the same userID already exists, it will update the existing record. Otherwise,
         it will insert a new record.

         Args:
             account_data (dict): A dictionary containing account details such as username, balance, and password.

         Example:
             account_data = {
                 'User_ID': 1,
                 'Account_Holder_Name': 'John Doe',
                 'User_name': 'johndoe',
                 'User_password': 'password123',
                 'Transaction_History': '[...]',
                 'Checking_Balance': 1500.00,
                 'Savings_Balance': 3000.00,
                 'Current_Budget_Warnings': 0
                 'Bills: [name: bill_1, amount: 100, due_date: 2026-04-15]
                 'bill_reminders : []
             }
             push_to_database(account_data)
         """

        # handles the json conversion while still being able to move the data in one variable to database.
        data_converter = {
            USER_ID: account_data[USER_ID],
            ACCOUNT_HOLDER_NAME: account_data[ACCOUNT_HOLDER_NAME],
            USER_NAME: account_data[USER_NAME],
            USER_PASSWORD: account_data[USER_PASSWORD],
            TRANSACTION_HISTORY: json.dumps(account_data[TRANSACTION_HISTORY]),
            CHECKING_BALANCE: account_data[CHECKING_BALANCE],
            SAVINGS_BALANCE: account_data[SAVINGS_BALANCE],
            CURRENT_BUDGET_WARNINGS: account_data[CURRENT_BUDGET_WARNINGS],
            BILLS: json.dumps(account_data[BILLS]),
            BILL_REMINDERS: json.dumps(account_data[BILL_REMINDERS])
        }

        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO accountlog (userID, account_holder_name, user_name, user_password, 
                                        transaction_history, checking_balance, savings_balance, current_budget_warnings,
                                        bills, bill_reminders)
                VALUES (:user_id, :account_holder_name, :user_name, :user_password, 
                        :transaction_history, :checking_balance, :savings_balance, :current_budget_warnings, :bills,
                        :bill_reminders)
                ON CONFLICT(userID) DO UPDATE SET 
                    account_holder_name = excluded.account_holder_name,
                    user_name = excluded.user_name,
                    user_password = excluded.user_password,
                    transaction_history = excluded.transaction_history,
                    checking_balance = excluded.checking_balance,
                    savings_balance = excluded.savings_balance,
                    current_budget_warnings = excluded.current_budget_warnings,
                    bills = excluded.bills,
                    bill_reminders = excluded.bill_reminders
            ''', data_converter)

    def pull_from_database(self, user_id):
        """
        Retrieves the account information for a specific user from the 'accountlog' table in the 'BankingData.db'
        database and returns it as a dictionary. If no account is found for the provided user ID, a message is printed.

        Parameters:
        ----------
        user_id : int
            The user ID of the account you want to retrieve from the database.

        Returns:
        -------
        dict or None:
            If the account is found, a dictionary containing the following account information is returned:
                - 'user_id' (int): The user's ID.
                - 'Account_Holder_Name' (str): The name of the account holder.
                - 'user_name' (str): The username.
                - 'user_password' (str): The user's password.
                - 'transaction_history' (str): The user's transaction history.
                - 'checking_balance' (float): The current balance in the checking account.
                - 'savings_balance' (float): The current balance in the savings account.
                - 'current_budget_warnings' (int): The number of budget warnings.
                - 'bills: (list): list of bills with name,amount, and due date'

            If no account is found for the given user ID, `None` is returned and a message is printed to the console.

        Example:
        -------
        account_info = pull_from_database(1)
        if account_info:
            print(account_info)
        """
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()
            # Use a WHERE clause to filter by userID
            cursor.execute('SELECT * FROM accountlog WHERE userID = ?', (user_id,))
            row = cursor.fetchone()  # Fetch only one row corresponding to the specific userID

            if row:
                transaction_history_data = row[4] if row[4] else '[]'
                bills_data = row[8] if row[8] else '[]'
                bills_reminder_data = row[9] if row[9] else '[]'

                # Map the fetched row into a dictionary
                account_info = {
                    USER_ID: row[0],
                    ACCOUNT_HOLDER_NAME: row[1],
                    USER_NAME: row[2],
                    USER_PASSWORD: row[3],
                    TRANSACTION_HISTORY: json.loads(transaction_history_data),
                    CHECKING_BALANCE: row[5],
                    SAVINGS_BALANCE: row[6],
                    CURRENT_BUDGET_WARNINGS: row[7],
                    BILLS: json.loads(bills_data),
                    BILL_REMINDERS: json.loads(bills_reminder_data)
                }

                return account_info
            else:
                print(f'No account found for userID: {user_id}')

    def get_user_choice(self, choices_and_funcs):
        """
         Prompts the user to select a choice from a menu. If the selected choice corresponds to a function,
         the function is executed. Otherwise, if it corresponds to a string, the associated sub-menu is loaded.

         Args:
             choices_and_funcs (list): A list of tuples where each tuple contains a number, description,
                                       and a function or menu key.
         """
        while True:
            string_choice = input('Choice: ')

            if string_choice.isdigit():
                int_choice = int(string_choice)

                # Ensure the selection is valid
                if 1 <= int_choice <= len(choices_and_funcs):
                    number, description, action = choices_and_funcs[int_choice - 1]

                    # If it's a function, call it
                    if callable(action):
                        action()

                    # If it's a string, use it as a key to find the next sub-menu
                    elif isinstance(action, str):
                        menu_maker(action)
                    else:
                        print(f"No sub-menu found for key: {action}")
                else:
                    print("Invalid choice. Please select a valid number.")
            else:
                print("Invalid input. Please enter a number.")

    def account_list_from_database(self):
        """
        Retrieves a list of accounts from the 'accountlog' table in the 'BankingData.db' SQLite database.

        The function displays the usernames along with their corresponding account numbers in a numbered list.
        The user can then select an account from the list by entering the corresponding number. After selection,
        the function confirms the user's choice. If confirmed, the selected account's data is retrieved from
        the database and an ActiveAccount object is created. This ActiveAccount is then passed to the
        active_user_menu for further interaction.

        If the user chooses to return to the main menu, the main_menu function from menu_handler is invoked.

        Functionality:
        1. Display a numbered list of all accounts from the database.
        2. Provide the option to select an account or return to the main menu.
        3. If an account is selected, confirm the choice and load the account details.
        4. Create an ActiveAccount object and pass it to the active_user_menu.

        Args:
            None

        Returns:
            None
        """
        # Connect to the BankingData.db database using the context manager.
        with ContextManager('BankingData.db') as connection:
            cursor = connection.cursor()

            # Retrieve all accounts from the accountlog table (fetch user_name and userID).
            cursor.execute('SELECT user_name, userID FROM accountlog')
            row = cursor.fetchall()  # Fetch all the rows from the query result.

            # Display each account's username with a corresponding number.
            for idx, (username, ident) in enumerate(row, start=1):
                print(f"{idx}. {username}")

            # Add an extra option to return to the main menu.
            print(f"{len(row) + 1}. Return to main menu")

            # Prompt the user to select an account or choose to return to the main menu.
            user_input = input("Select an option: ")

            # Check if the input is a valid number.
            if user_input.isdigit():
                user_selection = int(user_input)

                # If the user selects the last option, return to the main menu.
                if user_selection == len(row) + 1:
                    from interface.menu_handler import main_menu  # Import here to avoid circular imports.
                    main_menu()

                # If the user selects a valid account from the list.
                elif 1 <= user_selection <= len(row):
                    selected_user = row[user_selection - 1]  # Get the selected user from the list.
                    print(f"You selected: {selected_user[0]} (ID: {selected_user[1]})")

                    # Confirm the account selection with the user.
                    confirmation = get_user_confirmation('Is this the correct account? (Y),(N): ')

                    if confirmation:  # If the user confirms the selection.

                        # Retrieve the selected user's account details from the database.
                        handler = DatabaseUnpacker()
                        account_info = handler.pull_from_database(selected_user[1])  # Pull user data by user ID.

                        # Create an ActiveAccount object using the retrieved data.
                        active = ActiveAccount(
                            account_info[USER_ID],
                            account_info[ACCOUNT_HOLDER_NAME],
                            account_info[USER_NAME],
                            account_info[USER_PASSWORD],
                            account_info[TRANSACTION_HISTORY],
                            account_info[CHECKING_BALANCE],
                            account_info[SAVINGS_BALANCE],
                            account_info[CURRENT_BUDGET_WARNINGS],
                            account_info[BILLS],
                            account_info[BILL_REMINDERS])

                        from interface.menu_handler import menu_maker  # negates circular imports
                        # Call active_user_menu to allow further actions on the selected account.
                        menu_maker('User Account Menu', active)



                    else:
                        # If the user does not confirm the selection.
                        print('Account selection canceled.')

                else:
                    # If the user selection is outside the valid range of account options.
                    print("Invalid selection, please try again.")

            else:
                # If the input is not a valid number.
                print("Invalid input, please enter a number.")


def display_account_list():
    """
    Displays the list of accounts by calling the 'account_list_from_database' method.
    """
    accounts = DatabaseUnpacker()
    accounts.account_list_from_database()
