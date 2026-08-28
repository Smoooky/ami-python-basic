from collections.abc import Callable, Sequence
from typing import Any

Decorator = Callable[[Callable[..., Any]], Any]


def logged(log: list[str]) -> Decorator:
    raise NotImplementedError("Implement me")


def doubled(func: Callable[..., Any]) -> Any:
    raise NotImplementedError("Implement me")


def checked(func: Callable[..., Any]) -> Any:
    raise NotImplementedError("Implement me")


def apply(decorators: Sequence[Decorator], func: Callable[..., Any]) -> Any:
    raise NotImplementedError("Implement me")
