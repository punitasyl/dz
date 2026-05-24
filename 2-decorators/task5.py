'''
Создайте дескриптор, который будет валидировать, что присваиваемое значение является строкой и имеет минимальную длину

Входные данные: Встроенные данные для тестирования дескриптора в классе

Выходные данные: Класс с дескриптором, который корректно валидирует строковые значения и их длину

Ограничения: Дескриптор должен проверять тип данных (строка) и минимальную длину, выбрасывать исключения при нарушении условий

Примеры:
Input: создание объекта User(name="Alice") и присвоение user.name = "Bob"
Output: объект создается успешно, значение присваивается без ошибок

Входные данные: попытка присвоить user.name = "" (пустая строка)
Output: ValueError с сообщением о нарушении минимальной длины

Входные данные: попытка присвоить user.name = 123 (не строка)
Output: TypeError с сообщением о неверном типе данных
'''


class StringDescriptor:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")

        if len(value) < self.min_length:
            raise ValueError(f"Value must be at least {self.min_length} characters long")
        
        instance.__dict__[self.__class__.__name__] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__class__.__name__]

class User:
    name = StringDescriptor(min_length=3)

    def __init__(self, name):
        self.name = name

# Testing the descriptor
try:
    user = User(name="Alice")
    print(user.name)  # Output: Alice

    user.name = "Bob"
    print(user.name)  # Output: Bob

    user.name = ""  # This will raise a ValueError
except ValueError as ve:
    print(ve)

try:
    user = User(name="Alice")
    print(user.name)  # Output: Alice

    user.name = "Bob"
    print(user.name)  # Output: Bob

    user.name = 123  # This will raise a TypeError
except TypeError as te:
    print(te)


