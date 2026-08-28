"""Задача 2. Изменить на месте или вернуть новый.

Функции, меняющие список на месте, ничего не возвращают и обязаны сохранять тот
же объект: тесты проверяют это через `is`. Функции, возвращающие новый список,
не имеют права трогать исходный.
"""


def extend_in_place(target: list[int], extra: list[int]) -> None:
    """Дописать значения в конец списка. Объект остаётся тем же."""
    raise NotImplementedError("Implement me")


def extended(source: list[int], extra: list[int]) -> list[int]:
    """Новый список из значений обоих. Исходный не меняется."""
    raise NotImplementedError("Implement me")


def replace_contents(target: list[int], values: list[int]) -> None:
    """Заменить содержимое списка целиком, не создавая новый объект."""
    raise NotImplementedError("Implement me")


def drop_odd(target: list[int]) -> None:
    """Убрать из списка нечётные числа, сохранив сам объект."""
    raise NotImplementedError("Implement me")
