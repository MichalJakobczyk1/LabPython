class BankAccount:
    def __init__(self, account_number, currency, balance, owner):
        self.account_number = account_number
        self._currency = currency
        self._balance = balance
        self._owner = owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate

    def __str__(self):
        return f"Account Number: {self.account_number}, Owner: {self._owner}, Balance: {self._balance} {self._currency}"

    def __len__(self):
        return self._balance

    def __add__(self, other):
        if isinstance(other, BankAccount) and self._are_accounts_compatible(other):
            new_balance = self._balance + other.balance
            return BankAccount(self.account_number, self._currency, new_balance, self._owner)
        else:
            raise ValueError("Cannot add incompatible accounts.")

    def _are_accounts_compatible(self, other):
        return (
            self.account_number == other.account_number
            and self._currency == other._currency
            and self._owner == other.owner
        )

acc_one = BankAccount("890567123", "PLN", 1000.0, "Johhny")
acc_two = BankAccount("650989452", "PLN", 2000.0, "Josh")

print(acc_one)
print(len(acc_one))

amount_pln = 100.0
exchange_rate = 0.25
amount_usd = BankAccount.convert_currency(amount_pln, exchange_rate)
print(f"Converted {amount_pln} PLN to {amount_usd} USD")

combined_account = acc_one + acc_two
print(combined_account)