from collections.abc import Iterable, Iterator
from typing import Any

# Строка журнала: предмет и балл.
Row = tuple[str, int]


def only(rows: Iterable[Row], subject: str) -> Iterator[Row]:
    raise NotImplementedError("Implement me")


def scores(rows: Iterable[Row]) -> Iterator[int]:
    raise NotImplementedError("Implement me")


def passing(values: Iterable[int], threshold: int) -> Iterator[int]:
    raise NotImplementedError("Implement me")


def first(values: Iterable[Any], count: int) -> Iterator[Any]:
    raise NotImplementedError("Implement me")


def average(values: Iterable[int]) -> float | None:
    raise NotImplementedError("Implement me")
