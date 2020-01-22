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
        if balance >= 100:
            temp = AccountHolder(fname, mname, lname, account, balance, status)
            self.account_holder.append(temp)
            return f"A {account} account created for {fname} {mname} {lname} with a balance of {balance}."
        else:
            return "An account opening requires a minimum of $100"

    def show_members(self):
        for i in self.account_holder:
            print(f"{i.fname} {i.mname} {i.lname} has ${i.balance} in their {i.account} account and their account is {i.status}")

    def transfer(self, name1, name2, transfer_amount):
        for i in self.account_holder:
            for x in self.account_holder:
                if name1 == i.fname and name2 == x.fname:
                    if i.status != 'freeze' and i.status != 'closed':
                        if i.status != 'closed':
                            if i.balance >= transfer_amount:
                                i.balance -= transfer_amount
                                x.balance += transfer_amount
                            else:
                                i.balance -= transfer_amount
                                x.balance += transfer_amount
                                i.balance -= 35
                                i.status = 'freeze'
                    else:
                        break

    def withdrawl(self, name, withdrawl_amount):
        for i in self.account_holder:
            if name == i.fname:
                if i.status != 'freeze' and i.status != 'closed':
                    if i.balance >= withdrawl_amount:
                        i.balance -= withdrawl_amount
                    else:
                        i.balance -= withdrawl_amount
                        i.balance -= 35
                        i.status = 'freeze'
                else:
                    break

    def closeAccount(self, name):
        for i in self.account_holder:
            if i.fname == name:
                i.status = 'closed'

    def depositMoney(self, name, deposit_amount):
        for i in self.account_holder:
            if i.fname == name and i.status != 'closed':
                i.balance += deposit_amount
            if i.status == 'freeze' and i.balance > 0:
                i.status = 'opened'

def main():
    wellsFargo = Bank('wells fargo', '123 sesame street')
    action = 1
    while action != 7:
        print("1. Create Account")
        print("2. Check Account Holders")
        print("3. Transfer Balance")
        print("4. Withdrawl Balance")
        print("5. Deposit")
        print("6. Close Account")
        print("7. Exit Application")

        action = int(input("What would you like to do?"))

        if (action == 1):
            fname = input("First Name: ")
            mname = input("Middle Name: ")
            lname = input("Last Name: ")
            account = input ("Checking/Savings: ")
            balance = int(input("Initial Deposit: "))
            wellsFargo.add_account_holder(fname, mname, lname, account, balance, "opened")
        elif (action == 2):
            wellsFargo.show_members()
        elif (action == 3):
            name1 = input("Enter the first name of account transfering from: ")
            name2 = input("Enter the first name of account transfering to: ")
            transfer_amount = int(input("Enter amount to transfer: "))
            wellsFargo.transfer(name1, name2, transfer_amount)
        elif(action == 4):
            name = input("Enter your first name: ")
            withdrawl_amount = int(input("Enter your desired withdrawl amount: "))
            wellsFargo.withdrawl(name, withdrawl_amount)
        elif (action == 5):
            name = input("Enter the first name of the account you wish to deposit to: ")
            deposit_amount = int(input("Enter the amount Depositing: "))
            wellsFargo.depositMoney(name, deposit_amount)
        elif (action == 6):
            name = input("Enter your first name: ")
            wellsFargo.closeAccount(name)
        elif (action == 7):
            break

main()
