import math
from .shape import Shape


class Circle(Shape):
    '''
    gives the area and perimeter of Circle
    '''
    
    def __init__(self, radius):
        self.radius = radius

    def __del__(self):
        print(f"object{self.radius}  is being distryoed")

    def area(self):
        return math.pi * self.radius ** 2
    
    def peri(self):
        return 2 * math.pi * self.radius
    
    def description(self):
        return "Circle"
