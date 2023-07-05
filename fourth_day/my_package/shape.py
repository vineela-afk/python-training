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