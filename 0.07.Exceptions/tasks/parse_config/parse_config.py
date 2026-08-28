ConfigValue = bool | int | str


class LineError(Exception):
    def __init__(self, line: int, reason: str) -> None:
        raise NotImplementedError("Implement me")


class MissingEqualsError(LineError):
    def __init__(self, line: int) -> None:
        raise NotImplementedError("Implement me")


class BadKeyError(LineError):
    def __init__(self, line: int, key: str) -> None:
        raise NotImplementedError("Implement me")


class BadValueError(LineError):
    def __init__(self, line: int, key: str) -> None:
        raise NotImplementedError("Implement me")


class DuplicateKeyError(LineError):
    def __init__(self, line: int, key: str, first_line: int) -> None:
        raise NotImplementedError("Implement me")


class ConfigError(Exception):
    def __init__(self, errors: list[LineError]) -> None:
        raise NotImplementedError("Implement me")


def parse_config(lines: list[str], strict: bool = True) -> dict[str, ConfigValue]:
    raise NotImplementedError("Implement me")


def check_config(lines: list[str]) -> list[LineError]:
    raise NotImplementedError("Implement me")
