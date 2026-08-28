"""Задача 3. Сортировка и разворот: на месте и копией.

Методы списка меняют его на месте и возвращают None, а встроенные функции и
срезы дают новый список. Перепутать их легко, поэтому тесты проверяют и
возвращаемое значение, и то, что стало с исходным списком.
"""


def sort_in_place(values: list[int]) -> None:
    """Отсортировать список по возрастанию, сохранив сам объект."""
    raise NotImplementedError("Implement me")


def sorted_copy(values: list[int]) -> list[int]:
    """Новый отсортированный список. Исходный остаётся как был."""
    raise NotImplementedError("Implement me")


def reverse_in_place(values: list[int]) -> None:
    """Развернуть список задом наперёд, сохранив сам объект."""
    raise NotImplementedError("Implement me")


def reversed_copy(values: list[int]) -> list[int]:
    """Новый список в обратном порядке. Исходный остаётся как был."""
    raise NotImplementedError("Implement me")
