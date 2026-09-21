"""Задача 2. Множества на списках.

Все функции получают списки, а не множества. Оператор `-` со списком справа не
работает, поэтому пользуйтесь методами: они принимают любую последовательность.

Порядок обхода множества непредсказуем, поэтому результат всегда возвращается
списком, упорядоченным по алфавиту.
"""


def only_first(first: list[str], second: list[str]) -> list[str]:
    """Значения, которые есть в первом списке и отсутствуют во втором."""
    raise NotImplementedError("Implement me")


def shared(first: list[str], second: list[str]) -> list[str]:
    """Значения, встречающиеся в обоих списках."""
    raise NotImplementedError("Implement me")


def exclusive(first: list[str], second: list[str]) -> list[str]:
    """Значения, которые есть ровно в одном из списков."""
    raise NotImplementedError("Implement me")


def contains_all(items: list[str], required: list[str]) -> bool:
    """Есть ли в items все значения из required. Повторы не важны."""
    raise NotImplementedError("Implement me")
