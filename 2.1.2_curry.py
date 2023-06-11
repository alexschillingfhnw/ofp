# curry is a function that takes two arguments: func and fixed_arg
# func is a function that takes two arguments: a and b
# fixed_arg is an integer
# curried is a function that takes one argument: c
# curried returns the result of calling func with fixed_arg and c
# curry returns curried

def curry(func, fixed_arg):
    def curried(*args):
        return func(fixed_arg, *args)
    return curried

def add(a: int, b: int, c: int):
    return a + b + c

bar = curry(add, 2)
print(bar(1, 3))                    # Output: 6

bar2 = curry(add, 5)
print(bar2(7, 1))                   # Output: 13
