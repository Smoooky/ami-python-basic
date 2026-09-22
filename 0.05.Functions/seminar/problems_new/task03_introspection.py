"""Задача 3. Функция под капотом.

Всё о функции видно и без модуля inspect: атрибут `__code__` хранит
байт-код и сведения о параметрах, `__defaults__` и `__kwdefaults__` —
значения по умолчанию, а в `co_flags` спрятаны биты о `*args` и
`**kwargs`. Читаем это вручную.
"""

from collections.abc import Callable
from typing import Any


def param_count(func: Callable[..., Any]) -> int:
    """Число явных параметров: позиционные плюс только именованные.

    `*args` и `**kwargs` не считаются. Для `def f(a, *, b)` это 2.
    """
    raise NotImplementedError("Implement me")


def defaults_table(func: Callable[..., Any]) -> dict[str, Any]:
    """Параметры с дефолтами -> их значения.

    Кортеж `__defaults__` выравнивается с хвостом позиционных параметров,
    именованные берутся из `__kwdefaults__`. Для `def f(a, b=1, *, c=2)`
    это {"b": 1, "c": 2}.
    """
    raise NotImplementedError("Implement me")


def accepts_star(func: Callable[..., Any]) -> tuple[bool, bool]:
    """Пара (есть ли *args, есть ли **kwargs).

    Оба факта закодированы битами в `func.__code__.co_flags`:
    0x04 — `*args`, 0x08 — `**kwargs`.
    """
    raise NotImplementedError("Implement me")


def short_signature(func: Callable[..., Any]) -> str:
    """Сигнатура одной строкой — так же, как её пишет сам Python.

    Примеры: "fa(x, /, y=1, *, z=2)", "fb(a, *args, **kw)", "fc()".
    Разделители `/` и `*` ставятся только когда есть соответствующие
    параметры; если есть только именованные без `*args`, звёздочка
    нужна сама по себе: "fd(*, debug=False)". Дефолты записываются
    в repr-виде.
    """
    raise NotImplementedError("Implement me")
