from typing import Any


def dig(data: Any, path: list[Any], default: Any = None) -> Any:
    raise NotImplementedError("Implement me")


def has_path(data: Any, path: list[Any]) -> bool:
    raise NotImplementedError("Implement me")


def flatten(data: Any, paths: dict[str, list[Any]]) -> dict[str, Any]:
    raise NotImplementedError("Implement me")
