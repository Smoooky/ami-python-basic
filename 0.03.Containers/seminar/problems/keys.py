"""Задача 1. Когда два значения — один ключ.

Числа разных типов, равные друг другу, попадают в словарь как один ключ.
Функции ниже позволяют это проверить, не заглядывая в теорию.
"""

Key = int | float | bool


def same_key(first: Key, second: Key) -> bool:
    """Окажутся ли два значения одним и тем же ключом словаря.

    Проверять хеши напрямую не нужно: достаточно построить словарь из обоих
    значений и посмотреть на его размер.
    """
    raise NotImplementedError("Implement me")


def surviving_type(first: Key, second: Key) -> str:
    """Имя типа ключа, который останется в словаре, если положить туда сначала
    first, а потом second: "int", "float" или "bool".

    Если значения разные, остаётся тип первого из них.
    """
    raise NotImplementedError("Implement me")


def distinct_count(values: list[Key]) -> int:
    """Сколько различных ключей получится из списка значений."""
    raise NotImplementedError("Implement me")
