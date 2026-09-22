"""Задача 4. Класс Version: своё состояние, равенство, хеш — решения."""

from __future__ import annotations


class Version:
    """Номер версии: major.minor."""

    created = 0

    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor
        Version.created += 1  # счётчик — поле класса, пишем в класс

    def bump_minor(self) -> Version:
        return Version(self.major, self.minor + 1)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return False
        return (self.major, self.minor) == (other.major, other.minor)

    def __hash__(self) -> int:
        return hash((self.major, self.minor))


def dedupe(versions: list[Version]) -> list[Version]:
    """Убрать повторы, сохранив порядок первого появления."""
    seen: set[Version] = set()
    unique: list[Version] = []
    for version in versions:
        if version not in seen:  # множество работает по хешу и равенству
            seen.add(version)
            unique.append(version)
    return unique
