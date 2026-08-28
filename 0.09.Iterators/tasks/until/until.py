from collections.abc import Callable
from typing import Any


def collect(source: Callable[[], Any], sentinel: Any) -> list[Any]:
    raise NotImplementedError("Implement me")


def read_chunks(read: Callable[[int], str], size: int) -> list[str]:
    raise NotImplementedError("Implement me")


def first_hit(source: Callable[[], Any], sentinel: Any, target: Any) -> int | None:
    raise NotImplementedError("Implement me")
