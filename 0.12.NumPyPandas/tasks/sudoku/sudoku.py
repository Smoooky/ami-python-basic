import numpy as np
import numpy.typing as npt

# Поле судоку: 9x9, числа от 1 до 9, ноль — пустая клетка.
Grid = npt.NDArray[np.int8]
# Одна девятка: строка, столбец или квадрат, вытянутый в девять чисел.
Group = npt.NDArray[np.int8]

SIZE = 9
BLOCK = 3


def check(grid: Grid) -> None:
    raise NotImplementedError("Implement me")


def rows(grid: Grid) -> Grid:
    raise NotImplementedError("Implement me")


def columns(grid: Grid) -> Grid:
    raise NotImplementedError("Implement me")


def blocks(grid: Grid) -> Grid:
    raise NotImplementedError("Implement me")


def has_repeats(group: Group) -> bool:
    raise NotImplementedError("Implement me")


def mistakes(grid: Grid) -> list[str]:
    raise NotImplementedError("Implement me")


def is_complete(grid: Grid) -> bool:
    raise NotImplementedError("Implement me")


def is_valid(grid: Grid) -> bool:
    raise NotImplementedError("Implement me")
