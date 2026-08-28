from collections.abc import Callable
from typing import Any


def compose(steps: list[Callable[[int], int]]) -> Callable[[int], int]:
    raise NotImplementedError("Implement me")


def partial(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[..., Any]:
    raise NotImplementedError("Implement me")


def repeat(func: Callable[[int], int], times: int) -> Callable[[int], int]:
    raise NotImplementedError("Implement me")
