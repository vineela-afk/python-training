from .shape import Shape


class Rectangle(Shape):
    '''
    gives the area and perimeter of Rectangle
    '''

    def __init__(self, length, bre):
        if length < 0 or bre < 0:
            raise ValueError("The paras must be positive numbers")
        self.length = length
        self.bre = bre

    def area(self):
        return self.length*self.bre
    
    def peri(self):
        return 4 * (self.length + self.bre)
    
    def description(self):
        return "Rectangle"