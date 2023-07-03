a, b, c = input("Enter the values: ").split()
'''
    a ,b ,c are three numbers and we are checking the larger of the three
'''
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
