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