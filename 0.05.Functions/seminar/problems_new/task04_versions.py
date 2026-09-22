"""Задача 4. Класс Version: своё состояние, равенство, хеш.

Номер версии документа — пара (major, minor). Объекты не мутируют:
bump_minor возвращает новый номер, а не меняет старый. Равные номера
должны схлопываться в set и работать ключами dict — это возможно только
при согласованной паре `__eq__`/`__hash__`.
"""

from __future__ import annotations


class Version:
    """Номер версии: major.minor."""

    created = 0

    def __init__(self, major: int, minor: int) -> None:
        """Запомнить координаты в полях major и minor.

        Каждое создание учитывается в счётчике created — поле класса,
        общее для всех версий.
        """
        raise NotImplementedError("Implement me")

    def bump_minor(self) -> Version:
        """Новая версия с minor на единицу больше.

        Исходная версия не меняется, результат — новый объект (и он тоже
        попадает в счётчик created).
        """
        raise NotImplementedError("Implement me")

    def __eq__(self, other: object) -> bool:
        """Равенство по координатам. Сравнение с чужим типом — False."""
        raise NotImplementedError("Implement me")

    def __hash__(self) -> int:
        """Хеш из кортежа координат: равные версии хешируются одинаково."""
        raise NotImplementedError("Implement me")


def dedupe(versions: list[Version]) -> list[Version]:
    """Убрать повторы, сохранив порядок первого появления.

    Подсказка: множество уже виденных версий — по хешу и равенству.
    """
    raise NotImplementedError("Implement me")
