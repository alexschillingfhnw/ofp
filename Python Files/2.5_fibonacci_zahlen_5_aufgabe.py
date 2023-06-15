# 3. Aufgaben mit Dekorator

# Aufgabe 5
import functools
import timeit

@functools.lru_cache
def fibonacci_rec(n: int) -> int:
    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

n_list = [10,30,50,100,200,400]

for n in n_list:
    start_time = timeit.default_timer()

    fib = fibonacci_rec(n)
    print("Fibonacci: ", fib)

    end_time = timeit.default_timer()
    print("Rechenzeit: {} Sekunden".format(end_time - start_time))
