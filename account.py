class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.account_name = name
        self.account_balance = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Deposits the specified amount into the account.
        :param amount: Account balance
        :return: bool, True if the deposit was successful, False if not.
        """
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the specified amount from the account.
        :param amount: float
        :return: bool, True if withdrawal successful, False if not.
        """
        if amount <= 0 or amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Returns the current balance in the account.
        :return: self.balance
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        Returns the name of the account holder.
        :return: self.name
        """
        return self.account_name
