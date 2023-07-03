s = input("Enter the string: ")
s2 = input("Enter the string: ")
t = len(s)
if t % 2 == 0:
    print(s[0:t//2]+s2+s[-t//2:])

else:
    print(s[0:t//2]+s2+s[-t//2+1:])
