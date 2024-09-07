
# Finance Manager

## Project Overview

**Finance Manager** is a simple Python-based application designed to help users manage their personal finances. It provides tools to create accounts, track transactions, and deposit funds through an intuitive, menu-driven interface.

## Features

- **Account Management**: Create and manage multiple financial accounts.
- **Transaction Tracking**: Deposit funds and view transaction history.
- **Menu Navigation**: Easy-to-use main menu and submenu structure for accessing different features.

## Installation

To use the Finance Manager, you will need:

- **Python 3.x**: Download from [python.org](https://www.python.org/).

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/mtcvoid/Finance_Manager_1.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Finance_Manager_1
   ```
3. Run the Python program:
   ```bash
   python main.py
   ```

## Usage

After starting the program, users will be guided by a menu interface to perform tasks such as:

1. Creating an account.
2. Depositing money into the account.
3. Viewing the transaction history.

Example:
```python
user_account = create_new_account()
user_account.accounts.deposit('checking', 200)
print(user_account.all_transactions)
```

## Project Structure

- **accounts/**: Contains modules related to account management.
- **transactions/**: Manages deposits, withdrawals, and transaction history.
- **interface/**: Handles the menu-driven navigation system.
- **main.py**: The entry point for the program.
- **tests/**: Unit tests for the application's core features.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Please make sure your code adheres to the project's style guidelines.


