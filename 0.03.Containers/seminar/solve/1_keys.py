"""Решение задачи 1 (problems_new/1_keys.py)."""

Key = int | float | bool


def same_hash(first: Key, second: Key) -> bool:
    """Одинаков ли хеш двух значений."""
    return hash(first) == hash(second)


def collide_only(first: int, second: int) -> bool:
    """Совпал ли хеш у двух разных целых чисел."""
    return first != second and hash(first) == hash(second)


def who_stayed(pairs: list[tuple[Key, str]]) -> tuple[str, str]:
    """Ключ — от первой записи, значение — от последней."""
    squeezed = dict(pairs)          # равные ключи схлопываются в один
    key = next(iter(squeezed))
    return type(key).__name__, squeezed[key]
