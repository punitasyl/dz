# make_pair = создает Tuple из двух значений
# get_first = получает первое значение из Tuple
# get_second = получает второе значение из Tuple
# swap_pair = меняет элементы местами

from typing import Tuple, TypeVar

T = TypeVar('T')
R = TypeVar('R')


def make_pair(x: T, y: R) -> Tuple[T, R]:
    return (x, y)

def get_first(pair: Tuple[T, R]) -> T:
    return pair[0]

def get_second(pair: Tuple[T, R]) -> R:
    return pair[1]

def swap_pair(pair: Tuple[T, R]) -> Tuple[R, T]:
    return (pair[1], pair[0])

pair = make_pair(1, 'hello')
print(get_first(pair))  # Output: 1
print(get_second(pair))  # Output: 'hello'
print(swap_pair(pair))  # Output: ('hello', 1)
