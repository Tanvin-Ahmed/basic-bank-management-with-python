from Bank import Bank
from Person import Admin, User


def main():
    bank = Bank()

    user_1 = User("Tanvin", "tanvin@gmail.com", "1234", 10000)
    user_2 = User("Ahmed", "ahmed@gmail.com", "5678", 12000)
    user_3 = User("Touhid", "touhid@gmail.com", "9876", 15000)

    admin = Admin("Amdin", "amdin@gmail.com", "123456")

    bank.create_account(user_1)
    bank.create_account(user_2)
    bank.create_account(user_3)

    bank.create_admin(admin)

    # user 1 transaction with bank
    bank.deposit(user_1, 10000)
    bank.withdraw(user_1, 5000)
    bank.take_loan(user_1, 30001)
    user_1.show_transaction_history()
    print(user_1)


if __name__ == '__main__':
    main()
