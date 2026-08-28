from collections import abc
from typing import Any

# Кортеж готов, менять его не нужно — только пользоваться.
CHECKED: tuple[Any, ...] = (
    abc.Sized,
    abc.Iterable,
    abc.Container,
    abc.Hashable,
    abc.Callable,
    abc.Sequence,
    abc.MutableSequence,
    abc.Mapping,
    abc.MutableMapping,
    abc.Set,
)


def looks_like(value: Any, *names: str) -> bool:
    raise NotImplementedError("Implement me")


def is_hashable(value: Any) -> bool:
    raise NotImplementedError("Implement me")


def abc_names(value: Any) -> set[str]:
    raise NotImplementedError("Implement me")


def hash_promise_broken(value: Any) -> bool:
    raise NotImplementedError("Implement me")
