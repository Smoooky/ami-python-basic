from collections.abc import Generator, Iterable


def tally() -> Generator[dict[str, int], str | None, None]:
    raise NotImplementedError("Implement me")


def feed(votes: Iterable[str]) -> dict[str, int]:
    raise NotImplementedError("Implement me")


def leaders(votes: Iterable[str]) -> Generator[str | None, None, None]:
    raise NotImplementedError("Implement me")
