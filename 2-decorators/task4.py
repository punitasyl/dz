'''
Описание: Создайте декоратор, который будет измерять время выполнения декорируемой функции и выводить это время в миллисекундах

Входные данные: Встроенная функция для декорирования

Выходные данные: Декорированная функция, которая выводит время выполнения перед возвратом результата

Ограничения: Декоратор должен работать с функциями с любым количеством аргументов и возвращать исходный результат

Примеры:
Input: вызов декорированной функции calculate(5, 3)
Output:
Execution time: 0.123 ms
8

Входные данные: вызов декорированной функции process_data()
Output:
Execution time: 0.456 ms
Data processed

'''

from time import time
import time
from functools import wraps

def timeit(func):
  

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time: {execution_time:.3f} ms")
        return result

    return wrapper

@timeit
def calculate(a, b):
    return a + b

@timeit
def process_data():
    time.sleep(0.1)  # Simulate some processing time
    return "Data processed"

print(calculate(5, 3))
print(process_data())