from collections.abc import Sequence


def menus(soups: Sequence[str], mains: Sequence[str]) -> list[tuple[str, str]]:
    raise NotImplementedError("Implement me")


def codes(alphabet: str, length: int) -> list[str]:
    raise NotImplementedError("Implement me")


def photos(people: Sequence[str]) -> list[tuple[str, ...]]:
    raise NotImplementedError("Implement me")


def teams(people: Sequence[str], size: int) -> list[tuple[str, ...]]:
    raise NotImplementedError("Implement me")


def scoops(flavours: Sequence[str], count: int) -> list[tuple[str, ...]]:
    raise NotImplementedError("Implement me")
