
from functools import wraps


def log(call):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(call):
                print("Call #", _ + 1)
                func(*args, **kwargs)
        return wrapper
    return decorator


@log(3)
def work():
    print("Working...")


@log(2)
def calculate():
    print("Result 42")

work()
calculate()
