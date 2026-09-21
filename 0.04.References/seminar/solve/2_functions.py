"""Решение задачи 2 (problems_new/2_functions.py)."""

from collections.abc import Callable


def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Двойное применение — обычный вложенный вызов."""
    return func(func(value))


def compose(
    outer: Callable[[int], int], inner: Callable[[int], int]
) -> Callable[[int], int]:
    """Внутри определяем новую функцию и возвращаем сам объект-функцию."""

    def composed(value: int) -> int:
        return outer(inner(value))

    return composed


def make_scaler(factor: int) -> Callable[[int], int]:
    """Внутренняя функция помнит factor — это и есть независимое замыкание."""

    def scale(value: int) -> int:
        return value * factor

    return scale


def call_table(
    ops: dict[str, Callable[[int, int], int]], name: str, a: int, b: int
) -> int:
    """Словарь отображает имя в функцию; дальше — обычный вызов."""
    return ops[name](a, b)
