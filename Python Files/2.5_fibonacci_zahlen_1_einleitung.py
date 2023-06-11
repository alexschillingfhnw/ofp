# 1. Einleitung

# Aufgabe 1

import timeit

def fibonacci_rec(n: int) -> int:
	return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

n_list = [10,20,25]

for n in n_list:
    start_time = timeit.default_timer()
    print("Fibonacci: ", fibonacci_rec(n))
    end_time = timeit.default_timer()
    print("Rechenzeit: {} Sekunden".format(round(end_time - start_time,5)))


# fibonacci mit Zähler
cnt = 0

def fibonacci_rec_cnt(n: int) -> int:
    global cnt
    cnt += 1
    return n if n <= 1 else fibonacci_rec_cnt(n - 1) + fibonacci_rec_cnt(n - 2)

n_list = [10,20,25]

for n in n_list:
    print("Anzahl n, Fibonacci, Count: ", n, fibonacci_rec_cnt(n), cnt)