import sys

# class A:
#     def __init__(self) -> None:
#         self.x = 1
#         self.y = 2

# class B:
#     __slots__ = ("x", "y")

#     def __init__(self) -> None:
#         self.x = 3
#         self.y = 4

# b = B()
# print(b.x)  # 3
# print(b.y)  # 4

# a = A()
# print(sys.getsizeof(a))  # 48
# print(sys.getsizeof(a.__dict__))  # 32
# print(sys.getsizeof(b))  # 32

import gc

a = []
b = [a]
a.append(b)

print(gc.get_stats())