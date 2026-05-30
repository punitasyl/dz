'''
Задача:
Создать сервис Low Stock Service с методом run.
Метод проверяет остатки в репозитории (In-Memory Stock Repository) и отправляет уведомления, если остаток менее 10 единиц, через email notifier.
Архитектура:
Определены три основных компонента: Low Stock Service, In-Memory Stock Repository и email notifier.
Необходимо использовать принцип инверсии зависимости, чтобы сделать систему гибкой к изменениям.
Реализация принципа:
Введены абстракции через протоколы для репозитория и нотификатора.
StockRepository интерфейс с методом get_stock_count.
Notifier интерфейс с методом notify.
Low Stock Service работает с любыми реализациями, соответствующими этим интерфейсам.
Кодирование:
Создан класс InMemoryStockRepository с методом get_stock_count.
Создан класс EmailNotifier с методом notify.
Low Stock Service использует зависимости через инъекцию протоколов, отвязываясь от конкретных реализаций.
'''

from dataclasses import dataclass
from typing import Protocol


class StockRepository(Protocol):
    def get_stock_count(self) -> int:
        ...

class Notifier(Protocol):
    def notify(self, message: str):
        ...

@dataclass    
class InMemoryStockRepository(StockRepository):
    items_count: int

    def get_stock_count(self) -> int:
        return self.items_count

@dataclass
class EmailNotifier(Notifier):
    def notify(self, message: str):
        print(f"Sending email notification: {message}")
    
@dataclass
class LowStockService:
    stock_repository: StockRepository
    notifier: Notifier

    def run(self, ):
        stock_count = self.stock_repository.get_stock_count()
        if stock_count <= 10:
            self.notifier.notify(f"Low stock")
        else:
            self.notifier.notify(f"Stock is sufficient")


service = LowStockService(InMemoryStockRepository(11), EmailNotifier())
service.run()
