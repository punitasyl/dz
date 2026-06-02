# Сделайте типобезопасный generic-класс кэша
# с ключами и значениями произвольных типов.

from typing import TypeVar, Generic, Dict
from dataclasses import dataclass
K = TypeVar('K')
V = TypeVar('V')


class Cache(Generic[K, V]):
    def __init__(self) -> None:
        self._cache: Dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        self._cache[key] = value

    def get(self, key: K) -> V:
        return self._cache[key]
    
    def keys(self) -> list[K]:
        return list(self._cache.keys())
    
    def values(self) -> list[V]:
        return list(self._cache.values())

# Пример использования
hits = Cache[str, int]()
hits.set("home", 100)
hits.set("about", 50)

print(hits.get("home"))  # x будет типа int | None
print(hits.keys()) # list[str]
print(hits.values()) # list[int]


hits.set("contact", "5")  # Ошибка типов, так как значение должно быть int
hits.get(123) # Ошибка типов, так как ключ должен быть str