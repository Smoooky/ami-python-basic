"""Задача 3. Поиск в словаре, где None — обычное значение: второй заход.

`get` отвечает одинаково и на «ключа нет», и на «значение None», поэтому
различать эти случаи приходится самому — через `in` или вернув признак
«задана ли настройка» отдельным значением.
"""


def fetch(settings: dict[str, int | None], name: str) -> tuple[bool, int | None]:
    """Кортеж «задана ли настройка» и её значение.

    У незаданной настройки значение в кортеже — None; заданная со значением
    None так и возвращается: (True, None).
    """
    raise NotImplementedError("Implement me")


def picked(settings: dict[str, int | None], names: list[str]) -> dict[str, int | None]:
    """Словарь только из заданных настроек, перечисленных в names.

    Порядок пар — как в списке имён. Повторы имён не удваивают записи.
    """
    raise NotImplementedError("Implement me")


def count_missing(settings: dict[str, int | None], names: list[str]) -> int:
    """Сколько РАЗНЫХ имён из списка не задано."""
    raise NotImplementedError("Implement me")


def first_unset(settings: dict[str, int | None], names: list[str]) -> str | None:
    """Первое имя из списка, которого нет в настройках; если все заданы — None."""
    raise NotImplementedError("Implement me")
