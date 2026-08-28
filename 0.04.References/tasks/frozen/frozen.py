from typing import Any

# Значения, которые нельзя изменить: их считаем «замороженными» сами по себе.
ATOMS = (int, float, complex, bool, str, bytes, type(None))


def is_frozen(value: Any) -> bool:
    raise NotImplementedError("Implement me")


def mutable_parts(value: Any, path: tuple[int, ...] = ()) -> list[tuple[int, ...]]:
    raise NotImplementedError("Implement me")


def freeze(value: Any) -> Any:
    raise NotImplementedError("Implement me")


def thaw(value: Any) -> Any:
    raise NotImplementedError("Implement me")
