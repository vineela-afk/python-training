class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance please add more.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account :", self.account_number)
        print(f"Balance: ${self.balance}\n")   


ac1 = BankAccount(2345, 1000, " viharo")
ac2 = BankAccount(1234, 2000, "habri")


print("Customer Details:")
ac1.print_customer_details()
ac1.deposit(1000)
ac1.check_balance()
ac1.withdraw(4000)
ac1.withdraw(3400)
ac1.check_balance()
