def chunk(data: bytearray, start: int, size: int) -> memoryview:
    raise NotImplementedError("Implement me")


def copy_chunk(data: bytearray, start: int, size: int) -> bytearray:
    raise NotImplementedError("Implement me")


def total(window: memoryview) -> int:
    raise NotImplementedError("Implement me")


def overwrite(window: memoryview, values: list[int]) -> None:
    raise NotImplementedError("Implement me")


def is_shared(window: memoryview, data: bytearray) -> bool:
    raise NotImplementedError("Implement me")
