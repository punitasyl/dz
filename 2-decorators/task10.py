'''
Описание: Создайте дескриптор, который будет автоматически округлять присваиваемые числовые значения 
          до заданного количества знаков после запятой

Входные данные: Встроенные данные для тестирования дескриптора в классе

Выходные данные: Класс с дескриптором, который автоматически округляет числовые значения при присвоении

Ограничения: Дескриптор должен работать только с числовыми значениями (int, float), для других типов выбрасывать TypeError

Примеры:
Input: создание объекта Product(price=19.999) и присвоение product.price = 25.6789
Output: объект создается, при обращении к product.price возвращается 20.00, после присвоения product.price возвращает 25.68

Входные данные: попытка присвоить product.price = "invalid"
Output: TypeError с сообщением о том, что значение должно быть числом
'''

class RoundedValue:

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("RoundedValue.__init__ must be called with int or float")
        instance.__dict__[self.name] = round(value, 2)

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

class Product:
    price = RoundedValue()

    def __init__(self, price):
        self.price = price

product1 = Product(45.48424)
product2 = Product(95.4523234135)
product3 = Product(14.43)
print(product1.price)
print(product2.price)
print(product3.price)



