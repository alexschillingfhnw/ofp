# --------- map Example ----------- #
print("map Example")

# suqares each element in the list
squared_numbers = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(squared_numbers))

# checks if each element in list is smaller than 4 and prints the result (TRUE or FALSE)
smaller_four = map(lambda x: x < 4, [1, 2, 3, 4, 5])
print(list(smaller_four))

print("--------\n")

# --------- filter Example ----------- #
print("filter Example")

# checks if each element in the list is smaller than 3 and prints out all elements that are true
bigger_3 = filter(lambda x: x < 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(bigger_3))

print("--------\n")

# --------- reduce Example ----------- #
print("reduce Example")

from functools import reduce

# adds each element in the list together and prints 1 value
sum_numbers = reduce(lambda x, y: x + y, [1, 2, 3, 1])
print(sum_numbers)

# multiplies each element in the list and prints 1 value
mult_numbers = reduce(lambda x, y: x * y, [1, 2, 3, 8, 1, 2])
print(mult_numbers)

print("--------\n")

# --------- curry Example ----------- #
print("curry Example")
