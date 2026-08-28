from collections.abc import Iterable, MutableSequence
from typing import Any


class Route(MutableSequence[str]):
    def __init__(self, stops: Iterable[str] = ()) -> None:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __getitem__(self, index: Any) -> Any:
        raise NotImplementedError("Implement me")

    def __setitem__(self, index: Any, value: Any) -> None:
        raise NotImplementedError("Implement me")

    def __delitem__(self, index: Any) -> None:
        raise NotImplementedError("Implement me")

    def insert(self, index: int, value: str) -> None:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")
