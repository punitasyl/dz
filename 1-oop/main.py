
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    secret_key: str = field(repr=False, compare=False)
    priority: int = 3
    done: bool = False
    created_at: datetime = field(default_factory=datetime.now, compare=False)


task1 = Task("Buy groceries", "3534wvrg4wg")
task2 = Task("Buy groceries", "gw4g2235253")
print(task1 == task2)
print(task1)





# class User:

#     users = []

#     def __init__(self, name, age: int):
#         self.name = name
#         self.age = age
#         User.users.append(self)

#     @classmethod
#     def from_string(cls, data: str):
#         name, age = data.split(",")
#         return cls(name, int(age))

#     @classmethod
#     def total_users(cls):
#         return len(cls.users)

# user1 = User("Alice", 30)
# user2 = User("Bob", 25)
# print(f"Total users: {User.total_users()}")

# maxim = User.from_string("Maxim, 28")
# print(f"Created user: {maxim.name}, Age: {maxim.age}")
# print(f"Total users: {User.total_users()}")