######################
#Ethan Elliott
#bankaccount.py
#4/23/25
#assignment12
#csci151
######################

#importing this for printing purposes
import stdio

#creating class bankaccount that will allow me to make objects for this tpye
class BankAccount:
    #constructor that takes in account number and the holder name then also the balance which is defaulted to zero
    def __init__(self, acct_num, acct_holder, balance=0):
        self._account_number = acct_num
        self._account_holder = acct_holder
        self._balance = balance

    #method just retrieves the account num, very basic method
    def get_account_holder_name(self):
        return self._account_holder

#depositing functionality checks for positive int then adds to balance and prints out the new bal
    def deposit(self, value):
        if value <= 0:
            stdio.writeln("needs to be positive...")
        else:
            self._balance += value
            stdio.writeln(f"deposited {value} to {self._account_number}. bal: {self._balance}")

#withdrawal functionality checks for positive int and if there is enough in the acc to withdraw from
    def withdraw(self, value):
        if value <= 0 or value > self._balance:
            stdio.writeln("not enough or not positive")
        else:
            self._balance -= value
            stdio.writeln(f"withdrew {value} from {self._account_number}. bal: {self._balance}")

#retrieving the acc num and bal
    def get_balance(self):
        return self._balance

#check if pos if so itll just call the other methods
    def transfer(self, other, value):
        if value <= 0 or value > self._balance:
            stdio.writeln("not enough or not positive")
        else:
            self.withdraw(value)
            other.deposit(value)

#show the acc num, holder, and bal to user in an f string
    def __str__(self):
    #just print to user by returning str from when this is called
        return f"acc num: {self._account_number}, acc holder: {self._account_holder}, bal: {self._balance}"

#test client that checks all the methods in my class
def main():
    account1 = BankAccount(53172, "ruby", 2000)
    account2 = BankAccount(91883, "ethan", 1000)

    stdio.writeln("test for acc info:")
    stdio.writeln(account1)
    stdio.writeln(account2)
    stdio.writeln()

    stdio.writeln("test for deposit:")
    account1.deposit(200)
    account2.deposit(-100)
    stdio.writeln()

    stdio.writeln("test for withdraw:")
    account1.withdraw(300)
    account1.withdraw(2000)
    account1.withdraw(-50)
    stdio.writeln()

    stdio.writeln("test for transfer:")
    account1.transfer(account2, 400)
    account1.transfer(account2, -100)
    account1.transfer(account2, 2000)
    stdio.writeln()

    stdio.writeln("testing the get_methods:")
    stdio.writeln(f"account 1 holder: {account1.get_account_holder_name()}")
    stdio.writeln(f"account 1 balance: {account1.get_balance()}")
    stdio.writeln(f"account 2 holder: {account2.get_account_holder_name()}")
    stdio.writeln(f"account 2 balance: {account2.get_balance()}")
    stdio.writeln()

    stdio.writeln("test for acc info:")
    stdio.writeln(account1)
    stdio.writeln(account2)

#if ran, run main function
if __name__ == "__main__":
    main()