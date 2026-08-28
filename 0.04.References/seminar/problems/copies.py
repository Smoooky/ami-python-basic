"""Задача 5. Поверхностная и глубокая копия руками.

Модулем `copy` пользоваться здесь не нужно: обе копии собираются включением.
Разница только в том, копируются ли внутренние строки таблицы.
"""


def shallow(rows: list[list[int]]) -> list[list[int]]:
    """Новый внешний список, внутри — те же самые строки, что и в исходном."""
    raise NotImplementedError("Implement me")


def deep(rows: list[list[int]]) -> list[list[int]]:
    """Копия, в которой новые и внешний список, и каждая строка."""
    raise NotImplementedError("Implement me")


def is_independent(first: list[list[int]], second: list[list[int]]) -> bool:
    """Правда ли, что две таблицы не делят между собой ни одной строки.

    Сравнивать нужно объекты, а не содержимое: одинаковые по значению, но
    разные строки независимости не нарушают.
    """
    raise NotImplementedError("Implement me")
