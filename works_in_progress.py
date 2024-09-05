account = NewAccount(5555, '1234', 'Mclouse', 'Matthew Clouse',
                     'Checking', 10)





while True:
    print("""
    (1) Log into account
    (2) Create new account.
    """)
    menu_1 = input('Choice: ')
    if menu_1 == '1':
        pass
    if menu_1 == '2':
        pass

    def __init__(self, user_id: int, new_password: str, user_name: str,
                 holder_name: str = "", account_name: str = None,initial_funds: int = 0):
        self._account_name = account_name
        self.holder_name = holder_name
        self._user_id = user_id
        self.user_name = user_name
        self._user_password = new_password
        self.initial_funds = initial_funds
        self._entire_balance = 0
        self.all_transactions = []
        self._checking_balance = 0
        self.checking_transactions = []
        self._saving_balance = 0
        self.saving_transactions = []
        self.current_budget_warnings = 0