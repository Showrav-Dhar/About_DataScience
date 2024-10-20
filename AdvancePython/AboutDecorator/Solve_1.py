# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time


def time_calculator(func):  # taking function as a parameter of another function
    def wrapper(*args, **kwargs):  # taking unlimited arguments
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start}s to run")
        return result

    return wrapper  # returning the definition of wrapper


@time_calculator
def example_function(n):
    # after writing @time_calculator, example_function will always go through time_calculator while executing
    # with its parameter
    time.sleep(n)


if __name__ == '__main__':
    example_function(2)
