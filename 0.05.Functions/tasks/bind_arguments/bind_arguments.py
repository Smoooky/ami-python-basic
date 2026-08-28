from typing import Any


def bind_arguments(
    parameters: list[tuple[str, str]],
    defaults: dict[str, Any],
    args: list[Any],
    kwargs: dict[str, Any],
) -> dict[str, Any]:
    raise NotImplementedError("Implement me")
