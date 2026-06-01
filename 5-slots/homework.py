'''
Создать класс User с полями: имя, email, password
Создать класс SlotUser с полями: имя, email, password используя slots
Создать 2 списка из 100 000 экземпляров каждого класса и вывести сравнение занимаемой памят
'''

from dataclasses import dataclass
import sys

class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

class SlotUser:
    __slots__ = ("name", "email", "password")

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

users = [User("name", "email", "password") for _ in range(100_000)]
slot_users = [SlotUser("name", "email", "password") for _ in range(100_000)]

# Размер одного объекта
print(f"One User object: {sys.getsizeof(users[0])} bytes")
print(f"One SlotUser object: {sys.getsizeof(slot_users[0])} bytes")

# Размер __dict__ для User
user_dict_size = sys.getsizeof(users[0].__dict__)
print(f"User __dict__ size: {user_dict_size} bytes")

# Общий размер всех объектов
user_total = sys.getsizeof(users) + sum(sys.getsizeof(u) + sys.getsizeof(u.__dict__) for u in users)
slotuser_total = sys.getsizeof(slot_users) + sum(sys.getsizeof(u) for u in slot_users)

print(f"\nTotal User memory: {user_total:,} bytes")
print(f"Total SlotUser memory: {slotuser_total:,} bytes")
print(f"Memory saved: {user_total - slotuser_total:,} bytes ({(user_total - slotuser_total) / user_total * 100:.1f}%)")
