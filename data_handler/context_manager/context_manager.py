import sqlite3


class ContextManager:
    """
    A context manager class for managing SQLite database connections.

    This class handles the opening and closing of database connections, ensuring that transactions
    are either committed if successful or rolled back if an exception occurs during execution.

    Attributes:
    -----------
    host : str
        The path to the SQLite database file.

    Methods:
    --------
    __enter__():
        Opens the connection to the database and returns the connection object.

    __exit__(exc_type, exc_val, exc_tb):
        Commits the transaction if no exceptions occurred, otherwise closes the connection.
    """
    def __init__(self, host):
        """
         Initializes the ContextManager with the given database path.

         Args:
             host (str): The path to the SQLite database file.
         """
        self.connection = None
        self.host = host

    def __enter__(self):
        """
        Opens a connection to the SQLite database and returns the connection object.

        Returns:
            sqlite3.Connection: The connection object to interact with the database.
        """
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the connection to the database. If no exceptions occurred, commits the transaction.
        Otherwise, rolls back the transaction and closes the connection.

        Args:
            exc_type (Exception): The exception type (if any).
            exc_val (Exception): The exception value (if any).
            exc_tb (traceback): The traceback object (if any).
        """
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
