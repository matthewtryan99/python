##Banking App
class AccountHolder:
    def __init__(self, fname, mname, lname, account, balance, status):
        self.fname = fname
        self.lname = lname
        self.account = account
        self.balance = balance
        self.status = status

class Bank:
    def __init__(self):
        self.account_holder = []
    def add_account_holder(self, fname, mname, lname, account, balance, status):
        temp = AccountHolder(fname, mname, lname, account, balance, status)
        self.account_holder.append(temp)
        