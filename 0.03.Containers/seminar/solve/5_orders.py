"""Решение задачи 5 (problems_new/5_orders.py)."""


def all_unique(values: list[str]) -> bool:
    """Повторы схлопываются во множестве: длины разошлись — был повтор."""
    return len(set(values)) == len(values)


def seen_once(values: list[str]) -> list[str]:
    """Сначала счётчик, затем фильтр: порядок задаёт исходный список."""
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return [value for value in values if counts[value] == 1]


def first_repeat(values: list[str]) -> str | None:
    """Множество как память: O(1) на проверку «уже видели»."""
    seen: set[str] = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None
