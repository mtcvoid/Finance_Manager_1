
# Free Finance - Financial Management System

## Project Overview

Free Finance is a modular financial management system designed to handle multiple aspects of personal finance, including:
- Account management
- Transaction processing
- Budgeting and bill tracking
- Market watch for financial updates

The project includes unit testing for core functionalities and supports database management for storing and retrieving financial data.

## Project Structure

The project is organized as follows:

```plaintext
Free_Finance-master/
│
├── account_objects/
│   ├── accounting/         # Handles financial transactions
│   └── accounts/           # Manages user accounts (creation, listing, etc.)
│
├── data_handler/
│   ├── context_manager/    # Manages the execution context (sessions, transactions)
│   ├── database/           # Interacts with the database for persistent data storage
│   └── variables/          # Stores constants and configurations
│
├── interface/              # Contains user interface components for different finance modules
│   ├── user_interface_bill_tracker.py
│   ├── user_interface_budget.py
│   └── ...
│
├── mods/                   # Feature modules (e.g., bill tracking, budgeting, market watch)
│   ├── bill_tracker/
│   ├── budget/
│   └── market_watch/
│
├── testing/                # Unit tests for the project
│   ├── account_transaction_unit_test.py
│   ├── database_unit_testing.py
│   └── ...
│
└── main/
    └── app.py              # Main entry point for running the application
```

## Features

### 1. Account Management
The `account_objects` package handles account-related tasks such as:
- **Account creation** (`account_creator.py`)
- **Account listing** (`Account_list.py`)
- **Transaction management** (`transactions.py`)

### 2. Data Handling
The `data_handler` package manages the flow and storage of financial data. Key components include:
- **Database interaction** (`data_base_handler.py`)
- **Context management** for transactions (`context_manager.py`)
- **Constants and configurations** (`constants.py`)

### 3. User Interface
The `interface` package defines various user interfaces:
- **Budgeting** (`user_interface_budget.py`)
- **Bill tracker** (`user_interface_bill_tracker.py`)
- **Market watch** for real-time financial updates (`user_interface_market_watch.py`)

### 4. Modular Features
The `mods` package includes feature-specific modules, like:
- **Bill Tracker** (`bill_tracking_handler.py`)
- **Budget Management** (`budget_handler.py`)
- **Market Watch** (`market_watch_handler.py`)

### 5. Testing
The project includes unit tests to verify the functionality of key components, found in the `testing/` directory. You can run these tests to ensure everything works as expected.

## Installation

### Prerequisites
Ensure you have the following software installed:
- Python 3.x
- Pip (Python package manager)
- Any required packages listed in `requirements.txt` (if provided)

### Steps

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Free_Finance.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Free_Finance-master
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main application:
   ```bash
   python main/app.py
   ```

## Usage

Once the application is running, you can:
- Create and manage accounts
- Track expenses and income
- Monitor bills and budgeting performance
- Watch market trends for financial instruments

## Running Tests

To run the unit tests:
```bash
pytest testing/
```

The tests will cover functionality such as account transactions, database interactions, and user interface interactions.

## Contribution

Contributions are welcome! If you'd like to improve the project or add features, feel free to submit a pull request. Be sure to include tests for any new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
