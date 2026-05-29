'''
Заказ в интернет магазине
Item - name, price, qty и метод subtotal() -> считает цену
Политики скидок - NoDiscount - без скидки, PercentageDiscount - процент
Order - list[Item] и политика скидок, метод расчёта total total_with_discount
'''

from dataclasses import dataclass
from typing import Protocol

class DiscountPolicy(Protocol):
    def discount(self, total: float) -> float:
        ...


@dataclass
class Item:
    '''Единица товара'''
    name: str
    price: float
    qty: int

    def subtotal(self) -> float:
        '''Расчёт суммы'''
        return self.price * self.qty

class NoDiscount:
    def discount(self, total: float) -> float:
        return 0

@dataclass
class PercentageDiscount:
    percentage: float

    def discount(self, total: float) -> float:
        return total * (self.percentage / 100)

@dataclass
class Order:
    items: list[Item]
    policy: DiscountPolicy

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items)

    def total_with_discount(self) -> float:
        total = self.total()
        return total - self.policy.discount(total)
    
    def set_policy(self, policy: DiscountPolicy):
        self.policy = policy



# Пример использования
basket = [Item("Laptop", 1000.0, 1), Item("Mouse", 50.0, 2)]
order = Order(basket, NoDiscount())
print(f"Total without discount: {order.total()}")
print(f"Total with no discount: {order.total_with_discount()}")
order.set_policy(PercentageDiscount(10))
print(f"Total with 10% discount: {order.total_with_discount()}")