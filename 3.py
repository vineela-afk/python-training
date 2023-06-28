a,b,c =input("Enter the values: " ).split()
if a>b and a>c:
    print("Larger number is: " + a)
elif b>a and b>c:
    print("Larger number is: " + b)
else:
    print("Larger number is: " + c)