fname1, fname2 = input("Enter Firstname: ").split()
lname1, lname2 = input("Enter Lastname: ").split()
roll1, roll2 = input("Enter rollno: ").split()
sortby = input("Choose how to sort FirstName or LastName or Rollno: ")
list1 = [fname1, fname2]
list2 = [lname1, lname2]
list3 = [roll1, roll2]
if sortby == "FirstName":
    print(sorted(list1))
elif sortby == "LastName":
    print(sorted(list2))
elif sortby == "Rollno":
    print(sorted(list3))
else:
    print("Invalid method")
