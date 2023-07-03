s = input("Enter String  : ")
a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
list_name = list(s)
temp = list_name[a]
list_name[a] = list_name[b]
print(''.join(list_name))
