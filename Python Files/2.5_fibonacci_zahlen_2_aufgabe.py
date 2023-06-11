# 2. Aufgaben mit rekursiven Fibonacci-Funktionen

# Aufgabe 2

def fibonacci_rec(n: int) -> (int, int):
    if n <= 1:
        return n, 1
    else:
        fib1, cnt1 = fibonacci_rec(n - 1)
        fib2, cnt2 = fibonacci_rec(n - 2)
        return fib1 + fib2, cnt1 + cnt2 + 1

n_list = [10,20]

for n in n_list:
    fib, cnt = fibonacci_rec(n)
    print("Fibonacci, Count: ", fib, cnt)

