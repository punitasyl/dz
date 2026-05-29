# Хранилище
# Нужно реалозовать MemoryStorage и FileStorage с методами load и save
# Приложение чистает строку и передаёт в use_storage, сохраняет в одном из storage
# После успешного сохранения читает storage и выводит сохранённые данные

from abc import ABC, abstractmethod
import json
import os
from typing import Protocol

class Storage(ABC):

    @abstractmethod
    def save(self, data: str) -> None:
        ...

    @abstractmethod
    def load(self) -> str:
        ...

    def log(self):
        print("Data has been saved.")

class MemoryStorage(Storage):

    def save(self, data: str):
        self.data = data
        self.log()

    def load(self) -> str:
        return getattr(self, 'data', '')

class FileStorage(Storage):

    def save(self, data: str) -> None:
        with open("data.txt", 'w', encoding='utf-8') as f:
            f.write(data)
        self.log()
        
    def load(self) -> str:
        if not os.path.exists("data.txt"):
            return ""
        with open("data.txt", 'r', encoding='utf-8') as f:
            return f.read()
    
def use_storage(storage: Storage, data: str):
    storage.save(data)
    return storage.load()

# Пример использования
mem = MemoryStorage()
file = FileStorage()

user_input = input("Введите строку для сохранения: ")
print(use_storage(mem, user_input))  # Output: Hello, World!
print(use_storage(file, user_input))  # Output: Hello, World!