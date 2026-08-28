from typing import Any


def same_object(left: Any, right: Any) -> bool:
    raise NotImplementedError("Implement me")


def same_value(left: Any, right: Any) -> bool:
    raise NotImplementedError("Implement me")


def describe(left: Any, right: Any) -> str:
    raise NotImplementedError("Implement me")


def shared_positions(left: list[Any], right: list[Any]) -> list[int]:
    raise NotImplementedError("Implement me")


def distinct_objects(values: list[Any]) -> int:
    raise NotImplementedError("Implement me")
