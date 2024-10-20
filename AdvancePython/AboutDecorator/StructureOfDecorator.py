# def outer(func):
#     def wrapper(*args, **kwargs):
#         #statement1
#         #statement2
#         return func(*args, **kwargs) # always return the original function with its arguments
#
#     return wrapper
#
#
# @outer
# def user_func(*args, **kwargs):
#     #statement
#
#
# if __name__ == '__main__':
#     user_func()

# Key Points to Remember for why the wrapper() returns the original function :
#
# Decorators wrap the original function
# The wrapper function acts as a proxy of the original function
# Any return value from the original function must be passed through the wrapper
# Missing returns in decorators breaks the function's behavior
# Each decorator in a chain must preserve the return value


# Common Use Cases of decorators
# Timing functions (as in your previous example)
# Logging
# Authentication and authorization
# Caching
# Input validation
# Rate limiting
