# basics
# def my_decorator(func):
#     def wrapper():
#         print("Something happens before")
#         func()
#         print("Something happens after")
#     return wrapper()
#
#
# @my_decorator
# def say_hello():
#     print("Hello testing decorator")
#
#
# if __name__ == '__main__':
#     say_hello()

# Decorators With Arguments
#
# def repeat(times):
#     def decorator(func):  # main decorator
#         def wrapper():
#             for _ in range(times):
#                 func()
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(times=3)
# def greet():
#     print("HELLO")
#
#
# if __name__ == '__main__':
#     greet()

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # If we don't return func(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def add(a, b):
    return a + b


result = add(2, 3)
print(result)
