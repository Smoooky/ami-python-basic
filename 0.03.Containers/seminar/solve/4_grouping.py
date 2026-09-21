"""Решение задачи 4 (problems_new/4_grouping.py)."""


def by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Группировка: пустой список группы создаёт setdefault."""
    groups: dict[str, list[str]] = {}
    for word in words:
        groups.setdefault(word[0], []).append(word)
    return groups


def word_counts(text: str) -> dict[str, int]:
    """Счётчик: дефолт 0 доставляет get."""
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def keys_by_value(mapping: dict[str, int]) -> dict[int, list[str]]:
    """Тот же setdefault, но ключом становится значение исходного словаря."""
    groups: dict[int, list[str]] = {}
    for key, value in mapping.items():
        groups.setdefault(value, []).append(key)
    return groups
