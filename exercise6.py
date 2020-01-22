##Banking App
class AccountHolder:
    def __init__(self, fname, mname, lname, account, balance, status):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.account = account
        self.balance = balance
        self.status = status

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account_holder = []
    def add_account_holder(self, fname, mname, lname, account, balance, status):
        if balance > 100:
            temp = AccountHolder(fname, mname, lname, account, balance, status)
            self.account_holder.append(temp)
            return f"A {account} account created for {fname} {mname} {lname} with a balance of {balance}."
        else:
            return "An account opening requires a minimum of $100"
def main():
    wellsFargo = Bank('wells fargo', '123 sesame street')
    action = 1
    while action != 6:
        print("1. Create Account")
        print("6. Exit Application")

        action = int(input("What would you like to do?")

        if action == 1:
            fname = input("First Name: ")
            mname = input("Middle Name: ")
            lname = input("Last Name: ")
            account = input ("Checking/Savings: ")
            balance = int(input("Initial Deposit: "))
            wellsFargo.add_account_holder(fname, mname, lname, account, balance, "opened")
        if action == 6:
            break

main()