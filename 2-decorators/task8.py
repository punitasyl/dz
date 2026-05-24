'''
Описание: Создайте декоратор, который будет проверять типы аргументов функции 
и выбрасывать исключение при несоответствии ожидаемым типам

Входные данные: Встроенная функция для декорирования с типизированными параметрами

Выходные данные: Декорированная функция, которая проверяет типы аргументов перед выполнением

Ограничения: Декоратор должен принимать словарь с именами параметров и их ожидаемыми типами, выбрасывать TypeError при несоответствии

Примеры:
Input: вызов декорированной функции add_numbers(5, 3)
Output: 8

Входные данные: вызов декорированной функции add_numbers("5", 3)
Output: TypeError: Argument 'a' must be of type <class 'int'>, got <class 'str'>
'''

from functools import wraps

def type_check(expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg_name, expected_type in expected_types.items():
                if arg_name in kwargs:
                    arg_value = kwargs[arg_name]
                else:
                    arg_index = func.__code__.co_varnames.index(arg_name)
                    if arg_index < len(args):
                        arg_value = args[arg_index]
                    else:
                        continue  # Аргумент не был передан, пропускаем проверку

                if not isinstance(arg_value, expected_type):
                    raise TypeError(f"Argument '{arg_name}' must be of type {expected_type}, got {type(arg_value)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check({'a': int, 'b': int})
def add_numbers(a, b):
    return a + b

# Testing the type_check decorator
print(add_numbers(5, 3))  # Output: 8
try:
    print(add_numbers("5", 3))  # This will raise a TypeError
except TypeError as te:
    print(te)  # Output: Argument 'a' must be of type <class 'int'>, got <class 'str'>