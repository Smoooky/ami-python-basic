"""Задача 3. Поиск в словаре, когда None — обычное значение.

Значением здесь может быть и None, поэтому `get` без оговорок не годится:
он отвечает одинаково и на «ключа нет», и на «значение None».
"""


def is_set(settings: dict[str, int | None], name: str) -> bool:
    """Задана ли настройка. Настройка со значением None считается заданной."""
    raise NotImplementedError("Implement me")


def value_or(settings: dict[str, int | None], name: str, default: int) -> int | None:
    """Значение настройки, а если её нет — default.

    Настройка, заданная как None, возвращается как None: подменять её нельзя.
    """
    raise NotImplementedError("Implement me")


def first_present(settings: dict[str, int | None], names: list[str], default: int) -> int | None:
    """Значение первой заданной настройки из списка имён.

    Если ни одна не задана — default. Настройка со значением None прекращает
    поиск и возвращается как None.
    """
    raise NotImplementedError("Implement me")


def missing(settings: dict[str, int | None], names: list[str]) -> list[str]:
    """Имена незаданных настроек, по алфавиту и без повторов."""
    raise NotImplementedError("Implement me")
