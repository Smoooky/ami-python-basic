from collections.abc import Callable
from typing import Any


class Memo:
    """Класс-декоратор: запоминает результаты по аргументам."""

    def __init__(self, size: int | None = None) -> None:
        raise NotImplementedError("Implement me")

    @staticmethod
    def key(*args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("Implement me")

    def __call__(self, func: Callable[..., Any]) -> Any:
        raise NotImplementedError("Implement me")
