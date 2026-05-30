

from abc import ABC, abstractmethod


class Payable(ABC):

    @abstractmethod
    def refund(self, amount):
        pass

class Tokenazable(ABC):

    @abstractmethod
    def tokenize_card(self, data):
        pass

class BalanceCheckable(ABC):

    @abstractmethod
    def check_balance(self, amount):
        pass


class Card(Payable, Tokenazable):
    def pay(self, amount):
        print(f"Оплата по карте: {amount}")

    def refund(self, amount):
        print(f"Возврат средств по карте: {amount}")

    def tokenize_card(self, data):
        print(f"Токенизация данных карты: {data}")
    