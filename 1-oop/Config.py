'''
Описание: Создайте класс Config с полями appname, version и debugmode, затем переопределите метод eq для сравнения объектов конфигурации по содержимому

Входные данные: Встроенные данные в коде (название приложения, версия, режим отладки для нескольких конфигураций)

Выходные данные: Результаты сравнения различных объектов конфигурации между собой

Ограничения: Используйте только базовые возможности Python для создания класса и переопределения eq

Примеры:
Входные данные: appname="MyApp", version="1.0.0", debugmode=True
Output: Результат сравнения с другими конфигурациями

Входные данные: appname="MyApp", version="1.0.0", debugmode=False
Output: Результат сравнения с идентичными и различными конфигурациями
'''

class Config:

    def __init__(self, app_name: str, version: str, debug_mode: bool):
        self.app_name = app_name
        self.version = version
        self.debug = debug_mode

    def __eq__(self, other):
        if not isinstance(other, Config):
            return NotImplemented
        return (self.app_name == other.app_name and
                self.version == other.version and
                self.debug == other.debug)

config1 = Config("MyApp", "1.0", True)
config2 = Config("MyApp", "1.0", True)
print(config1 == config2)  # True
config3 = Config("MyApp", "1.0", False)
print(config1 == config3)  # False