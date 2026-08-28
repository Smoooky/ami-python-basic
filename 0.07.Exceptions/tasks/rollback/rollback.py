from types import TracebackType
from typing import Any


class Rollback:
    def __init__(
        self,
        target: dict[str, Any],
        suppress: tuple[type[BaseException], ...] = (),
    ) -> None:
        raise NotImplementedError("Implement me")

    def __enter__(self) -> dict[str, Any]:
        raise NotImplementedError("Implement me")

    def __exit__(
        self,
        exctype: type[BaseException] | None,
        excinst: BaseException | None,
        exctb: TracebackType | None,
    ) -> bool:
        raise NotImplementedError("Implement me")
