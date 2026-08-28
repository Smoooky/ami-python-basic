from collections.abc import Callable
from typing import Any


def describe(*args: Any, **kwargs: Any) -> str:
    raise NotImplementedError("Implement me")


# Атрибуты, дописанные функции, mypy не видит. Если будете проверять решение
# типами, на таких строках понадобится `# type: ignore[attr-defined]`.
def traced(func: Callable[..., Any]) -> Any:
    raise NotImplementedError("Implement me")
