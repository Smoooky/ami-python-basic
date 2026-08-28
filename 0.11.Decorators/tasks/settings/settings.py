from collections.abc import Iterator
from typing import Any


def temporary(config: dict[str, Any], key: str, value: Any) -> Iterator[dict[str, Any]]:
    raise NotImplementedError("Implement me")


def section(log: list[str], name: str) -> Iterator[None]:
    raise NotImplementedError("Implement me")


def muted(*errors: type[BaseException]) -> Iterator[list[BaseException]]:
    raise NotImplementedError("Implement me")
