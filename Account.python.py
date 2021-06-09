class Account (object):
    def _init_(self, account_number, account_name, account_type):
        self.account_balance - 0
        self.acoount_number = account_number
        self.account_name = account_name
        self.account_type = account_type

def deposit(self, amount):
    pass

def withraw(self, amount):
    pass

def check_balance(self):
    pass
    return self.account_balance

def _str_ (self):
    description = "Account info\n-------\n"
    description += "Name: {}\n"
    description += "Type: {}\n"
    description += "Number: {}\n"
    description += "Balance: {}\n"

    return description.format(
        self.account_name,
        self.account_type,
        self.account_number,
        self.account_balance
    )

iclass = account(1234567890, "iclass", "savings")
print(iclass)

print("checking balance")
print("iclass.check_balance")

print("Deposit 10")
print("iclass.deposit(=10))

print("checking balance")
print("iclass.check_balance")

print(iclass)
