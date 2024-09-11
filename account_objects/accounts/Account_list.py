from data_handler.context_manager.context_manager import *

with ContextManager('BankingData.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT user_name, user_id FROM accountlog')
    row = cursor.fetchall()
    for username, ident in row:
        print(username)
