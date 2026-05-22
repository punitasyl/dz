'''Описание: Создайте класс Book с полями title, author и pages, затем создайте экземпляр этого класса и выведите информацию о книге.

Входные данные: Встроенные данные в коде (название книги, автор, количество страниц)

Выходные данные: Информация о созданной книге в формате строки

Ограничения: Используйте только базовые возможности Python для создания класса

Примеры:
Входные данные: title="1984", author="George Orwell", pages=328
Output: Информация о книге в читаемом формате

Входные данные: title="Python Programming", author="John Smith", pages=450
Output: Информация о книге в читаемом формате'''


class Book:
    '''Класс для хранения информации о книге
    '''
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}")
