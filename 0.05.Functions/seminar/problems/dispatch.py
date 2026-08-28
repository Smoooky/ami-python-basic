"""Задача 1. Таблица операций вместо цепочки условий.

Функция — такой же объект, как число: её можно положить в словарь значением.
Цепочка `if name == ...` здесь не нужна нигде.
"""

from collections.abc import Callable

Operation = Callable[[int, int], int]


def build_table() -> dict[str, Operation]:
    """Словарь из четырёх операций над двумя числами:

    "плюс" — сумма, "минус" — разность, "умножить" — произведение,
    "максимум" — большее из двух.
    """
    raise NotImplementedError("Implement me")


def known(table: dict[str, Operation]) -> list[str]:
    """Названия операций по алфавиту."""
    raise NotImplementedError("Implement me")


def apply_op(table: dict[str, Operation], name: str, a: int, b: int) -> int | None:
    """Результат операции с указанным названием.

    Если такой операции в таблице нет, возвращается None.
    """
    raise NotImplementedError("Implement me")


def apply_all(table: dict[str, Operation], names: list[str], a: int, b: int) -> list[int | None]:
    """Результаты всех перечисленных операций, в том же порядке.

    Неизвестные названия дают None и из результата не выбрасываются.
    """
    raise NotImplementedError("Implement me")
