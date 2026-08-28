from error_kind import ErrorKind, error_kind, error_summary, is_retryable


def test_basic_kinds() -> None:
    assert error_kind(KeyError("user")) is ErrorKind.LOOKUP
    assert error_kind(ZeroDivisionError()) is ErrorKind.ARITHMETIC
    assert error_kind(FileNotFoundError()) is ErrorKind.OS
    assert error_kind(ValueError("плохой ввод")) is ErrorKind.VALUE
    assert error_kind(TypeError()) is ErrorKind.TYPE
    assert error_kind(AttributeError()) is ErrorKind.OTHER


def test_fatal_is_not_an_exception() -> None:
    assert error_kind(KeyboardInterrupt()) is ErrorKind.FATAL
    assert error_kind(SystemExit()) is ErrorKind.FATAL


def test_retryable() -> None:
    assert is_retryable(ConnectionResetError()) is True
    assert is_retryable(FileNotFoundError()) is False


def test_summary() -> None:
    summary = error_summary([KeyError(), IndexError(), TypeError()])
    assert summary == {ErrorKind.LOOKUP: 2, ErrorKind.TYPE: 1}
    assert error_summary([]) == {}
