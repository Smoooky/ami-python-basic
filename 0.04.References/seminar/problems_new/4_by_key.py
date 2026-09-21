"""Задача 4. Сортировка с ключом.

`sorted` и `max` не сравнивают элементы напрямую: они сравнивают результат
функции-ключа. Ключом годится и кортеж — он сравнивается по компонентам
слева направо.
"""

from collections.abc import Callable


def by_length_then_alpha(words: list[str]) -> list[str]:
    """Новый список: сначала короткие, при равной длине — по алфавиту.

    Подсказка: ключ-кортеж (длина, слово) сравнивается именно так —
    сначала первая компонента, при равенстве вторая.
    """
    raise NotImplementedError("Implement me")


def by_grade_desc(pairs: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Новый список пар «имя, оценка» по убыванию оценки."""
    raise NotImplementedError("Implement me")


def best_word(words: list[str], key: Callable[[str], int]) -> str:
    """Слово с наибольшим ключом; при равенстве — первое по порядку.

    Именно так ведёт себя `max` со сторонним ключом.
    """
    raise NotImplementedError("Implement me")


def ranked(words: list[str], key: Callable[[str], int]) -> list[str]:
    """Новый список по убыванию ключа. Исходный не меняется."""
    raise NotImplementedError("Implement me")
