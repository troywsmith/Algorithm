"""
Design question - design a bank account class with debit and credit accounts (10 minutes)
"""

from collections import defaultdict
import random

class BankAccount:

    def __init__(self, name, account_number, balance=0.00):
        print('\nWelcome to Capital One!')
        print('Thank you for opening an account {}!\n'.format(name))
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self.balance += amount
        self.show_balance()

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.show_balance()

    def show_balance(self):
        print('Account {} balance: ${}'.format(
            self.account_number, self.balance))


if __name__ == '__main__':
    acct_num = 1000
    debit_account = BankAccount('Troy', random.randint(1000,10000))
    debit_account.deposit(1000)
    debit_account.withdraw(83.34)