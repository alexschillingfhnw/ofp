from functools import *

def anzahl_gerade(numbers):
    count = reduce(lambda x, y: x + 1, filter(lambda x: x % 2 == 0, numbers), 0)
    return count

print(anzahl_gerade([1,2,3,4,5,6,7,8,9]))        # Output: 4
