num = int(input("Enter number: "))


def generator_func(number):
    '''
    this generates the values from1 to n
    '''
    value = 1
    while value <= number:
        yield value
        value += 1


for output in generator_func(num):
    print(output)
