from collections.abc import Iterable, Sequence
from typing import NamedTuple


class Match(NamedTuple):
    """Сыгранный матч. winner is None — ничья."""

    left: str
    right: str
    winner: str | None


def schedule(players: Sequence[str]) -> list[tuple[str, str]]:
    raise NotImplementedError("Implement me")


def missing(players: Sequence[str], played: Iterable[Match]) -> list[tuple[str, str]]:
    raise NotImplementedError("Implement me")


def standings(players: Sequence[str], played: Iterable[Match]) -> dict[str, int]:
    raise NotImplementedError("Implement me")


def podium(players: Sequence[str], played: Iterable[Match], count: int) -> list[tuple[str, int]]:
    raise NotImplementedError("Implement me")
