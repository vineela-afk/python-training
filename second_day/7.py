def middle(n):
    return n[1]


list_tuple = [(1, 2), (5, 4), (8, 1)]


def sort(list_tuple):
    '''
    it sorts
    '''
    return sorted(list_tuple, key=middle)


print(sort(list_tuple))
