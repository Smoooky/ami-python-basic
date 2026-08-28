from typing import Any


class Dealer:
    """Итератор: выдаёт карты по одной и помнит, сколько уже выдал."""

    def __init__(self, cards: list[str]) -> None:
        raise NotImplementedError("Implement me")

    def __iter__(self) -> Dealer:
        raise NotImplementedError("Implement me")

    def __next__(self) -> str:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")


class Deck:
    """Итерируемый объект: на каждый перебор выдаёт нового раздающего."""

    def __init__(self, cards: list[str]) -> None:
        raise NotImplementedError("Implement me")

    def __iter__(self) -> Dealer:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")


def is_iterable(value: Any) -> bool:
    raise NotImplementedError("Implement me")


def is_iterator(value: Any) -> bool:
    raise NotImplementedError("Implement me")
