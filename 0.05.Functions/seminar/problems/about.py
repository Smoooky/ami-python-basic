"""Задача 2. Что можно узнать о функции, не вызывая её.

У функции есть имя и словарь аннотаций — оба доступны как обычные атрибуты.
Сами аннотации на выполнение не влияют, но прочитать их можно.
"""

from collections.abc import Callable
from typing import Any


def name_of(func: Callable[..., Any]) -> str:
    """Имя функции — то, под которым её объявили."""
    raise NotImplementedError("Implement me")


def is_annotated(func: Callable[..., Any]) -> bool:
    """Есть ли у функции хотя бы одна аннотация."""
    raise NotImplementedError("Implement me")


def annotations_of(func: Callable[..., Any]) -> dict[str, str]:
    """Аннотации функции, где вместо типов стоят их имена.

    Для `def double(x: int) -> int` результат — {"x": "int", "return": "int"}.

    Отдельный случай — аннотация `-> None`: в словаре под ключом "return"
    лежит сам объект None, а не тип. Имя его типа — "NoneType".
    """
    raise NotImplementedError("Implement me")


def returns(func: Callable[..., Any]) -> str:
    """Имя типа результата.

    Для `-> None` это "NoneType". Если результат не аннотирован вовсе —
    пустая строка. Различить эти два случая по значению нельзя, нужно
    смотреть, есть ли вообще ключ "return".
    """
    raise NotImplementedError("Implement me")
