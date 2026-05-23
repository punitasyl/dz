'''
Описание: Создайте класс Employee с полями name, position и salary, 
затем переопределите метод repr для читабельного строкового представления объекта

Входные данные: Встроенные данные в коде (имя сотрудника, должность, зарплата для нескольких сотрудников)

Выходные данные: Строковое представление каждого созданного объекта Employee при выводе

Ограничения: Используйте только базовые возможности Python для создания класса и переопределения repr

Примеры:
Входные данные: name="John Smith", position="Developer", salary=75000
Output: Employee(name='John Smith', position='Developer', salary=75000)

Входные данные: name="Sarah Johnson", position="Manager", salary=85000
Output: Employee(name='Sarah Johnson', position='Manager', salary=85000)
'''

class Employee:
    '''Класс для хранения информации о сотруднике
    '''
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', position='{self.position}', salary={self.salary})"
    
employee1 = Employee(name="John Smith", position="Developer", salary=75000)
employee2 = Employee(name="Sarah Johnson", position="Manager", salary=85000)
print(employee1)
print(employee2)