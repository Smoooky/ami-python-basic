from collections import deque
from collections.abc import Iterable


def shift(people: Iterable[str], step: int) -> list[str]:
    raise NotImplementedError("Implement me")


def serve(people: Iterable[str], step: int) -> list[str]:
    raise NotImplementedError("Implement me")


def last(events: Iterable[str], size: int) -> deque[str]:
    raise NotImplementedError("Implement me")


def is_palindrome(text: str) -> bool:
    raise NotImplementedError("Implement me")
