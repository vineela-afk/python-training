s = input("Enter the string: ")
t = ''

for index, ele in enumerate(s):
    if index % 2 != 0:
        t += ele
    else:
        index += 1

print(t)
