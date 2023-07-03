name = input("Enter student name: ")
a, b, c = input("Enter the marks: ").split()
dict = {"name": [a, b, c]}
sumof = int(dict["name"][0])+int(dict["name"][1])+int(dict["name"][2])
print(f"{name} scored total of {sumof}")
