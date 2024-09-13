from data_handler.context_manager.context_manager import *
"""
Module for retrieving and displaying a list of account usernames and their corresponding user IDs.

This script connects to the `BankingData.db` database, retrieves the username and user ID from the `accountlog` table, 
and prints each username to the console.

Dependencies:
-------------
- Requires the `ContextManager` class from `data_handler.context_manager.context_manager` for managing the database connection.

Usage:
------
Simply run the script to see a list of usernames from the `accountlog` table in the `BankingData.db` database.

Example:
--------
>>> python Account_list.py
   username1
   username2
   ...
"""
with ContextManager('BankingData.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT user_name, user_id FROM accountlog')
    row = cursor.fetchall()
    for username, ident in row:
        print(username)
