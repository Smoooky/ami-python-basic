"""Задача 1. Таблица, у которой строки — разные объекты.

Умножение списка повторяет ссылку, поэтому `[[0] * 3] * 3` даёт три имени для
одной строки. Здесь строки обязаны быть независимыми, и тесты это проверяют
оператором `is`.
"""


def make_grid(rows: int, cols: int) -> list[list[int]]:
    """Таблица rows на cols, заполненная нулями. Все строки — разные объекты."""
    raise NotImplementedError("Implement me")


def set_cell(grid: list[list[int]], row: int, col: int, value: int) -> None:
    """Записать значение в клетку. Таблица меняется на месте, ничего не
    возвращается."""
    raise NotImplementedError("Implement me")


def distinct_rows(grid: list[list[int]]) -> int:
    """Сколько среди строк таблицы различных объектов.

    Две одинаковые по содержимому, но разные строки считаются за две.
    """
    raise NotImplementedError("Implement me")


def shares_rows(grid: list[list[int]]) -> bool:
    """Есть ли в таблице две позиции, занятые одним и тем же объектом-строкой."""
    raise NotImplementedError("Implement me")
