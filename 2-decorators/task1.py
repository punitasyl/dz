

def log(fn):
    def wrapper():
        print(f"Calling '{fn.__name__}'")
        result = fn()
        return result
    return wrapper

@log
def hello():
    print("Hello, World!")

@log
def calculate():
    print(42)

hello()
calculate()