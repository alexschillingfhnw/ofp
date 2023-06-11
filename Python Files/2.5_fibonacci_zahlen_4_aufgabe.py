# 2. Aufgaben mit rekursiven Fibonacci-Funktionen

# Aufgabe 4

import timeit

def fibonacci_rec(n: int, memo: dict = {}) -> (int, int):
    if n in memo: 
        return memo[n]
    elif n <= 1:
        result, cnt = n, 1
    else:
        fib1, cnt1 = fibonacci_rec(n - 1, memo)
        fib2, cnt2 = fibonacci_rec(n - 2, memo)
        result, cnt = fib1 + fib2, cnt1 + cnt2 + 1

    memo[n] = result, cnt
    return result, cnt

n_list = [10,30,50,100,200,400]

for n in n_list:
    start_time = timeit.default_timer()

    fib, cnt = fibonacci_rec(n)
    print("Fibonacci: ", fib)
    print("Count: ", cnt)

    end_time = timeit.default_timer()
    print("Rechenzeit: {} Sekunden".format(end_time - start_time))
