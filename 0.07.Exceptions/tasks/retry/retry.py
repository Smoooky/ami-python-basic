from typing import Any, Callable  # noqa: UP035  — в лекции показан именно typing.Callable


class RetryError(Exception):
    def __init__(self, attempts: int, last_error: BaseException) -> None:
        raise NotImplementedError("Implement me")


def retry(
    action: Callable[[], Any],
    attempts: int = 3,
    retry_on: tuple[type[BaseException], ...] = (Exception,),
) -> Any:
    raise NotImplementedError("Implement me")
