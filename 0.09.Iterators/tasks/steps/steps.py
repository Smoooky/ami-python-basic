from collections.abc import Iterable, Iterator
from typing import Any


def windows(values: Iterable[int], size: int) -> Iterator[tuple[int, ...]]:
    raise NotImplementedError("Implement me")


def averages(values: Iterable[int], size: int) -> Iterator[float]:
    raise NotImplementedError("Implement me")


def dedupe(values: Iterable[int]) -> Iterator[int]:
    raise NotImplementedError("Implement me")


def runs(values: Iterable[int]) -> Iterator[tuple[int, int]]:
    raise NotImplementedError("Implement me")
