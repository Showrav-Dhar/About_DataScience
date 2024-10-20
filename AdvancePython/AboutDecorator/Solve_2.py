# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def custom_debug(func):
    def wrapper(*args, **kwargs):
        total_args_values = ', '.join(str(arg) for arg in args)
        total_kwargs_values = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling = {func.__name__} with args {total_args_values} and kwargs {total_kwargs_values}")
        return func(*args, **kwargs)

    return wrapper


@custom_debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


if __name__ == '__main__':
    greet("Sheldon", greeting="Good morning")
