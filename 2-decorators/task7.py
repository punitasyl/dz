'''
Описание: Создайте декоратор, который будет перехватывать исключения в декорируемой функции и возвращать значение 
по умолчанию вместо выброса исключения

Входные данные: Встроенная функция для декорирования

Выходные данные: Декорированная функция, которая возвращает значение по умолчанию при возникновении исключения

Ограничения: Декоратор должен перехватывать любые исключения и возвращать None как значение по умолчанию

Примеры:
Input: вызов декорированной функции divide(10, 2)
Output: 5.0

Входные данные: вызов декорированной функции divide(10, 0)
Output: None

'''
from functools import wraps

def catch_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return None
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

# Testing the catch_exceptions decorator
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: None
