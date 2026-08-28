from typing import Any, Protocol


# Объявите здесь протокол: два метода и пометка @runtime_checkable.
class Pinnable(Protocol):
    """Всё, что можно повесить на доску объявлений."""


class Note:
    """Записка. Наследоваться от Pinnable не нужно и нельзя."""

    def __init__(self, title: str, text: str) -> None:
        raise NotImplementedError("Implement me")

    def title(self) -> str:
        raise NotImplementedError("Implement me")

    def lines(self) -> list[str]:
        raise NotImplementedError("Implement me")


def render(item: Pinnable) -> str:
    raise NotImplementedError("Implement me")


def pin_all(items: list[Any]) -> list[str]:
    raise NotImplementedError("Implement me")


def broken_pins(items: list[Any]) -> list[int]:
    raise NotImplementedError("Implement me")
