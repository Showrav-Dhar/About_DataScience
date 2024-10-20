# Build a decorator that checks if the user given list at least contains one integer that is negative
def custom_checker(func):
    def wrapper(numbers, *args, **kwargs):
        f = True  # we have assumed that there is no negative
        for i in numbers:
            if i < 0:
                f = False  # means there is a negative value so our assumption is false and no error message will be printed
                break

        if f:   # if our assumption is right then error will be showed
            raise ValueError("List must contain at least one negative integer")

        return func(numbers, *args, **kwargs)

    return wrapper


@custom_checker  # line [18 to 23] is same as, sum_cal = custom_checker(sum_cal)
def sum_cal(numbers):  # returns the sum of a given list
    ans = 0
    for i in numbers:
        ans += i
    return ans


if __name__ == '__main__':
    # result = sum_cal([1, 2, -3, 10, 12]) # no error
    # print("The sum is = ", result)
    result2 = sum_cal([1, 2, 3, 10, 12])  # will print error message
    print("The sum is = ", result2)
