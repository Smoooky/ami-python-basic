from collections.abc import Callable
from typing import Any

# Декоратор — это то, что принимает функцию и возвращает замену для неё.
Decorator = Callable[[Callable[..., Any]], Any]


def at_most(times: int) -> Decorator:
    raise NotImplementedError("Implement me")


def default_on_error(value: Any, *errors: type[BaseException]) -> Decorator:
    raise NotImplementedError("Implement me")


def clamped(low: int, high: int) -> Decorator:
    raise NotImplementedError("Implement me")
