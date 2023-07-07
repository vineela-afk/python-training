class AgeBelow(BaseException):
    pass


class AgeAbove(BaseException):
    pass


try:
    num = int(input("Enter age: "))
    if num < 18:
        raise AgeBelow(f"under age by {18-num}")
    elif num > 18:
        raise AgeAbove(f"over age by {num-18}")
except (AgeAbove, AgeBelow) as e:
    print(e)