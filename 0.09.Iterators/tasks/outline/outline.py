from collections.abc import Iterable, Iterator
from typing import Any

# Пункт плана: либо строка, либо вложенный список пунктов.
Item = str | list["Item"]


def flat(outline: Iterable[Item]) -> Iterator[str]:
    raise NotImplementedError("Implement me")


def numbered(outline: Iterable[Item], level: int = 0) -> Iterator[tuple[int, str]]:
    raise NotImplementedError("Implement me")


def depth(outline: Iterable[Item]) -> int:
    raise NotImplementedError("Implement me")


def chain(*sources: Iterable[Any]) -> Iterator[Any]:
    raise NotImplementedError("Implement me")
