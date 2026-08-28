from collections.abc import Iterable, Iterator
from pathlib import Path


def walk(root: Path) -> Iterator[Path]:
    raise NotImplementedError("Implement me")


def take[T](source: Iterable[T], count: int) -> list[T]:
    raise NotImplementedError("Implement me")


def first(root: Path, suffix: str) -> Path | None:
    raise NotImplementedError("Implement me")


def by_suffix(root: Path) -> dict[str, int]:
    raise NotImplementedError("Implement me")


def total_size(root: Path) -> int:
    raise NotImplementedError("Implement me")


def largest(root: Path) -> Path | None:
    raise NotImplementedError("Implement me")
