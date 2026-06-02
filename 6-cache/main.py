
from dataclasses import dataclass
from typing import Optional, TypeVar, Callable


# T = TypeVar('T')
# R = TypeVar('R')

# def process_items(items: list[T], transformer: Callable[[T], R]) -> list[R]:
#     # Placeholder for processing logic
#     return [transformer(item) for item in items]  # This is just a dummy implementation

# def to_upper(s: str) -> str:
#     return s.upper()

# results = process_items(['hello', 'world'], to_upper)
# print(results)  # Output: ['HELLO', 'WORLD']



# @dataclass
# class User:
#     id: int
#     name: str
#     email: str

# def get_user_by_id(user_id: int) -> Optional[User]:
#     users = [User(id=1, name="John Doe", email="john.doe@example.com"),
#              User(id=2, name="Jane Smith", email="jane.smith@example.com")]
#     # Placeholder for database retrieval logic
#     for user in users:
#         if user.id == user_id:
#             return user
#     return None

# user = get_user_by_id(1)
# print(user)  # Output: User(id=1, name='John Doe',
