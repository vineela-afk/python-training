def check():
    try:
        num1 = int(input("Enter num: "))
        print(num1)
    except ValueError:
        print("Invalid input ")
    try:
        float1 = float(input("Enter float: "))
        print(float1)
    except ValueError:
        print("Invalid input ")
    

check()
