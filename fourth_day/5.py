from my_package import Circle, Square, Rectangle


try:
    length1 = float(input("Enter length  of shape 1: "))
    breadth1 = float(input("Enter breadth of shape 1: "))
    length2 = float(input("Enter length of shape 2: "))
    breadth2 = float(input("Enter breadth of shape 2: "))
except ValueError:
    print("Invalid input")
    exit()

shape1 = Rectangle(length1, breadth1)
shape2 = Rectangle(length2, breadth2)

if shape1.compare_area(shape2):
    print("Shape 1 has larger area")
else:
    print("Shape 2 has larger area")

if shape1.compare_peri(shape2):
    print("Shape 1 has larger peri")
else:
    print("Shape 2 has larger peri")
