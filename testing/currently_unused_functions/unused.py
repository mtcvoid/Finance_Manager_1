def get_data(self, account, checking_balance: int, savings_balance: int):  # there might not be a need for this method
    """
     Retrieves account details and transaction information to prepare it for database insertion.

     Parameters:
         account (Account): An object containing account details such as username, balance, and password.
         tran (Transactions): An object that holds transaction history and current balances.

     Returns:
         dict: A dictionary containing the account details and transaction information, structured for insertion
               into the database.
     """
    account_data = account.get_account_details()

    return account_data