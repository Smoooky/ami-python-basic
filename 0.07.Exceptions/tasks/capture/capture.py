from types import TracebackType


class Captured:
    def __init__(self) -> None:
        raise NotImplementedError("Implement me")

    def __enter__(self) -> Captured:
        raise NotImplementedError("Implement me")

    def __exit__(
        self,
        exctype: type[BaseException] | None,
        excinst: BaseException | None,
        exctb: TracebackType | None,
    ) -> None:
        raise NotImplementedError("Implement me")
