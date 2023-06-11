from functools import reduce

# Reduce 
def mein_filter(func, numbers):
    return reduce(lambda acc, x: acc + [x] if func(x) else acc, numbers, [])

def mein_filter2(func, numbers):
    return reduce(lambda acc, x: acc + x if func(x) else acc, numbers, 0)

print(mein_filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: [4, 5, 6, 7, 8, 9]
print(mein_filter2(lambda x: x > 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 39