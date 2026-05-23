'''
Описание: Создайте класс Student с полями name, studentid и grades (список оценок), затем добавьте статический метод isvalid_id для проверки корректности студенческого ID

Входные данные: Встроенные данные в коде (имя студента, ID, список оценок, тестовые ID для проверки)

Выходные данные: Информация о созданном студенте и результаты проверки различных ID

Ограничения: Используйте только базовые возможности Python для создания класса и статического метода с декоратором @staticmethod

Примеры:
Входные данные: name="Alice", student_id="ST2024001", grades=[85, 92, 78]
Output: Информация о студенте и результат проверки ID

Входные данные: test_id="ST2024002"
Output: True (ID корректен)

Входные данные: test_id="INVALID123"
Output: False (ID некорректен)
'''

class Student:

    def __init__(self, name, student_id, grades: list[float]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("ST") and len(student_id) == 9 and student_id[2:].isdigit()
    

student1 = Student("Alice", "ST2024001", [85.5, 90.0, 78.0])
print(f"Student: {student1.name}, ID: {student1.student_id}, Grades: {student1.grades}")
print(f"Is valid ID: {Student.is_valid_id('INVALID123')}") 