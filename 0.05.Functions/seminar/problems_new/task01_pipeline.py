"""Задача 1. Конвейер функций.

Функция — обычный объект: её можно положить в список, передать в другую
функцию и вернуть из неё. Подзадачи идут от простого к сложному и все
про одно — собрать из функций конвейер.
"""

from collections.abc import Callable
from typing import Any


def apply_each(funcs: list[Callable[[Any], Any]], value: Any) -> list[Any]:
    """Каждую функцию списка от одного и того же значения.

    Для [f, g] и value результат — [f(value), g(value)].
    """
    raise NotImplementedError("Implement me")


def thread(value: Any, funcs: list[Callable[[Any], Any]]) -> Any:
    """Пропустить значение через цепочку функций слева направо.

    Для value и [f, g] результат — g(f(value)). Пустой список —
    само значение без изменений.
    """
    raise NotImplementedError("Implement me")


def partial_apply(
    func: Callable[..., Any], *fixed_args: Any, **fixed_kwargs: Any
) -> Callable[..., Any]:
    """Свой functools.partial: заранее зафиксировать часть аргументов.

    Вызов результата подставляет fixed_args впереди новых позиционных
    аргументов, а именованные новые перекрывают fixed_kwargs.
    Готовым functools.partial пользоваться нельзя — только вложенной
    функцией.
    """
    raise NotImplementedError("Implement me")


def fuse(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Композиция без списков: fuse(f, g)(x) == g(f(x)).

    Функции применяются в порядке передачи: сначала f, потом g.
    fuse() без аргументов — тождественная функция.
    """
    raise NotImplementedError("Implement me")
