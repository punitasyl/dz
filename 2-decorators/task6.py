'''
Описание: Создайте декоратор, который будет кэшировать результат выполнения функции 
и возвращать сохранённое значение при повторном вызове с теми же аргументами

Входные данные: Встроенная функция для декорирования

Выходные данные: Декорированная функция, которая кэширует результаты и выводит информацию о кэше

Ограничения: Декоратор должен работать с функциями с любым количеством позиционных аргументов, 
кэш должен быть уникальным для каждой комбинации аргументов

Примеры:
Input: вызов декорированной функции expensive_calc(2, 3) дважды
Output:
Calculating...
Result: 5
Using cached result
Result: 5

Входные данные: вызов декорированной функции process("hello") и затем process("world")
Output:
Processing...
Result: HELLO
Processing...
Result: WORLD
'''

from functools import wraps


def cache(func):
    cached_results = {} # Словарь для хранения кэшированных результатов
    
    @wraps(func)
    def wrapper(*args):
        if args in cached_results: 
            print("Using cached result")
            return cached_results[args]
        
        print("Calculating...")
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper

@cache
def expensive_calc(x, y):
    return x + y

@cache
def process(text):
    return text.upper()

# Testing the cache decorator
print(expensive_calc(2, 3))  # Output: Calculating... Result: 5
print(expensive_calc(2, 3))  # Output: Using cached result Result: 5
print(process("hello"))  # Output: Processing... Result: HELLO
print(process("world"))  # Output: Processing... Result: WORLD
print(process("hello"))  # Output: Using cached result Result: HELLO