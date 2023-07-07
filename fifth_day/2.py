try:
    num = int(input("Enter number to be positive: "))
    if num < 0:
        raise ValueError("it shouldnt be negative")
except ValueError as e:
    print(e)
    
finally:
    print("done")