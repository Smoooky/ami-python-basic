from collections.abc import Iterator, MutableMapping
from typing import Any


class Vocabulary(MutableMapping[str, str]):
    def __init__(self, words: Any = ()) -> None:
        raise NotImplementedError("Implement me")

    @staticmethod
    def normalize(word: str) -> str:
        raise NotImplementedError("Implement me")

    def __getitem__(self, word: str) -> str:
        raise NotImplementedError("Implement me")

    def __setitem__(self, word: str, translation: str) -> None:
        raise NotImplementedError("Implement me")

    def __delitem__(self, word: str) -> None:
        raise NotImplementedError("Implement me")

    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError("Implement me")

    def __len__(self) -> int:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")
