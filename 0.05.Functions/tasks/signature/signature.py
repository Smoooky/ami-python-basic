from collections.abc import Callable
from typing import Any


def linear(x: float, /, slope: float = 1.0, intercept: float = 0.0) -> float:
    raise NotImplementedError("Implement me")


def settings(*, host: str, port: int = 80) -> str:
    raise NotImplementedError("Implement me")


def mixed(a: int, b: int = 0, /, *, c: int = 0) -> int:
    raise NotImplementedError("Implement me")


def move(distance: int, /, **options: Any) -> tuple[int, dict[str, Any]]:
    raise NotImplementedError("Implement me")


def call_with(func: Callable[..., Any], positional: list[Any], named: dict[str, Any]) -> Any:
    raise NotImplementedError("Implement me")
