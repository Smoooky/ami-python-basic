"""Задача 5. Биты.

Нумерация битов идёт справа налево и начинается с нуля: у числа 5 (двоичное
101) нулевой бит равен 1, первый — 0, второй — 1. Все числа неотрицательны.
"""


def nth_bit(n: int, i: int) -> int:
    """Значение i-го бита числа: 0 или 1. nth_bit(5, 0) == 1, nth_bit(5, 1) == 0."""
    raise NotImplementedError("Implement me")


def set_bit(n: int, i: int) -> int:
    """Число с установленным в единицу i-м битом. Остальные биты не меняются,
    и если бит уже был единицей, число остаётся прежним."""
    raise NotImplementedError("Implement me")


def clear_bit(n: int, i: int) -> int:
    """Число с обнулённым i-м битом. Остальные биты не меняются."""
    raise NotImplementedError("Implement me")


def is_power_of_two(n: int) -> bool:
    """Является ли число степенью двойки. Ноль — не является.

    Подсказка: у степени двойки ровно один единичный бит, а посчитать единицы
    умеет сам int.
    """
    raise NotImplementedError("Implement me")
