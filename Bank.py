import uuid


class Bank:
    def __init__(self) -> None:
        self.__user_list = {}
        self.__total_available_balance = 0
        self.__total_loan_amount = 0
        self.__provide_load = True
        self.__admin = None

    def create_account(self, account):
        self.__user_list[account.user_id] = account

    def deposit(self, account, amount):
        account.deposit_amount += amount
        self.__user_list[account.user_id] = account
        self.__total_available_balance += amount
        account.save_transaction_history(
            uuid.uuid4(), f"New deposit amount {amount}")

    def withdraw(self, account, amount):
        if account.deposit_amount >= amount:
            account.deposit_amount -= amount
            self.__user_list[account.user_id] = account
            self.__total_available_balance -= amount
            account.save_transaction_history(
                uuid.uuid4(), f"New withdraw amount {amount}")
        else:
            print(f"Not enough funds to withdraw")

    def take_loan(self, account, amount):
        if self.__provide_load is True:
            if amount > account.deposit_amount * 2:
                print(
                    f"Sorry, the amount is too large to give as loan. You can take maximum {account.deposit_amount * 2} as loan")
            else:
                account.loan_amount = amount
                self.__user_list[account.user_id] = account
                self.__total_available_balance -= amount
                self.__total_loan_amount += amount
                account.save_transaction_history(
                    uuid.uuid4(), f"New loan amount {amount}")
        else:
            print("Bank stop to give loan")

    #! methods for admin
    def create_admin(self, account):
        self.__admin = account

    def update_loan_permission(self, account, permission):
        if self.__admin.email is account.email and self.__admin.password is account.password:
            self.__provide_load = permission
        else:
            print("Unauthorized access")

    def show_total_balance(self, account):
        if self.__admin.email is account.email and self.__admin.password is account.password:
            print(f"Total Balance is {self.__total_available_balance}")
        else:
            print("Unauthorized access")
