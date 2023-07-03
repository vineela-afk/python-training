n = int(input("Enter number: "))


def generator_func(n):
    '''
    this generates the values from1 to n
    '''
    value = 1
    while value <= n:
        yield value
        value += 1


for value in generator_func(n):
    print(value)
    