class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def display_info(self):
        print("Account Holder:",self.account_holder,"Balance:",self.balance)
def main():
    account_holder = input()
    balance = float(input())
    bank = BankAccount(account_holder,balance)
    bank.deposit(100)
    bank.display_info()
main()