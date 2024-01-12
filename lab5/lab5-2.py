class BankAccount:
    def __init__(self, account_number, currency, balance, owner):
        self.account_number = account_number
        self.currency = currency
        self._balance = balance
        self._owner = owner

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def get_owner(self):
        return self._owner

    def set_owner(self, new_owner):
        self._owner = new_owner

    def __str__(self):
        return f"Account Number: {self.account_number}, Owner: {self._owner}, Balance: {self._balance} {self.currency}"

    def __len__(self):
        return self._balance

    def __add__(self, other):
        if isinstance(other, BankAccount) and self._are_accounts_compatible(other):
            new_balance = self._balance + other.get_balance()
            return BankAccount(self.account_number, self.currency, new_balance, self._owner)
        else:
            raise ValueError("Cannot add incompatible accounts.")

    def _are_accounts_compatible(self, other):
        return (
            self.account_number == other.account_number
            and self.currency == other.currency
            and self._owner == other.get_owner()
        )

acc_one = BankAccount("890567123", "PLN", 1000.0, "Johhny")
acc_two = BankAccount("650989452", "PLN", 2000.0, "Josh")

print(acc_one)
print(len(acc_one))

combined_account = acc_one + acc_two
print(combined_account)