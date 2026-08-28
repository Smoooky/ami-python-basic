"""Задача 2. Проверки без переменной-флага.

Каждая функция — одна строка с `any` или `all`. Циклы с флагом «нашли или нет»
здесь не нужны. Обратите внимание на то, каким должен быть ответ на пустом
списке.
"""


def has_negative(numbers: list[int]) -> bool:
    """Есть ли в списке отрицательное число. На пустом списке — False."""
    raise NotImplementedError("Implement me")


def all_even(numbers: list[int]) -> bool:
    """Все ли числа чётные. Пустой список считается подходящим."""
    raise NotImplementedError("Implement me")


def any_starts_with(words: list[str], prefix: str) -> bool:
    """Начинается ли хотя бы одно слово с указанного начала.

    Готового метода для этого мы не проходили, но начало слова — это срез
    нужной длины.
    """
    raise NotImplementedError("Implement me")


def is_sorted(numbers: list[int]) -> bool:
    """Идут ли числа по неубыванию.

    Подсказка: список упорядочен, когда каждая соседняя пара упорядочена, а
    пары соседей даёт zip списка с его же срезом без первого элемента.
    """
    raise NotImplementedError("Implement me")


def no_blanks(rows: list[str]) -> bool:
    """Нет ли среди строк пустых или состоящих только из пробелов."""
    raise NotImplementedError("Implement me")
