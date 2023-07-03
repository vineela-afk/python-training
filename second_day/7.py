def middle(num):
    '''
    return middle value
    '''
    return num[1]


list_tuple = [(1, 2), (5, 4), (8, 1)]


def sort(list_oftuple):
    '''
    it sorts
    '''
    return sorted(list_oftuple, key=middle)


print(sort(list_tuple))
