from collections.abc import Iterable


def top(scores: Iterable[int], count: int) -> list[int]:
    raise NotImplementedError("Implement me")


def worst(scores: Iterable[int], count: int) -> list[int]:
    raise NotImplementedError("Implement me")


class Leaderboard:
    """Таблица рекордов: держит только лучшие `size` результатов."""

    def __init__(self, size: int) -> None:
        raise NotImplementedError("Implement me")

    def add(self, score: int) -> bool:
        raise NotImplementedError("Implement me")

    def cutoff(self) -> int | None:
        raise NotImplementedError("Implement me")

    def best(self) -> list[int]:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")
