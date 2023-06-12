from typing import Callable

Averager = (Callable[[float], None], Callable[[], float])


def new_averager() -> Averager:
    tot, num = 'tot', 'num'
    state = {tot: 0, num: 0}

    def add_value(x: float):
        state[tot] += x
        state[num] += 1

    def get_average() -> float:
        return state[tot] / state[num]

    return add_value, get_average


# Erstellt eine neue Instanz von Averager
add_value, get_average = new_averager()

# Fügt einige Werte hinzu
add_value(10)
add_value(20)
add_value(30)

# Gibt den aktuellen Durchschnitt aus
print("Durchschnitt: ", get_average())