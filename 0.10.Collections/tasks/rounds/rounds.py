from collections.abc import Iterable, Sequence


def duty(people: Sequence[str], weeks: int) -> list[str]:
    raise NotImplementedError("Implement me")


def numbered(items: Iterable[str], start: int = 1, step: int = 1) -> list[tuple[int, str]]:
    raise NotImplementedError("Implement me")


def padded(items: Iterable[str], size: int, filler: str) -> list[str]:
    raise NotImplementedError("Implement me")


def page(items: Iterable[str], number: int, size: int) -> list[str]:
    raise NotImplementedError("Implement me")
