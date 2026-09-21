"""Задача 2. Множества на списках — второй заход.

Функции по-прежнему получают списки, а не множества: операторы `|` и `&` со
списком справа не работают, зато методы принимают любую последовательность.
Порядок обхода множества непредсказуем, поэтому результаты-списки всегда
отсортированы по алфавиту.
"""


def either(first: list[str], second: list[str]) -> list[str]:
    """Значения, встречающиеся хотя бы в одном из списков, по алфавиту."""
    raise NotImplementedError("Implement me")


def common_to_all(lists: list[list[str]]) -> list[str]:
    """Значения, которые есть в каждом из списков, по алфавиту.

    Повторы внутри одного списка не важны. Если списков нет — ответ пуст.
    """
    raise NotImplementedError("Implement me")


def no_overlap(first: list[str], second: list[str]) -> bool:
    """Нет ли у двух списков ни одного общего значения."""
    raise NotImplementedError("Implement me")


def same_members(first: list[str], second: list[str]) -> bool:
    """Один и тот же состав значений — без учёта порядка и повторов."""
    raise NotImplementedError("Implement me")
