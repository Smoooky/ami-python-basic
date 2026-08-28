from typing import Any


class Longer:
    def __init__(self, limit: int) -> None:
        raise NotImplementedError("Implement me")

    def __call__(self, text: str) -> bool:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")


class NoWords:
    def __init__(self, words: list[str]) -> None:
        raise NotImplementedError("Implement me")

    def __call__(self, text: str) -> bool:
        raise NotImplementedError("Implement me")

    def __repr__(self) -> str:
        raise NotImplementedError("Implement me")


def is_rule(value: Any) -> bool:
    raise NotImplementedError("Implement me")


def broken_rules(text: str, rules: list[Any]) -> list[int]:
    raise NotImplementedError("Implement me")


def accepted(texts: list[str], rules: list[Any]) -> list[str]:
    raise NotImplementedError("Implement me")
