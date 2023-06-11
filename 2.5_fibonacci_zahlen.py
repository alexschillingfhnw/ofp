# füge rechenzeit hinzu
import timeit

def fibonacci_rec(n: int) -> int:
	return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

n_list = [10,20]

for n in n_list:
    start_time = timeit.default_timer()
    #print(fibonacci_rec(n))
    end_time = timeit.default_timer()
    print("Rechenzeit: {} Sekunden".format(round(end_time - start_time,5)))


cnt = 0

def fibonacci_rec_cnt(n: int) -> int:
    global cnt
    cnt += 1
    return n if n <= 1 else fibonacci_rec_cnt(n - 1) + fibonacci_rec_cnt(n - 2)


def fibonacci_rec_cnt_new(n: int) -> (int, int):
    if n <= 1:
        return n, 1
    else:
        fib1, cnt1 = fibonacci_rec_cnt_new(n - 1)
        fib2, cnt2 = fibonacci_rec_cnt_new(n - 2)
        return fib1 + fib2, cnt1 + cnt2 + 1

n_list = [10,20]

for n in n_list:
    fib, cnt = fibonacci_rec_cnt_new(n)
    print(fib, cnt)
