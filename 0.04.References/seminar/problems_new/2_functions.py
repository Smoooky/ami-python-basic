"""Задача 2. Функция — тоже объект.

Функцию можно присвоить переменной, передать аргументом, вернуть из другой
функции и положить в словарь. Здесь придётся сделать всё из этого списка.
"""

from collections.abc import Callable


def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Применить функцию к значению два раза подряд.

    apply_twice(inc, 5) — это inc(inc(5)).
    
    """
    return func(func(value))


def compose(
    outer: Callable[[int], int], inner: Callable[[int], int]
) -> Callable[[int], int]:
    """Новая функция: сначала inner, затем её результат — в outer.

    Возвращать нужно функцию, а не готовое значение: compose(double, inc)
    бесполезен, пока его не вызовут.
    """
    def composed(value: int):
        return outer(inner(value))

    return composed

def make_scaler(factor: int) -> Callable[[int], int]:
   def scale(value: int):
       return value * factor

   return scale
double = make_scaler(2)
ten_times = make_scaler(10)
double(10)

def call_table(
    ops: dict[str, Callable[[int, int], int]], name: str, a: int, b: int
) -> int:
    """Взять из словаря функцию под именем name и вызвать её на a и b.

    Считается, что name в словаре есть: словарь функций — обычный dispatch.
    """
    return ops[name](a, b)
    raise NotImplementedError("Implement me")
