# x = 99
#
#
# def fun1():
#     x = 88
#
#     def fun2():
#         print(x)
#
#     return fun2
#
#
# if __name__ == '__main__':
#     res = fun1()
#     res()

# Clouser
def showmik(num):
    def dip(x):
        return x ** num

    return dip


if __name__ == '__main__':
    f = showmik(2)
    g = showmik(3)

    print(f(2))
    print(g(3))
