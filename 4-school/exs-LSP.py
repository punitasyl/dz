# Принцип замещения Лисков (Liskov Substitution Principle - LSP)

# Создать 4 метода платежи:
# - Все сумму
# - Все сумму - число бонусов
# - Деление на N частей, 1 сразу, остальные потом 


from dataclasses import dataclass



class Payment:
    
    def pay(self, amount: float):
        print(f"Списано: {amount}")
        return amount

@dataclass
class BonusPayment(Payment):
    bonuses: float

    def pay(self, amount: float) -> float:
        total_amount = amount - self.bonuses
        print(f"Списано: {total_amount} (с учетом бонусов: {self.bonuses})")
        return total_amount

@dataclass
class InstallmentPayment(Payment):
    installments: int

    def pay(self, amount: float) -> float:
        final = amount / self.installments
        print(f"Списано: {final} (в {self.installments} частях)")
        return final


def pay(method: Payment):
    method.pay(1000)