from collections import defaultdict
from collections.abc import Iterable, Mapping
from typing import Any


def by_club(pairs: Iterable[tuple[str, str]]) -> defaultdict[str, list[str]]:
    raise NotImplementedError("Implement me")


def tally(items: Iterable[str]) -> defaultdict[str, int]:
    raise NotImplementedError("Implement me")


def known(mapping: Mapping[str, Any], key: str) -> bool:
    raise NotImplementedError("Implement me")


def plain(mapping: Mapping[str, Any]) -> dict[str, Any]:
    raise NotImplementedError("Implement me")
