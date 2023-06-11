# 2. Aufgaben mit rekursiven Fibonacci-Funktionen

# Aufgabe 3

def fibonacci_rec(n: int, memo: dict = {}) -> int:
    # Prüft, ob das Ergebnis bereits im Dictionary gespeichert ist
    if n in memo: 
        # Wenn ja, gibt das gespeicherte Ergebnis zurück
        return memo[n]
     # Wenn n 0 oder 1 ist, ist das Ergebnis n selbst
    elif n <= 1:
        result = n
    else:  
        # Wenn n grösser als 1 ist, berechnet das Ergebnis als Summe der beiden vorherigen Fibonacci-Zahlen.
        fib1 =  fibonacci_rec(n - 1, memo)
        fib2 = fibonacci_rec(n - 2, memo)
        result = fib1 + fib2

    memo[n] = result 

    print(memo)

    return result  

print(fibonacci_rec(40))  
