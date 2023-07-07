try:
    num1 = int(input("Enter number to be num1: "))
    num2 = int(input("Enter number to be num2: "))
    a = num1/num2
    if num2 == 0:
        raise ZeroDivisionError("cant divide by zero")
    else:
        print(a)
except ZeroDivisionError as e:
    print(e)
finally:
    print("hi me from finally")