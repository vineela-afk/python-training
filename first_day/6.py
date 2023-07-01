from collections import Counter
s= input("Enter the string: ")
c= input("Enter the character: ")
x= Counter(s)
for i in x.elements():
    if i==c:
        print(i ,":", x[i])
        break