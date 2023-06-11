def multiply_by_2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_by_2
def calculate(x, y):
    return x + y

print(calculate(3, 4))