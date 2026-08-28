from collections.abc import Callable


def make_counter(start: int = 0) -> Callable[[], int]:
    raise NotImplementedError("Implement me")


def make_adder(step: int) -> Callable[[int], int]:
    raise NotImplementedError("Implement me")


def make_multiplier(number: int) -> Callable[[int], int]:
    raise NotImplementedError("Implement me")


def multipliers(count: int) -> list[Callable[[int], int]]:
    raise NotImplementedError("Implement me")


def shared_counter(count: int) -> list[Callable[[], int]]:
    raise NotImplementedError("Implement me")
