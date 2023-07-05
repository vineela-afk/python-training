import math


class Shape:
    '''
    its about shape cordinates
    '''
    def __init__(self, side, arg_y):
        self.side = side
        self.arg_y = arg_y

    def area(self):
        pass

    def peri(self):
        pass

    def compare_area(self, other):
        return self.area() > other.area()
    
    def compare_peri(self, other):
        return self.peri() > other.peri()

    def description(self):
        pass


class Square(Shape):
    '''
    gives the area and perimeter of square
    '''
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side**2
    
    def peri(self):
        return 4*self.side
    
    def description(self):
        return "Square"


class Circle(Shape):
    '''
    gives the area and perimeter of Circle
    '''

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def peri(self):
        return 2 * math.pi * self.radius
    
    def description(self):
        return "Circle"


class Rectangle(Shape):
    '''
    gives the area and perimeter of Rectangle
    '''

    def __init__(self, length, bre):
        self.length = length
        self.bre = bre

    def area(self):
        return self.length*self.bre
    
    def peri(self):
        return 4 * (self.length + self.bre)
    
    def description(self):
        return "Rectangle"


rect = Rectangle(3, 5)
sq = Square(4)
ci = Circle(3)

print(ci.compare_area(rect))
