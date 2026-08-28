from collections import Counter


def letter_counts(text: str) -> Counter[str]:
    raise NotImplementedError("Implement me")


def top(text: str, count: int) -> list[tuple[str, int]]:
    raise NotImplementedError("Implement me")


def is_anagram(left: str, right: str) -> bool:
    raise NotImplementedError("Implement me")


def can_build(word: str, letters: str) -> bool:
    raise NotImplementedError("Implement me")


def missing(word: str, letters: str) -> Counter[str]:
    raise NotImplementedError("Implement me")
