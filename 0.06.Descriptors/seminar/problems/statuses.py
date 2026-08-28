"""Задача 3. Перечисление и данные извне.

Данные приходят строками, а внутри программы удобнее работать с элементами
перечисления. Помните: элемент `Enum` не равен своему значению, сравнение со
строкой всегда ложно и ошибки при этом не возникает.
"""

from enum import Enum


class Status(Enum):
    """Состояние заказа."""

    NEW = "new"
    PAID = "paid"
    SHIPPED = "shipped"
    DONE = "done"


def parse(raw: str) -> Status | None:
    """Превратить строку в элемент перечисления.

    Неизвестная строка даёт None, а не ошибку: данные приходят снаружи и могут
    быть какими угодно. Исключений мы ещё не проходили, поэтому проверяйте
    заранее.
    """
    raise NotImplementedError("Implement me")


def parse_all(rows: list[str]) -> list[Status]:
    """Разобрать список строк, выбросив всё неизвестное. Порядок сохраняется."""
    raise NotImplementedError("Implement me")


def values() -> list[str]:
    """Значения всех состояний в порядке объявления."""
    raise NotImplementedError("Implement me")


def is_final(status: Status) -> bool:
    """Завершено ли состояние: доставлен или закрыт."""
    raise NotImplementedError("Implement me")
