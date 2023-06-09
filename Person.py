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
        self.deposit_amount = initial_amount
        self.user_id = uuid.uuid4()
        self.loan_amount = 0
        self.__transaction_history = {}

    def save_transaction_history(self, transaction_id, description):
        self.__transaction_history[transaction_id] = description

    def show_transaction_history(self):
        for key, value in self.__transaction_history.items():
            print(f"Transaction id: {key} and Description: {value}")

    def __repr__(self) -> str:
        return f"{self.name} has deposit amount: {self.deposit_amount} and he/she takes: {self.loan_amount} loan"


class Admin(Person):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.isAdmin = True
