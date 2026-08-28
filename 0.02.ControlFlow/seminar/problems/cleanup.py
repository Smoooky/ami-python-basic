"""Задача 3. Списки без изменения на ходу.

Все функции строят новый список включением и не трогают тот, который получили.
Тесты это проверяют отдельно.
"""


def without_negatives(numbers: list[int]) -> list[int]:
    """Список без отрицательных чисел. Ноль остаётся."""
    raise NotImplementedError("Implement me")


def dedup_adjacent(numbers: list[int]) -> list[int]:
    """Список без подряд идущих повторов: [1, 1, 2, 1] -> [1, 2, 1].

    Повторы, стоящие не рядом, сохраняются.
    """
    raise NotImplementedError("Implement me")


def flatten(rows: list[list[int]]) -> list[int]:
    """Все числа таблицы одним списком, строка за строкой.

    Достаточно одного включения с двумя циклами; порядок циклов в нём такой же,
    как у вложенных.
    """
    raise NotImplementedError("Implement me")


def cut_long(words: list[str], limit: int) -> list[str]:
    """Слова, укороченные до limit символов. Короткие остаются как есть."""
    raise NotImplementedError("Implement me")
