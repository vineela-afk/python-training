value= int(input("Enter the value : "))
if value>0 and  value <10:
    print("Small")
elif value>10 and value<100:
    print("Medium")
elif value<1000:
    print("Large")
else:
    print("Invalid")