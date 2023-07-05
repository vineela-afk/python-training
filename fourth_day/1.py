class Shape:
    '''
    its about shape cordinates
    '''
    def __init__(self, arg_x, arg_y):
        self.arg_x = arg_x
        self.arg_y = arg_y

    def __repr__(self):
        return f"x= {self.arg_x}, y={self.arg_y}"
    
    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Unsupoorted formate for = for 'Shape' and other ")
        raise NotImplementedError("equal comparison Not implemented ")

    def __gt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Unsupoorted formate for > for 'Shape' and other ")
        raise NotImplementedError("greater than comparison Not implemented ")

    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError("Unsupoorted formate for < for 'Shape' and other ")
        raise NotImplementedError("less than comparison Not implemented ")
    

shape1 = Shape(2, 4)
shape2 = Shape(5, 7)

try:
    print(shape1 > shape2)
except NotImplementedError as e:
    print(e)
