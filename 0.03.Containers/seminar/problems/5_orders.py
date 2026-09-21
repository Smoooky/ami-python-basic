"""Задача 5. Множество как память о просмотренном.

Множество здесь нужно не ради результата, а ради быстрой проверки «уже
встречалось». Результат при этом остаётся списком: у множества нет порядка, на
который можно положиться.
"""


def unique_ordered(values: list[str]) -> list[str]:
    """Значения без повторов в порядке первого появления."""
    raise NotImplementedError("Implement me")


def repeated(values: list[str]) -> list[str]:
    """Значения, встретившиеся больше одного раза, по алфавиту и без повторов."""
    raise NotImplementedError("Implement me")


def has_pair_with_sum(numbers: list[int], target: int) -> bool:
    """Есть ли в списке два элемента на разных местах, дающие в сумме target.

    Список проходится один раз: для очередного числа достаточно проверить,
    встречалось ли раньше дополняющее его до target.
    """
    raise NotImplementedError("Implement me")
