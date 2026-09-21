"""Решение задачи 3 (problems_new/3_lookup.py)."""


def fetch(settings: dict[str, int | None], name: str) -> tuple[bool, int | None]:
    """`in` различает «ключа нет» и «значение None»; `get` достаёт значение."""
    return name in settings, settings.get(name)


def picked(settings: dict[str, int | None], names: list[str]) -> dict[str, int | None]:
    """Только заданные настройки; порядок и повторы решает словарь."""
    return {name: settings[name] for name in names if name in settings}


def count_missing(settings: dict[str, int | None], names: list[str]) -> int:
    """Разность множества имён и представления ключей."""
    return len(set(names) - settings.keys())


def first_unset(settings: dict[str, int | None], names: list[str]) -> str | None:
    """Первое отсутствующее имя по ходу обхода."""
    for name in names:
        if name not in settings:
            return name
    return None
