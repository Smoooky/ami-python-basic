"""Задача 3. Функция под капотом — решения."""

from collections.abc import Callable
from typing import Any

_CO_VARARGS = 0x04
_CO_VARKEYWORDS = 0x08


def param_count(func: Callable[..., Any]) -> int:
    """Число явных параметров: позиционные плюс только именованные."""
    code = func.__code__
    return code.co_argcount + code.co_kwonlyargcount


def defaults_table(func: Callable[..., Any]) -> dict[str, Any]:
    """Параметры с дефолтами -> их значения."""
    code = func.__code__
    names = code.co_varnames
    table: dict[str, Any] = {}
    defaults = func.__defaults__ or ()
    if defaults:
        # Хвост позиционных параметров выравнивается с __defaults__.
        start = code.co_argcount - len(defaults)
        for name, value in zip(names[start : code.co_argcount], defaults, strict=True):
            table[name] = value
    table.update(func.__kwdefaults__ or {})
    return table


def accepts_star(func: Callable[..., Any]) -> tuple[bool, bool]:
    """Пара (есть ли *args, есть ли **kwargs) — биты в co_flags."""
    flags = func.__code__.co_flags
    return bool(flags & _CO_VARARGS), bool(flags & _CO_VARKEYWORDS)


def _with_defaults(names: tuple[str, ...], table: dict[str, Any]) -> list[str]:
    return [f"{name}={table[name]!r}" if name in table else name for name in names]


def short_signature(func: Callable[..., Any]) -> str:
    """Сигнатура одной строкой — так же, как её пишет сам Python."""
    code = func.__code__
    names = code.co_varnames
    table = defaults_table(func)
    has_args = bool(code.co_flags & _CO_VARARGS)
    has_kwargs = bool(code.co_flags & _CO_VARKEYWORDS)

    parts: list[str] = []
    parts.extend(_with_defaults(names[: code.co_posonlyargcount], table))
    if code.co_posonlyargcount:
        parts.append("/")

    index = code.co_argcount
    parts.extend(_with_defaults(names[code.co_posonlyargcount : index], table))

    # Порядок в co_varnames: позиционные, *args, только именованные, **kwargs.
    if has_args:
        parts.append(f"*{names[index]}")
        index += 1
    kwonly = names[index : index + code.co_kwonlyargcount]
    index += code.co_kwonlyargcount
    if not has_args and code.co_kwonlyargcount:
        parts.append("*")
    parts.extend(_with_defaults(kwonly, table))

    if has_kwargs:
        parts.append(f"**{names[index]}")
    return f"{func.__name__}({', '.join(parts)})"
