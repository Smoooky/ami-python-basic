"""Задача 2. Объект, который годится в множество.

Свой `__eq__` отменяет унаследованный хеш, и объект перестаёт быть хешируемым.
Хеш придётся задать самому — по тем же полям, по которым сравниваете, иначе
равные объекты попадут в разные ячейки и множество их не схлопнет.
"""


class Coord:
    """Точка на карте: широта и долгота."""

    def __init__(self, lat: int, lon: int) -> None:
        """Сохранить координаты."""
        raise NotImplementedError("Implement me")

    def __eq__(self, other: object) -> bool:
        """Две точки равны, если совпадают обе координаты.

        Сравнение с объектом другого типа даёт False, а не ошибку.
        """
        raise NotImplementedError("Implement me")

    def __hash__(self) -> int:
        """Хеш по тем же полям, что участвуют в сравнении."""
        raise NotImplementedError("Implement me")


def unique(points: list[Coord]) -> int:
    """Сколько среди точек различных. Повторы схлопываются."""
    raise NotImplementedError("Implement me")
