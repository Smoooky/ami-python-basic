"""Задача 1. Конвейер функций — решения."""

from collections.abc import Callable
from typing import Any


def apply_each(funcs: list[Callable[[Any], Any]], value: Any) -> list[Any]:
    """Каждую функцию списка от одного и того же значения."""
    return [func(value) for func in funcs]


def thread(value: Any, funcs: list[Callable[[Any], Any]]) -> Any:
    """Пропустить значение через цепочку функций слева направо."""
    for func in funcs:
        value = func(value)
    return value


def partial_apply(
    func: Callable[..., Any], *fixed_args: Any, **fixed_kwargs: Any
) -> Callable[..., Any]:
    """Свой functools.partial: заранее зафиксировать часть аргументов."""

    def applied(*args: Any, **kwargs: Any) -> Any:
        merged = dict(fixed_kwargs)
        merged.update(kwargs)  # новые именованные перекрывают зафиксированные
        return func(*fixed_args, *args, **merged)

    return applied


def fuse(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Композиция: fuse(f, g)(x) == g(f(x)); fuse() — тождественная."""

    def composed(value: Any) -> Any:
        for func in funcs:
            value = func(value)
        return value

    return composed
