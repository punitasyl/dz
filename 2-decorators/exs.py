
from functools import wraps


class Limit:
    def __init__(self, max_calls: int):
        self.count = max_calls

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.count <= 0:
                raise RuntimeError("Call limit exceeded")
            self.count -= 1
            return func(*args, **kwargs)
        return wrapper

# def limit_calls(max_calls: int):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             count_attr = f"_{func.__name__}_calls"
#             current = getattr(wrapper, count_attr, 0)
#             if current >= max_calls:
#                 raise RuntimeError("Call limit exceeded")
#             setattr(wrapper, count_attr, current + 1)
#             print(f"Call {current + 1} to {func.__name__}()")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

class Engine:

    @Limit(3)
    def start(self):
        print("Engine started")
    

car = Engine()

car.start()
car.start()

car.start()
car.start() # <- runntime error: Too many calls to start()