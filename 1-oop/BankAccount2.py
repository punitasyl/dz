'''
Описание: Создайте класс BankAccount с полями accountnumber, balance и owner, затем добавьте классовый метод fromcsv для создания объекта из CSV-строки

Входные данные: Встроенные данные в коде (номер счета, баланс, владелец, CSV-строка для парсинга)

Выходные данные: Информация о созданных банковских счетах через обычный конструктор и через классовый метод

Ограничения: Используйте только базовые возможности Python для создания класса и классового метода с декоратором @classmethod

Примеры:
Входные данные: account_number="ACC001", balance=1500.0, owner="John Doe"
Output: Информация о банковском счете

Входные данные: csv_data="ACC002,2500.0,Jane Smith"
Output: Информация о банковском счете, созданном из CSV
'''

class BankAccount:
    '''Класс для хранения информации о банковском счете
    '''
    def __init__(self, account_number: str, balance: float, owner: str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    @classmethod
    def from_csv(cls, csv_data: str):
        account_number, balance, owner = csv_data.split(",")
        return cls(account_number, float(balance), owner)

account1 = BankAccount(account_number="ACC001", balance=1500.0, owner="John Doe")
csv_data = "ACC002,2500.0,Jane Smith"
account2 = BankAccount.from_csv(csv_data)
print(f"Account 1: Number={account1.account_number}, Balance={account1.balance}, Owner={account1.owner}")
print(f"Account 2: Number={account2.account_number}, Balance={account2.balance}, Owner={account2.owner}")
