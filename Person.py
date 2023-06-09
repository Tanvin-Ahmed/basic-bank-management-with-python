import uuid


class Person:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.__email = email
        self.__password = password

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password


class User(Person):
    def __init__(self, name, email, password, initial_amount) -> None:
        super().__init__(name, email, password)
        self.__deposit_amount = initial_amount
        self.__user_id = uuid.uuid4()
        self.__loan_amount = 0
        self.__transaction_history = {}

    @property
    def user_id(self):
        return self.__user_id

    @property
    def deposit_amount(self):
        return self.__deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, amount):
        self.__deposit_amount = amount

    @property
    def loan_amount(self):
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, amount):
        self.__loan_amount = amount

    def save_transaction_history(self, transaction_id, description):
        self.__transaction_history[transaction_id] = description

    def show_transaction_history(self):
        print(f"------- {self.name}'s account transaction history -------")
        for key, value in self.__transaction_history.items():
            print(f"Transaction id: {key} and Description: {value}")

    def show_available_balance(self):
        print(
            f"Available balance of {self.name}'s account is: {self.deposit_amount}")

    def show_loan_balance(self):
        print(
            f"Loan balance of {self.name}'s account is: {self.__loan_amount}")


class Admin(Person):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.isAdmin = True
