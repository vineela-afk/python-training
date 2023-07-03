a, b = input("enter two number: ").split()
op = input("Operations to perform: ")
if op == "+":
    print(int(a)+int(b))
elif op == "*":
    print(int(a)*int(b))
elif op == "/":
    print(int(a)/int(b))
else:
    print(int(a)-int(b))