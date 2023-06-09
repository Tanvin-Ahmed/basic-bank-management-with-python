from Bank import Bank
from Person import Admin, User


def main():
    bank = Bank()

    user_1 = User("Tanvin", "tanvin@gmail.com", "1234", 10000)
    user_2 = User("Ahmed", "ahmed@gmail.com", "5678", 12000)
    user_3 = User("Touhid", "touhid@gmail.com", "9876", 15000)
    bank.create_account(user_1)
    bank.create_account(user_2)
    bank.create_account(user_3)

    admin = Admin("Amdin", "amdin@gmail.com", "123456")
    bank.create_admin(admin)

    bank.deposit(user_1, 10000)
    # bank.update_loan_permission(admin, False) #! admin stop to give loan
    # bank.take_loan(user_1, 30001) #! larger amount than user_bank_balance * 2
    bank.take_loan(user_1, 20000)
    bank.take_loan(user_1, 20000)
    user_1.show_loan_balance()

    user_1.show_available_balance()
    user_2.show_available_balance()

    bank.fund_transfer(1000, user_1, user_2)
    user_1.show_transaction_history()
    user_2.show_transaction_history()

    user_1.show_available_balance()
    user_2.show_available_balance()

    bank.show_total_available_balance(admin)
    bank.show_loan_amount(admin)


if __name__ == '__main__':
    main()
