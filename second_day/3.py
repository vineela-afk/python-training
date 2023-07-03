name = input("Enter student name: ")
a, b, c = input("Enter the marks: ").split()
dic = {"name": [a, b, c]}
sumof = int(dic["name"][0])+int(dic["name"][1])+int(dic["name"][2])
print(f"{name} scored total of {sumof}")
