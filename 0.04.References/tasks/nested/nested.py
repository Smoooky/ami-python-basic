from typing import Any

# Вложенные данные: числа и списки таких же данных, без циклов.
Data = int | list[Any]


def total(data: Data) -> int:
    raise NotImplementedError("Implement me")


def depth(data: Data) -> int:
    raise NotImplementedError("Implement me")


def flatten(data: Data) -> list[int]:
    raise NotImplementedError("Implement me")


def count_lists(data: Data) -> int:
    raise NotImplementedError("Implement me")


def find(data: Data, target: int) -> list[int] | None:
    raise NotImplementedError("Implement me")
