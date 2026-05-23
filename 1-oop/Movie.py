
'''
Описание: Создайте класс Movie с полями title, director и duration, затем добавьте метод экземпляра getdurationhours для преобразования длительности из минут в часы и минуты

Входные данные: Встроенные данные в коде (название фильма, режиссер, длительность в минутах для нескольких фильмов)

Выходные данные: Информация о каждом фильме и его длительности в формате часы:минуты

Ограничения: Используйте только базовые возможности Python для создания класса и методов экземпляра

Примеры:
Входные данные: title="The Matrix", director="Wachowski Sisters", duration=136
Output: Фильм "The Matrix" (режиссер: Wachowski Sisters), длительность: 2:16

Входные данные: title="Inception", director="Christopher Nolan", duration=148
Output: Фильм "Inception" (режиссер: Christopher Nolan), длительность: 2:28
'''

class Movie:

    def __init__(self, title: str, director: str, duration: int):
        self.title = title
        self.director = director
        self.duration = duration
    
    @property
    def get_duration_hours(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return f"{hours}:{minutes:02d}"

movie1 = Movie("Inception", "Christopher Nolan", 136)
print(f"Movie: {movie1.title}, Director: {movie1.director}, Duration: {movie1.get_duration_hours}")