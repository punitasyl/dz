#Есть User, Product и Order y которых есть поле id.
#Нужно сделать универвальную функицю поиска по id

from dataclasses import dataclass
from typing import Optional, Protocol, TypeVar, List

class HasID(Protocol):
    id: int

T = TypeVar('T', bound=HasID)

@dataclass
class User(HasID):
    id: int
    name: str

@dataclass
class Product(HasID):
    id: int
    name: str

@dataclass
class Order(HasID):
    id: int
    product_id: int
    user_id: int

def find_by_id(items: List[T], item_id: int) -> Optional[T]:
    for item in items:
        if item.id == item_id:
            return item
    return None

# Пример использования
users = [User(id=1, name="Alice"), User(id=2, name="Bob")]
products = [Product(id=1, name="Laptop"), Product(id=2, name="Phone")]
orders = [Order(id=1, product_id=1, user_id=1), Order(id=2, product_id=2, user_id=2)]
print(find_by_id(users, 1))  # Output: User(id=1, name='Alice')
print(find_by_id(products, 2))  # Output: Product(id=2, name
print(find_by_id(orders, 1))  # Output: Order(id=1, product_id=1, user_id=1)
print(find_by_id(users, 3))  # Output: None


