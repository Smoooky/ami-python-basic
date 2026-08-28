from enum import Enum


# Перечисление готово, менять его не нужно — только пользоваться.
class ErrorKind(Enum):
    FATAL = "fatal"
    LOOKUP = "lookup"
    ARITHMETIC = "arithmetic"
    OS = "os"
    VALUE = "value"
    TYPE = "type"
    OTHER = "other"


def error_kind(error: BaseException) -> ErrorKind:
    raise NotImplementedError("Implement me")


def is_retryable(error: BaseException) -> bool:
    raise NotImplementedError("Implement me")


def error_summary(errors: list[BaseException]) -> dict[ErrorKind, int]:
    raise NotImplementedError("Implement me")
