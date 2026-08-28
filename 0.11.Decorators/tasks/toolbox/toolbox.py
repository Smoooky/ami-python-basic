from collections.abc import Callable
from typing import Any


def first_line(text: str | None) -> str:
    raise NotImplementedError("Implement me")


def once(func: Callable[..., Any]) -> Any:
    raise NotImplementedError("Implement me")


class Registry:
    """Набор команд, которые можно вызвать по имени."""

    def __init__(self) -> None:
        raise NotImplementedError("Implement me")

    def register(self, name: str, *, summary: str = "") -> Callable[[Callable[..., Any]], Any]:
        raise NotImplementedError("Implement me")

    def run(self, name: str, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("Implement me")

    def summary(self, name: str) -> str:
        raise NotImplementedError("Implement me")

    def names(self) -> list[str]:
        raise NotImplementedError("Implement me")

    def help(self) -> str:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __contains__(self, name: object) -> bool:
        raise NotImplementedError("Implement me")
