'''
Описание: Создайте дескриптор, который будет автоматически преобразовывать присваиваемые значения в верхний регистр

Входные данные: Встроенные данные для тестирования дескриптора в классе

Выходные данные: Класс с дескриптором, который автоматически преобразует строки в верхний регистр при присвоении

Ограничения: Дескриптор должен работать только со строковыми значениями, для других типов выбрасывать TypeError

Примеры:
Input: создание объекта Person(title="manager") и присвоение person.title = "developer"
Output: объект создается, при обращении к person.title возвращается "MANAGER", после присвоения person.title возвращает "DEVELOPER"

Входные данные: попытка присвоить person.title = 123
Output: TypeError с сообщением о том, что значение должно быть строкой
'''

class UpperCaseDescriptor:
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        instance.__dict__[self.name] = value.upper()

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, "")

    def __set_name__(self, owner, name):
        self.name = name

class Person:
    title = UpperCaseDescriptor()
    def __init__(self, title):
        self.title = title

person = Person("manager")
print(person.title)  # Output: MANAGER
person.title = "developer"
print(person.title)  # Output: DEVELOPER
try:
    person.title = 123
except TypeError as e:
    print(e)  # Output: Value must be a string