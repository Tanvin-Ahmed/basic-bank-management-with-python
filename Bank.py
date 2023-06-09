import uuid


class Bank:
    def __init__(self) -> None:
        self.__user_list = {}
        self.__total_available_balance = 0
        self.__total_loan_amount = 0
        self.__provide_load = True
        self.__admin = None

    def create_account(self, account):
        self.__total_available_balance += account.deposit_amount
        self.__user_list[account.user_id] = account
        account.save_transaction_history(uuid.uuid4(
        ), f"{account.name} successfully created new account with initial balance: {account.deposit_amount}")

    def deposit(self, account, amount):
        account.deposit_amount += amount
        self.__user_list[account.user_id] = account
        self.__total_available_balance += amount
        account.save_transaction_history(
            uuid.uuid4(), f"New deposit amount {amount}")

    def withdraw(self, account, amount):
        if account.deposit_amount >= amount:
            if amount > self.__total_available_balance:
                print("Bank is bankrupt")
            else:
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
            elif amount > account.deposit_amount * 2 - account.loan_amount:
                print(
                    f"Already you take {account.loan_amount} form bank. Now the maximum amount that you can take loan from bank is {account.deposit_amount * 2 - account.loan_amount}")
            elif amount > self.__total_available_balance:
                print("Bank is bankrupt")
            else:
                account.loan_amount += amount
                self.__user_list[account.user_id] = account
                self.__total_available_balance -= amount
                self.__total_loan_amount += amount
                account.save_transaction_history(
                    uuid.uuid4(), f"New loan amount {amount}")
        else:
            print("Bank stop to give loan")

    def fund_transfer(self, amount, from_account, to_account):
        if amount > from_account.deposit_amount:
            print(
                f"Insufficient funds in {from_account.name}'s account to transfer from {from_account.name} to {to_account.name}")
        elif amount > self.__total_available_balance:
            print("Bank is bankrupt")
        else:
            from_account.deposit_amount -= amount
            to_account.deposit_amount += amount

            transaction_id = uuid.uuid4()
            from_account.save_transaction_history(
                transaction_id, f"{amount} successfully transferred from my account to {to_account.name}'s account")
            to_account.save_transaction_history(
                transaction_id, f"{amount} successfully received from {from_account.name}'s account")

            self.__user_list[from_account.user_id] = from_account
            self.__user_list[to_account.user_id] = to_account

    # ? methods for admin

    def create_admin(self, account):
        self.__admin = account

    def update_loan_permission(self, account, permission):
        if self.__admin.email is account.email and self.__admin.password is account.password:
            self.__provide_load = permission
        else:
            print("Unauthorized access")

    def show_loan_amount(self, account):
        if self.__admin.email is account.email and self.__admin.password is account.password:
            print(
                f"Total loan amount of this bank is: {self.__total_loan_amount}")
        else:
            print("Unauthorized access")

    def show_total_available_balance(self, account):
        if account.email == self.__admin.email and account.password == self.__admin.password:
            print(
                f"Total available bank balance is: {self.__total_available_balance}")
        else:
            print("Unauthorized access")
