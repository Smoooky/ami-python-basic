"""Задача 1. Деление, остаток и арифметика над сравнениями.

Условных конструкций мы ещё не проходили — они не нужны ни в одной функции.
Всё решается операторами `//`, `%`, `divmod` и сравнениями, которые дают 0 и 1.
"""


def sign(n: int) -> int:
    """Знак числа: 1 для положительных, -1 для отрицательных, 0 для нуля."""
    raise NotImplementedError("Implement me")


def same_sign(a: int, b: int) -> bool:
    """Одного ли знака числа. Ноль считается неотрицательным, как и любое
    положительное число."""
    raise NotImplementedError("Implement me")


def ceil_div(a: int, b: int) -> int:
    """Деление вверх: наименьшее целое, не меньшее a / b. Делитель положителен.

    ceil_div(7, 2) == 4, ceil_div(8, 2) == 4, ceil_div(-7, 2) == -3.
    Результат обязан быть int, поэтому через float считать нельзя.
    """
    raise NotImplementedError("Implement me")


def clock_add(hour: int, shift: int) -> int:
    """Час на 24-часовом циферблате через shift часов. Сдвиг может быть
    отрицательным и по модулю больше суток; результат — от 0 до 23."""
    raise NotImplementedError("Implement me")


def split_time(total: int) -> tuple[int, int, int]:
    """Часы, минуты и секунды в total секундах: 3661 -> (1, 1, 1).

    Достаточно двух вызовов divmod.
    """
    raise NotImplementedError("Implement me")
