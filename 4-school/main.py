
# Single Responsibility Principle (SRP) - Принцип единственной ответственности



# Принцип открытости/закрытости (Open/Closed Principle - OCP)
# Классы должны быть открыты для расширения, но закрыты для модификации.

# from dataclasses import dataclass


# @dataclass
# class DiscountCalculator:
#     def calculate(self, price):
#         return 0
    

#LSP - Liskov Substitution Principle - Принцип подстановки Барбары Лисков
# Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения правильности выполнения программы.

# @dataclass
# class User:
#     name: str
#     bonus: int = 0

#     def add_bonus(self, amount: int):
#         self.bonus += amount
#         print(f"{self.name} received a bonus of {amount}. Total bonus: {self.bonus}")


# class PremiumUser(User):
#     def add_bonus(self, amount: int):
#         super().add_bonus(amount * 2)  # Premium users receive double bonus

# class BannedUser(User):
#     def add_bonus(self, amount: int):
#         print(f"{self.name} is banned and cannot receive bonuses.")

# user = User(name="Alice")
# premium_user = PremiumUser(name="Bob")
# banned_user = BannedUser(name="Charlie")
# user.add_bonus(10)  # Alice received a bonus of 10. Total bonus: 10
# premium_user.add_bonus(10)  # Bob received a bonus of 20. Total bonus
# banned_user.add_bonus(10)  # Charlie is banned and cannot receive bonuses.


