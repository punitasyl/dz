# Сделать функции
# safe_get - безопасное получение элемента по индексу
# map_optional -  применение функции к элементу, если он не None
# or_else - возвращает значение или default если None

from typing import Optional, TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')

def safe_get(lst: list[T], index: int) -> Optional[T]:
    if 0 <= index < len(lst):
        return lst[index]
    return None

def map_optional(value: Optional[T], func: Callable[[T], R]) -> Optional[R]:
    if value is not None:
        return func(value)
    return None

def or_else(value: Optional[T], default: T) -> T:
    return value if value is not None else default

# Примеры использования
my_list = [1, 2, 3]
print(safe_get(my_list, 1))  # Output: 2
print(safe_get(my_list, 5))  # Output: None
print(map_optional(5, lambda x: x * 2))  # Output: 10
print(map_optional(None, lambda x: x * 2) if False else None)  # Output: None
print(or_else(None, "default"))  # Output: "default"
print(or_else("value", "default"))  # Output: "value"