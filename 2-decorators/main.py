


# def log_decorator(func):
#     def wrapper():
#         print("Function is being called")
#         func()
#         print("Function has been called")
#     return wrapper


# @log_decorator
# def say_hello():
#     print(f"Hello, World!")

# say_hello()


# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} is being called with args: {args} and kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned: {result}")
#         return result
#     return wrapper

# @log
# def add(a: float, b: float) -> float:
#     return a + b

# print(add(5, 3))


# def add_repr(cls):
#     def __repr__(self):
#         return f"{cls.__name__}[{self.__dict__}]"
#     cls.__repr__ = __repr__
#     return cls

# @add_repr
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

# user1 = User("Alice", 30)
# print(user1)


# def repeat(times: int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def hello():
#     print("Hello, World!")

# hello()

# def retry(times: int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator


# @retry(3)
# def unstable():
#     import random
#     if random.random() < 0.7:
#         print("Success!")
#     else:
#         print("Failed, retrying...")

# unstable()

class User:

    age: float

u = User()
setattr(u, "age", 25)
print(getattr(u, "age"))