# Нужно сделать Repository, который работает с любымим типами и имеет методы:
# add - добавляет в список элемент
# get_by_index - получает по index
# get_all - получает все
# Всё хранится как list

from dataclasses import dataclass
from typing import Generic, TypeVar, List, Optional


T = TypeVar('T')

@dataclass
class Repository(Generic[T]):
    _items: List[T]

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_by_index(self, index: int) -> Optional[T]:
        if 0 <= index < len(self._items):
            return self._items[index]
        return None

    def get_all(self) -> List[T]:
        return self._items.copy()
    
# Пример использования
repo = Repository[int]([])
repo._items = [1, 2]    
print(repo.get_by_index(0))  # Output: 1
print(repo.get_by_index(5))  # Output: None
print(repo.get_all())  # Output: [1, 2]