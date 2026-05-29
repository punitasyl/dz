'''
Бронирование отеля
У нас есть отель, в котором есть номера разных типов (от Room):
 - Обычный номер
 - Люкс (имеет мультипликатор цены)
Гость может:
 - бронировать номер на определённые даты - через класс Booking - бронирование. Его можно отменить.
Отель (класс Hotel) должен:
 - уметь показывать список доступных номеров на заданнь
 - добавить номер
 - забронировать и отменить бронирование
 - показать забронированные номера
'''

from datetime import date, timedelta

class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
    
class Suite(Room):
    def __init__(self, number, price, multiplier):
        super().__init__(number, price)
        self.multiplier = multiplier
    
class Booking:
    def __init__(self, room, start_date, end_date):
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
    
    def cancel(self):
        # Логика отмены бронирования
        pass

class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookings = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def show_available_rooms(self, start_date, end_date):
        # Логика показа доступных номеров
        pass
    
    def book_room(self, room_number, start_date, end_date):
        # Логика бронирования номера
        pass
    
    def cancel_booking(self, booking):
        # Логика отмены бронирования
        pass
    
    def show_booked_rooms(self):
        # Логика показа забронированных номеров
        pass

# Пример использования
hotel = Hotel()
hotel.add_room(Room(101, 100))
hotel.add_room(Suite(201, 200, 1.5))
booking1 = hotel.book_room(101, date(2024, 7, 1), date(2024, 7, 5))
hotel.show_available_rooms(date(2024, 7, 1), date(2024, 7, 5))
hotel.show_booked_rooms()
hotel.cancel_booking(booking1)