"""Решение задачи 4 (problems_new/4_by_key.py)."""

from collections.abc import Callable


def by_length_then_alpha(words: list[str]) -> list[str]:
    """Кортеж-ключ: сначала длина, при равенстве — само слово."""
    return sorted(words, key=lambda word: (len(word), word))


def by_grade_desc(pairs: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Ключ — оценка, порядок — обратный."""
    return sorted(pairs, key=lambda pair: pair[1], reverse=True)


def best_word(words: list[str], key: Callable[[str], int]) -> str:
    """max со сторонним ключом уже возвращает первый из равных."""
    return max(words, key=key)


def ranked(words: list[str], key: Callable[[str], int]) -> list[str]:
    """sorted всегда даёт новый список; reverse сохраняет устойчивость."""
    return sorted(words, key=key, reverse=True)
