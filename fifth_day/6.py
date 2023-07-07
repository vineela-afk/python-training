class ConvtoInt(BaseException):
    pass


def con(num):
    try:
        val = int(num)
        print("converted", val)
    except (ConvtoInt, ValueError):
        print("cant convert")


num = input("Enter value: ")
con(num)

    