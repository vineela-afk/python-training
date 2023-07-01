s= input("Enter String  : ")
a= int(input("Enter the number: "))
b=int(input("Enter the number: "))
l=list(s)
temp=l[a]
l[a]=l[b]
l[b]=temp
print(''.join(l))