# Problem 3: Cache Return ValuesProblem
# Implement a decorator that caches the return values of a function,
# so that when it's called with the same arguments,
# the cached value is returned instead of re-executing the function.
import time


def custom_cache(func):
    cached_value = {}  # used dictionary to store the values in key value order
    print(cached_value)

    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result

    return wrapper


@custom_cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


if __name__ == '__main__':
    print(long_running_function(2, 3))
    print(long_running_function(2, 3))
    print(long_running_function(4, 3))
    print(long_running_function(2, 3))
