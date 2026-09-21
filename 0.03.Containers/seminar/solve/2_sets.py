"""Решение задачи 2 (problems_new/2_sets.py)."""


def either(first: list[str], second: list[str]) -> list[str]:
    """Значения хотя бы из одного списка: объединение + sorted."""
    return sorted(set(first) | set(second))


def common_to_all(lists: list[list[str]]) -> list[str]:
    """Значения из каждого списка: пересечение многих."""
    if not lists:
        return []
    common = set(lists[0])
    for other in lists[1:]:
        common &= set(other)
    return sorted(common)

def common_to_all(lists: list[list[str]]) -> list[str]:
    if not lists:
        return []
    return sorted(set.intersection(*map(set, lists)))



def no_overlap(first: list[str], second: list[str]) -> bool:
    """Нет ли общих значений: метод принимает любую последовательность."""
    return set(first).isdisjoint(second)


def same_members(first: list[str], second: list[str]) -> bool:
    """Одинаковый состав: повторы и порядок сравнение множеств игнорирует."""
    return set(first) == set(second)
