from .shape import Shape


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
