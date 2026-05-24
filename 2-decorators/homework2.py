
'''
Декоратор для ограничения числовых аргументов функции.
Параметры:
 - max_value: максимальное допустимое значение для числовых аргументов
 - mode: "error" или "clip"
- "error" - при превышении max_value выбрасывать исключение ValueError
- "clip" - при превышении max_value заменять значение на max_value
'''

def limit_args(max_value: int, mode: str = "clip"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = []
            for arg in args:
                if isinstance(arg, (int, float)):
                    if arg > max_value:
                        if mode == "error":
                            raise ValueError(f"Argument {arg} exceeds the maximum value of {max_value}")
                        elif mode == "clip":
                            new_args.append(max_value)
                        else:
                            raise ValueError("Invalid mode. Use 'error' or 'clip'.")
                    else:
                        new_args.append(arg)
                else:
                    new_args.append(arg)
            return func(*new_args, **kwargs)
        return wrapper
    return decorator
    

@limit_args(100, mode="error")
def multiply(a, b):
    return a * b


print(multiply(5, 3))    
print(multiply(900, 3))  