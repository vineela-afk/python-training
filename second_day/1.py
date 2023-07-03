b = float(input("Saurabh's initial account balance: "))
w = float(input("Withdrawal amount: "))

if b > w:
    b = b-w-10.5
    print(b)
else:
    print("Error message withdrawal didnt match the criteria")
