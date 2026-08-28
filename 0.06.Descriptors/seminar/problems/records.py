"""Задача 4. Датакласс вместо ручной обвязки.

Декоратор сам порождает `__init__`, `__repr__` и `__eq__`, а `frozen=True`
вдобавок запрещает менять поля — и потому делает объект хешируемым.

Изменяемое значение по умолчанию датакласс не разрешит: класс просто не
создастся. Здесь оно и не нужно.
"""

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Measurement:
    """Одно измерение: момент времени и значение.

    Поля объявляются в том порядке, в котором их сравнивают: сначала момент,
    потом значение.
    """

    moment: int
    value: int


def latest(rows: list[Measurement]) -> Measurement | None:
    """Измерение с наибольшим моментом. На пустом списке — None."""
    raise NotImplementedError("Implement me")


def distinct(rows: list[Measurement]) -> int:
    """Сколько среди измерений различных. Датакласс с frozen хешируем."""
    raise NotImplementedError("Implement me")


def in_order(rows: list[Measurement]) -> list[Measurement]:
    """Измерения по возрастанию. Исходный список не меняется."""
    raise NotImplementedError("Implement me")
