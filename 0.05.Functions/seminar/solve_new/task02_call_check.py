"""Задача 2. Сопоставление вызова и сигнатуры — решения."""

from typing import Any


def kind_of(parameters: list[tuple[str, str]], name: str) -> str:
    """Вид параметра: "p", "n" или "k"; неизвестное имя — ""."""
    for param_name, kind in parameters:
        if param_name == name:
            return kind
    return ""


def bind(
    parameters: list[tuple[str, str]],
    defaults: set[str],
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> dict[str, Any]:
    """Раскладка корректного вызова: имя параметра -> значение."""
    bound: dict[str, Any] = {}
    positional = [n for n, k in parameters if k in ("p", "n")]
    for name, value in zip(positional, args, strict=False):
        bound[name] = value
    bound.update(kwargs)
    return bound


def problems_of(
    parameters: list[tuple[str, str]],
    defaults: set[str],
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> list[str]:
    """Все ошибки вызова сообщениями в духе CPython, в строгом порядке."""
    messages: list[str] = []
    positional = [n for n, k in parameters if k in ("p", "n")]
    by_name = dict(parameters)
    filled_positionally = {n for n, _ in zip(positional, args, strict=False)}

    if len(args) > len(positional):
        messages.append("лишний позиционный аргумент")

    for name, kind in parameters:
        if kind == "p" and name in kwargs:
            messages.append(f"параметр '{name}' только позиционный, а передан по имени")

    for name, kind in parameters:
        if kind == "n" and name in filled_positionally and name in kwargs:
            messages.append(f"несколько значений для параметра '{name}'")

    for name in kwargs:
        if name not in by_name:
            messages.append(f"неожидаемый именованный аргумент '{name}'")

    for name, _ in parameters:
        if name in filled_positionally or name in kwargs:
            continue
        if name not in defaults:
            messages.append(f"нет значения для параметра '{name}'")

    return messages
